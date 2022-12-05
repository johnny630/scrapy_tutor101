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
