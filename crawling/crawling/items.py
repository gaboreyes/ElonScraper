# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

#import del item de django SpacexItem para poder convertirlo en un DJANGOITEM reconocible por scrapy
from scrapy_djangoitem import DjangoItem
from spacex.models import SpacexItem

#Sustituir el item default por un djangoitem que se comunique con el modelo que ya habiamos creado
class Spacex_Item(DjangoItem):
    django_model = SpacexItem
    # define the fields for your item here like:
    #name = scrapy.Field()

