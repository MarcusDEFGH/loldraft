# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.contrib.spiders import CrawlSpider
from ..items import LoltoolsItem
from ..constants import XPATHS_LADDER, XPATHS_GAME


class OpggSpider(CrawlSpider):
    name = 'opgg'
    allowed_domains = ['op.gg']
    servers = ['br', 'jp', 'euw', 'oce', 'lan', 'tr', 'www', 'na', 'eune',
               'las', 'ru']
    start_urls = ['http://' +
                  server + '.op.gg/ranking/ladder/' for server in servers]

    def extract_champions(self, selector):
        for champion in selector:
            yield champion.xpath(XPATHS_GAME['champion_name']).extract_first()

    def parse_profile_links(self, selector):
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
        # import ipdb; ipdb.set_trace()
        matches = response.xpath(XPATHS_GAME['_matches'])
        for match in matches:
            match_type = match.xpath(XPATHS_GAME['_match_type']).extract_first().strip()
            result = response.xpath(XPATHS_GAME['result']).extract_first().strip()
            if match_type != 'Ranked Solo' or result == 'Remake':
                continue

            selector_t1 = match.xpath(XPATHS_GAME['champions_team_1'])
            selector_t2 = match.xpath(XPATHS_GAME['champions_team_2'])
            team_1 = list(self.extract_champions(selector_t1))
            team_2 = list(self.extract_champions(selector_t2))

            if not response.meta.get('related'):
                summoners_t1 = match.xpath(XPATHS_GAME['summoners_team_1'])
                summoners_t2 = match.xpath(XPATHS_GAME['summoners_team_2'])
                self.parse_profile_links(summoners_t1)
                self.parse_profile_links(summoners_t2)

            item = LoltoolsItem()
            result = response.xpath(
                XPATHS_GAME['result']).extract_first().strip()
            name = response.xpath(XPATHS_GAME['name']).extract_first()
            if name in summoners_t1.xpath('.//text()').extract():
                if result == 'Victory':
                    item['result'] = result
                else:
                    item['result'] = 'Defeat'
            else:
                if result == 'Victory':
                    item['result'] = 'Defeat'
                else:
                    item['result'] = result
            item['server'] = response.url.split('/')[2].split('.')[0]
            item['mmr'] = response.xpath(XPATHS_GAME['mmr']).extract_first()
            item['team_1'] = team_1
            item['team_2'] = team_2
            item['timestamp'] = match.xpath(XPATHS_GAME['timestamp']).extract_first()

            yield item
