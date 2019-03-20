# -*- coding: utf-8 -*-
import scrapy
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class WxsearchSpider(scrapy.Spider):
    name = 'wxsearch'
    #allowed_domains = ['www.baidu.com']#显示爬虫下载范围
    start_urls = ['https://tieba.baidu.com/f?kw=剑网三交易&ie=utf-8&pn=0']#开始url，在下一次会自动变为下一个url

    def parse(self, response):
        print response.body
