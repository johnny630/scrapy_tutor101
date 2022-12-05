import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy_tutor101.spiders.stock_rank import StockRankSpider

process = CrawlerProcess(settings=get_project_settings())
process.crawl(StockRankSpider)
process.start()
