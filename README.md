# Scrapy tutor 101

## Changing user agent

You can use `response.request.headers` know what is the user agent.

1. revise `settings.py` `USER_AGENT`
2. revise `settings.py` `DEFAULT_REQUEST_HEADERS`, Dict add `User-Agent`
3. revise spieder code `response.follow` or `scrapy.Request` `headers` argument add `User-Agent`

## Debugging

https://docs.scrapy.org/en/latest/topics/debug.html

### 1. Parse Command

directly assigen which spider method you want to test.  
e.g.: `scrapy parse --spider=stock_rank -c parse -d 3 https://histock.tw/stock/rank.aspx?&p=3&d=1`

`-c`: you want to test method  
`-d`: depth level  
`--meta`: e.g. `--meta='{\"key\":\"value\"}'`

### 2. Scrapy Shell

enter shell mode to debug
`inspect_response(response, self)`

then in terminal run `scrapy crawl stock_rank`

### 3. Open in browser

`open_in_browser(response)`

### 4. Logging

`self.logger.warning()`

### 5. VSCode break point

create runner.py

1. VSCode terminal environment choose scrapy version.
2. VSCode IDE / Run / Start Debugging

## generate spider with crawl template

e.g. `scrapy genspider -t crawl stock_news https://histock.tw/stock/rank.aspx`

### Rule

https://docs.scrapy.org/en/latest/topics/spiders.html?highlight=Rule#crawling-rules

### linkExtractors

https://docs.scrapy.org/en/latest/topics/link-extractors.html?highlight=linkextra#module-scrapy.linkextractors.lxmlhtml

## Scrapy & Splash

https://github.com/scrapy-plugins/scrapy-splash

## install splash with Docker

pull splash image
`docker pull scrapinghub/splash`

run splash
`docker run -it -p 8050:8050 scrapinghub/splash`

### settings.py config

1. add `SPLASH_URL = 'http://127.0.0.1:8050'`
2. add

```
DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}
```

3. add

```
SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}
```

4. add `DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'`

##

## Selenium

[Official Website](https://www.selenium.dev/)  
[Python Selenium](https://pypi.org/project/selenium/)

[Selenium Cheat Sheet](http://allselenium.info/python-selenium-commands-cheat-sheet-frequently-used/)
[Selenium with Python 中文翻译文档](https://selenium-python-zh.readthedocs.io/en/latest/)

### Install

1. `pip install selenium`
2. download driver by different browser (要注意你的 broswer 版本號)
3. upt the driver to your python path.
