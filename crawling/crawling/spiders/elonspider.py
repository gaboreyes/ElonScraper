import scrapy
#import del item creado basado en el modelo de mi db
from crawling.items import Spacex_Item

class ElonSpider(scrapy.Spider):
    name = "elonspider"
    start_urls = ["https://www.spacex.com/news"]


    def parse(self, response):
        #instancia del item
        item = Spacex_Item()
        item["titulo"] = response.css("h2.title > a").extract_first()
        item["body"] = response.css("div.summary > p").extract_first()
        item["fecha"] = response.css("div.date").extract_first()
        yield item