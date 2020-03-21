# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


from spacex.models import SpacexItem

class CrawlingPipeline(object):

    def process_item(self, item, spider):
        #[0] porque siempre vas a estar procesando listas de 1 elemento con cada yield del item

        #print("Pipeline: " + item['titulo'][0])
        #print("Pipeline: " + item['fecha'][0])
        #print("Pipeline: " + item['body'][0])
        #item.save()

        #crea una instancia de SpacexItem con la data guardada en la var item que viene del yield en el spider.py
        SpacexItem.objects.create(
            titulo=item['titulo'][0],
            body=item['body'][0],
            fecha=item['fecha'][0],
        )
        return item
