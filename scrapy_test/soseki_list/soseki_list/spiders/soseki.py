import scrapy
class SosekiSpyder(scrapy.Spider):
  name = 'soseki'
  start_urls = [
    'https://www.aozora.gr.jp/index_pages/person148.html'
  ]

  def parse(self, response):
    title = response.css('title')
    print(title.extract())

