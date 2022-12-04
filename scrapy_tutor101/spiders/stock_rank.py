import scrapy


class StockRankSpider(scrapy.Spider):
    name = "stock_rank"
    allowed_domains = ["histock.tw"]
    start_urls = ["http://histock.tw/stock/rank.aspx/"]

    def parse(self, response):
        selectors = response.selector.xpath(
            '//table[@class="gvTB"]/tr[position()>1]'
        )  # get selector list
        result = [
            (
                tr.xpath("td[1]/text()").get(),
                tr.xpath("td[2]/a/text()").get(),
                tr.xpath("td[3]/span/text()").get(),
            )
            for tr in selectors
        ]

        css_selectors = response.css("table.gvTB>tr")[1:-1]
        css_result = [
            (
                tr.css("td:first-child::text").get(),
                tr.css("td:nth-child(2)>a::text").get(),
                tr.css("td:nth-child(3)>span::text").get(),
            )
            for tr in css_selectors
        ]

        yield {"result": result, "css_result": css_result}

        next_page_link = response.selector.xpath(
            '//div[@class="pager"]/a[text()="下一頁 >"]/@href'
        ).get()

        if next_page_link:
            yield response.follow(url=next_page_link, callback=self.parse)
