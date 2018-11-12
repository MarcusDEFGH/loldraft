XPATHS_GAME = {
    'mmr': '//span[@class="tierRank"]/text()',
    'result': './/div[@class="GameResult"]/text()',
    '_match_type': './/div[@class="GameType"]/text()',
    '_matches': '//div[@class="GameItemWrap"]',
    '_champions_team_1': './/div[@class="Team"][1]//div[@class="ChampionImage"]',
    '_champions_team_2': './/div[@class="Team"][2]//div[@class="ChampionImage"]',
    '_summoners_team_1': './/div[@class="Team"][1]//div[@class="SummonerName"]',
    '_summoners_team_2': './/div[@class="Team"][2]//div[@class="SummonerName"]',
    '_champion_name': './/div/text()',
    'timestamp': './/div[@class="TimeStamp"]//span/text()',
    'profile_link': './/a/@href',
    'player': '//div[@class="Information"]/span//text()'
}

XPATH_CHAMPIONS = {
    'role': ('//div[contains(@class, "champion-'
             'index__champion-item ")]/@class'),
    'name': ('//div[contains(@class, "champion-index__champion-item__name")]'
             '//text()')
}

XPATHS_LADDER = {
    '_summoners': '//a[not(contains(@class, "ranking-highest'
                  '__name"))]//@href[contains(.,"userName")]'
}


servers = ['br', 'jp', 'euw', 'oce', 'lan', 'tr', 'www', 'na', 'eune',
           'las', 'ru']
REGIONS = ['http://' + server + '.op.gg/ranking/ladder/' for server in servers]
