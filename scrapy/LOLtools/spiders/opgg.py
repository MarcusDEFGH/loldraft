# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.contrib.spiders import CrawlSpider
from ..items import LoltoolsItem
from ..constants import XPATH_CHAMPIONS, XPATHS_LADDER, XPATHS_GAME, REGIONS


class OpggSpider(CrawlSpider):
    name = 'opgg'
    allowed_domains = ['op.gg']
    start_urls = ['http://br.op.gg/champion/statistics']

    def fill_team(self, team, roles):
        formation = ['TOP', 'JUNGLE', 'MID', 'SUPPORT', 'ADC']
        ordered_team = ['TOP', 'JUNGLE', 'MID', 'SUPPORT', 'ADC']

        for index, item in enumerate(formation):
            for champion in team:
                champion_role = roles[champion - 1]
                if (item == champion_role) and (item in ordered_team):
                    ordered_team[index] = champion
                    team.remove(champion)
        while team:
            for index, slot in enumerate(ordered_team):
                if slot in formation:
                    ordered_team[index] = team[0]
                    del team[0]
        return ordered_team

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

    def parse_regions(self, response):
        summoners = response.xpath(XPATHS_LADDER['_summoners']).extract()
        for summoner in summoners:
            yield Request(url="http:"+summoner, callback=self.parse_games, meta=response.meta)

    def parse(self, response):
        meta = response.meta.copy()
        meta['info'] = {
            'champions': response.xpath(XPATH_CHAMPIONS['name']).extract(),
            'roles': [champion.split('--')[1].split()[0] for champion in
                      response.xpath(XPATH_CHAMPIONS['role']).extract()]
        }
        for region in REGIONS:
            yield Request(url=region, callback=self.parse_regions, meta=meta)

    def parse_games(self, response):
        champions = response.meta['info']['champions']
        roles = response.meta['info']['roles']
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
            team_1 = [champions.index(champion) for champion in team_1]
            team_2 = [champions.index(champion) for champion in team_2]
            item['team_1'] = self.fill_team(team_1, roles)
            item['team_2'] = self.fill_team(team_2, roles)
            item['timestamp'] = match.xpath(XPATHS_GAME['timestamp']).extract_first()

            yield item
