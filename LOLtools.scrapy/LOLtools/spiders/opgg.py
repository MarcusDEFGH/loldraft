# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.contrib.spiders import CrawlSpider
from ..items import LoltoolsItem
from ..constants import XPATHS_LADDER, XPATHS_GAME


class OpggSpider(CrawlSpider):
    name = 'opgg'
    allowed_domains = ['op.gg']
    servers = ['br', 'jp', 'euw', 'oce', 'lan', 'tr', 'www', 'na', 'eune', 'las', 'ru']
    start_urls = ['http://' + x + '.op.gg/ranking/ladder/' for x in servers]

    def parse(self, response):

        summoners = response.xpath(XPATHS_LADDER['_summoners']).extract()
        for summoner in summoners:

            yield Request(url="http:"+summoner, callback=self.parse_games)



    def parse_games(self, response):

        matches = response.xpath(XPATHS_GAME['_matches'])
        for match in matches:
            match_type = match.xpath(XPATHS_GAME['_match_type']).extract_first().strip()
            result = response.xpath(XPATHS_GAME['result']).extract_first().strip()
            if match_type != 'Ranked Solo' or result == 'Remake':
                continue
            team_1 = []
            team_2 = []
            ##TODO fix this god awful code
            champions_team_1 = match.xpath(XPATHS_GAME['champions_team_1'])
            champions_team_2 = match.xpath(XPATHS_GAME['champions_team_2'])
            for champion in champions_team_1:
                champ = champion.xpath(XPATHS_GAME['champion']).extract_first()
                team_1.append(champ)
            for champion in champions_team_2:
                champ = champion.xpath(XPATHS_GAME['champion']).extract_first()
                team_2.append(champ)

            summoners_team_1 = match.xpath(XPATHS_GAME['summoners_team_1'])
            summoners_team_2 = match.xpath(XPATHS_GAME['summoners_team_2'])

            for summoner in summoners_team_1:
                link = summoner.xpath(XPATHS_GAME['profile_link']).extract_first()
                yield Request(url="http:" + link, callback=self.parse_related_games)
            for summoner in summoners_team_2:
                link = summoner.xpath(XPATHS_GAME['profile_link']).extract_first()
                yield Request(url="http:" + link, callback=self.parse_related_games)

            item = LoltoolsItem()
            result = response.xpath(
                XPATHS_GAME['result']).extract_first().strip()
            name = response.xpath(XPATHS_GAME['name']).extract_first()
           # import ipdb; ipdb.set_trace()
            if name in summoners_team_1.xpath('.//text()').extract():
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

    def parse_related_games(self, response):
        """In a hurry so copy-pasting shit code like this one"""

        matches = response.xpath(XPATHS_GAME['_matches'])
        for match in matches:
            match_type = match.xpath(XPATHS_GAME['_match_type']).extract_first().strip()
            if match_type != 'Ranked Solo':
                continue
            team_1 = []
            team_2 = []
            result = response.xpath(XPATHS_GAME['result']).extract_first().strip()
            ## that looks so bad
            champions_team_1 = match.xpath(XPATHS_GAME['champions_team_1'])
            champions_team_2 = match.xpath(XPATHS_GAME['champions_team_2'])
            for champion in champions_team_1:
                champ = champion.xpath(XPATHS_GAME['champion']).extract_first()
                team_1.append(champ)
            for champion in champions_team_2:
                champ = champion.xpath(XPATHS_GAME['champion']).extract_first()
                team_2.append(champ)

            summoners_team_1 = match.xpath(XPATHS_GAME['summoners_team_1'])
            item = LoltoolsItem()
            result = response.xpath(
                XPATHS_GAME['result']).extract_first().strip()
            name = response.xpath(XPATHS_GAME['name']).extract_first()
           # import ipdb; ipdb.set_trace()
            if name in summoners_team_1.xpath('.//text()').extract():
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
