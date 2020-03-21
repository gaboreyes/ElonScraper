import scrapy
#import del item creado basado en el modelo de mi db
from crawling.items import Spacex_Item

#import para tener acceso a los modelos almacenados
from spacex.models import SpacexItem

class ElonSpider(scrapy.Spider):
    name = "elonspider"
    start_urls = ["https://www.spacex.com/news"]


    def parse(self, response):

        #dropeo de la tabla Spacex Items luego de cada crawl
        SpacexItem.objects.all().delete()
        print('OBJECTS DELETED')

        #var que almacena todos los divs que tienen un post
        all_post = response.css('div.views-row')
        
        #ciclo que glides over each post dentro de la lista de posts
        for post in all_post:
            #instancia del item
            item = Spacex_Item()
            #variables que almacenan la info de cada post
            item["titulo"] = post.css("h2.title > a::text").extract()
            item["body"] = post.css("div.summary > p::text").extract()
            item["fecha"] = post.css("div.date::text").extract()
            yield item