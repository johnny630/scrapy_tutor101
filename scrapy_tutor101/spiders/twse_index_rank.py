import scrapy
from scrapy_splash import SplashRequest

class TwseIndexRankSpider(scrapy.Spider):
    name = 'twse_index_rank'
    allowed_domains = ['twse.com.tw']
    url = 'https://www.twse.com.tw/zh/'

    # Here no used  
    # splash:on_request(function(request)
    #     request:set_header("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")
    # end)
    lua_script = '''
    function main(splash, args)
        splash.private_mode_enabled = false
        assert(splash:go{args.url, headers=splash.args.headers})
        assert(splash:wait(3))
        splash:set_viewport_full()
        return splash:html()
    end
    '''

    def start_requests(self):
        yield SplashRequest(
            url=self.url,
            callback=self.parse,
            endpoint='execute',
            args={
                'lua_source': self.lua_script
            }
        )

    def parse(self, response):
        stock_list = response.xpath('//table[@class="list link"]/tbody')[0].xpath('./tr')

        for stock in stock_list:
            stock_tds = stock.xpath('.//td/text()')
            yield {"id": stock_tds[0].get(), "name": stock_tds[1].get(), "price": stock_tds[2].get()}
