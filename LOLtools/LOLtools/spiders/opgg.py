# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.contrib.spiders import CrawlSpider
from ..items import LoltoolsItem
from ..constants import XPATHS_JOGO


class OpggSpider(scrapy.Spider):
    name = 'opgg'
    allowed_domains = ['op.gg']
    start_urls = ['http://br.op.gg/summoner/userName=paintay',
                  'http://br.op.gg/summoner/userName=highnoon',
                  'http://br.op.gg/summoner/userName=yopresidente1v9',
                  'http://na.op.gg/summoner/userName=imaqtpie',
                  'http://na.op.gg/summoner/userName=chowdog',
                  'http://na.op.gg/summoner/userName=plankgang',
                  'http://na.op.gg/summoner/userName=The%20Trump%20Trane']

    def parse(self, response):

        partidas = response.xpath(XPATHS_JOGO['_partidas'])
        for partida in partidas:
            tipo = partida.xpath(XPATHS_JOGO['_tipo']).extract_first().strip()
            if tipo != 'Ranked Solo':
                continue
            time_1 = []
            time_2 = []
            resultado = response.xpath(XPATHS_JOGO['resultado']).extract_first().strip()
            champions_time_1 = partida.xpath(XPATHS_JOGO['time_1'])
            champions_time_2 = partida.xpath(XPATHS_JOGO['time_2'])
            for champion in champions_time_1:
                champ = champion.xpath(XPATHS_JOGO['champion']).extract_first()
                time_1.append(champ)
            for champion in champions_time_2:
                champ = champion.xpath(XPATHS_JOGO['champion']).extract_first()
                time_2.append(champ)

            item = LoltoolsItem()
            item['resultado'] = resultado
            item['elo'] = response.xpath(XPATHS_JOGO['elo']).extract_first()
            item['time_1'] = time_1
            item['time_2'] = time_2
            item['timestamp'] = response.xpath(XPATHS_JOGO['timestamp']).extract_first()


            yield item
