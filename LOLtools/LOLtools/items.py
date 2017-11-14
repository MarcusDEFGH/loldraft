# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LoltoolsItem(scrapy.Item):
    elo = scrapy.Field()
    resultado = scrapy.Field()
    time_1 = scrapy.Field()
    time_2 = scrapy.Field()
    timestamp = scrapy.Field()
