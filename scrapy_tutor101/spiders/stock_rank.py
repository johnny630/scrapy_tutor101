import scrapy
from urllib.parse import urlparse, parse_qs


class StockRankSpider(scrapy.Spider):
    name = "stock_rank"
    allowed_domains = ["histock.tw"]
    start_urls = ["http://histock.tw/stock/rank.aspx/"]

    def parse(self, response):
        css_selectors = response.css("table.gvTB>tr")[1:-1]
        css_result = [
            (
                tr.css("td:first-child::text").get(),
                tr.css("td:nth-child(2)>a::text").get(),
                tr.css("td:nth-child(3)>span::text").get(),
            )
            for tr in css_selectors
        ]

        # export each stock
        for stock in css_result:
            yield {"id": stock[0], "name": stock[1], "price": stock[2]}

        next_page_link = response.selector.xpath(
            '//div[@class="pager"]/a[text()="下一頁 >"]/@href'
        ).get()

        if next_page_link:
            yield response.follow(url=next_page_link, callback=self.parse)
