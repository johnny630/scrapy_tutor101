import scrapy


class StockRankSpider(scrapy.Spider):
    name = 'stock_rank'
    allowed_domains = ['histock.tw/stock/rank.aspx']
    start_urls = ['http://histock.tw/stock/rank.aspx/']

    def parse(self, response):
        pass
