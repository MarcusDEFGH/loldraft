# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from ..items import Game
from ..constants import XPATHS_LADDER, XPATHS_GAME


class OpggSpider(scrapy.Spider):
    name = 'opgg'
    allowed_domains = ['op.gg']
    servers = ['br', 'jp', 'euw', 'oce', 'lan', 'tr', 'www', 'na', 'eune',
               'las', 'ru']
    start_urls = ['http://' +
                  server + '.op.gg/ranking/ladder/' for server in servers]

    def _parse_champions(self, selector):
        for champion in selector:
            yield champion.xpath(XPATHS_GAME['_champion_name']).extract_first()

    def _parse_profile_links(self, selector):
        for summoner in selector:
            link = selector.xpath(XPATHS_GAME['profile_link']).extract_first()
            meta = response.meta.copy()
            meta.update({'related': True})
            yield Request(url="http:" + link,
                          callback=self.parse_games, meta=meta)

    def parse(self, response):
        summoners = response.xpath(XPATHS_LADDER['_summoners']).extract()
        for summoner in summoners:
            yield Request(url="http:"+summoner, callback=self.parse_games)

    def parse_games(self, response):
        matches = response.xpath(XPATHS_GAME['_matches'])
        for match in matches:
            summoners_t1 = match.xpath(XPATHS_GAME['_summoners_team_1'])
            summoners_t2 = match.xpath(XPATHS_GAME['_summoners_team_2'])
            if not response.meta.get('related'):
                self._parse_profile_links(summoners_t1)
                self._parse_profile_links(summoners_t2)

            match_type = match.xpath(XPATHS_GAME['_match_type']
                                     ).extract_first().strip()
            result = response.xpath(XPATHS_GAME['result']
                                    ).extract_first().strip()
            if match_type != 'Ranked Solo' or result == 'Remake':
                continue

            selector_t1 = match.xpath(XPATHS_GAME['_champions_team_1'])
            selector_t2 = match.xpath(XPATHS_GAME['_champions_team_2'])
            team_1 = list(self._parse_champions(selector_t1))
            team_2 = list(self._parse_champions(selector_t2))

            item = Game()
            result = response.xpath(
                XPATHS_GAME['result']).extract_first().strip()
            player = response.xpath(XPATHS_GAME['player']).extract_first()
            players_t1 = [summoner.xpath(
                          './/text()'
                          ).extract()[1] for summoner in summoners_t1]
            if player in players_t1:
                if result == 'Victory':
                    item['result'] = 'Victory'
                else:
                    item['result'] = 'Defeat'
            else:
                if result == 'Victory':
                    item['result'] = 'Defeat'
                else:
                    item['result'] = 'Victory'
            item['server'] = response.url.split('/')[2].split('.')[0]
            item['mmr'] = response.xpath(XPATHS_GAME['mmr']).extract_first()
            item['team_1'] = team_1
            item['team_2'] = team_2
            item['timestamp'] = match.xpath(XPATHS_GAME['timestamp']
                                            ).extract_first()

            yield item
