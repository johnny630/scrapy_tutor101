# Scrapy tutor 101

## Changing user agent
You can use `response.request.headers` know what is the user agent.

1. revise `settings.py` `USER_AGENT`
2. revise `settings.py` `DEFAULT_REQUEST_HEADERS`, Dict add `User-Agent`
3. revise spieder code `response.follow` or `scrapy.Request` `headers` argument add  `User-Agent`