# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OrdoItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    description = scrapy.Field()
    date_created = scrapy.Field()
    last_updated = scrapy.Field()
    phone_number = scrapy.Field()
    price = scrapy.Field()
    m2 = scrapy.Field()
    city = scrapy.Field()

class Flat(OrdoItem):
    room = scrapy.Field()
    floor = scrapy.Field()
