# -*- coding: utf-8 -*-
import scrapy


class Soseki3Spider(scrapy.Spider):
    name = 'soseki3'
    allowed_domains = ['www.aozor.gr.jp']
    start_urls = ['https://www.aozor.gr.jp/']

    def parse(self, response):
      li_list = response.css('ol > li a')
      for a in li_list:
        href = a.css('::attr(href)').extract_first()
        text = a.css('::text').extract_first()
        href2 = response.urljoin(href)
          
    def parse_card(self, response):

