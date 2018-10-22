XPATHS_GAME = {
    'mmr': '//span[@class="tierRank"]/text()',
    'result': './/div[@class="GameResult"]/text()',
    '_match_type': './/div[@class="GameType"]/text()',
    '_matches': '//div[@class="GameItemWrap"]',
    'champions_team_1': './/div[@class="Team"][1]//div[@class="ChampionImage"]',
    'champions_team_2': './/div[@class="Team"][2]//div[@class="ChampionImage"]',
    'summoners_team_1': './/div[@class="Team"][1]//div[@class="SummonerName"]',
    'summoners_team_2': './/div[@class="Team"][2]//div[@class="SummonerName"]',
    'champion_name': './/div/text()',
    'timestamp': './/div[@class="TimeStamp"]//span/text()',
    'profile_link': './/a/@href',
    'name': '//div[@class="Information"]/span//text()'
}

XPATH_CHAMPIONS = {
    'role': ('//div[contains(@class, "champion-'
             'index__champion-item ")]/@class'),
    'name': ('//div[contains(@class, "champion-index__champion-item__name")]'
             '//text()')
}

XPATHS_LADDER = {
    '_summoners': '//a[not(contains(@class, "ranking-highest'
                  '__name"))]//@href[contains(.,"user")]'
}


servers = ['br', 'jp', 'euw', 'oce', 'lan', 'tr', 'www', 'na', 'eune',
           'las', 'ru']
REGIONS = ['http://' + server + '.op.gg/ranking/ladder/' for server in servers]