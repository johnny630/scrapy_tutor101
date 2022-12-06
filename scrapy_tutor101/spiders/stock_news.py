import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class StockNewsSpider(CrawlSpider):
    name = 'stock_news'
    allowed_domains = ['histock.tw']
    start_urls = ['https://histock.tw/stock/rank.aspx?m=11']

    rules = (
        Rule(
            LinkExtractor(restrict_xpaths='//table[@class="gvTB"]', allow=r'stock/\d+'),
            callback='parse_news',
            follow=True
        ),
    )

    def parse_news(self, response):
        self.logger.info(response.request.meta)

        stock_name = response.request.meta.get('link_text')
        news_list = response.xpath('//div[@class="tb-list tbNews"]/a')

        for news in news_list:
            yield {
                'stock_name': stock_name,
                'title': news.xpath('@title').get(),
                'link': news.xpath('@href').get()
            }
