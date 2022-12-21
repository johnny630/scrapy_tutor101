import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
import time

class TwseIndexRankSeleniumSpider(scrapy.Spider):
    name = 'twse_index_rank_selenium'
    allowed_domains = ['twse.com.tw']
    start_urls = ["https://www.twse.com.tw/zh/"] # 一定要有 start_urls

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')

        browser = webdriver.Chrome(options=chrome_options)
        # 嘗試幾種selenium 的等待但好像都沒什麼作用，最後決定先用sleep處理
        # https://www.selenium.dev/documentation/webdriver/waits/

        # browser.implicitly_wait(10)
        browser.get('https://www.twse.com.tw/zh/')
        # WebDriverWait(browser, timeout=100).until(
        #     # lambda d: d.find_element(By.CLASS_NAME,"list link")
        #     EC.presence_of_element_located((By.CLASS_NAME,"list link"))
        # )
        time.sleep(5)

        self.html = browser.page_source
        browser.close()

    def parse(self, response):
        resp = Selector(text=self.html)
        stock_list = resp.xpath('//table[@class="list link"]/tbody')[0].xpath('./tr')

        for stock in stock_list:
            stock_tds = stock.xpath('.//td/text()')
            yield {"id": stock_tds[0].get(), "name": stock_tds[1].get(), "price": stock_tds[2].get()}
