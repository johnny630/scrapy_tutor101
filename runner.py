import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy_tutor101.spiders.stock_rank import StockRankSpider
from scrapy_tutor101.spiders.twse_index_rank import TwseIndexRankSpider
from scrapy_tutor101.spiders.twse_index_rank_selenium import TwseIndexRankSeleniumSpider

process = CrawlerProcess(settings=get_project_settings())
process.crawl(TwseIndexRankSeleniumSpider)
process.start()
