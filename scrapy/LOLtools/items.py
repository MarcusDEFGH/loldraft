# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Game(scrapy.Item):
    timestamp = scrapy.Field()
    server = scrapy.Field()
    mmr = scrapy.Field()
    result = scrapy.Field()
    team_1 = scrapy.Field()
    team_2 = scrapy.Field()
