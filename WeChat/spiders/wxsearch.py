# -*- coding: utf-8 -*-
import scrapy
import sys
from scrapy import Request
from WeChat.items import WechatItem
reload(sys)
sys.setdefaultencoding("utf-8")

class WxsearchSpider(scrapy.Spider):
    name = 'wxsearch'
    #allowed_domains = ['www.baidu.com']#显示爬虫下载范围

    def start_requests(self):
        start_urls = ['https://www.baidu.com/s?ie=utf-8&wd=a&pn={}'.format(page) for page in range(0,40,10)]#开始url，在下一次会自动变为下一个url
        for url in start_urls:
            yield Request(url=url,callback=self.parse)

    def parse(self, response):
        print response.url
        print response




