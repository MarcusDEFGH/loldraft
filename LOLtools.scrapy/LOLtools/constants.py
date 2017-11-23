XPATHS_GAME = {
    'mmr': '//span[@class="tierRank"]/text()',
    'result': './/div[@class="GameResult"]/text()',
    '_match_type': './/div[@class="GameType"]/text()',
    '_matches': '//div[@class="GameItemWrap"]',
    'champions_team_1': './/div[@class="Team"][1]//div[@class="ChampionImage"]',
    'champions_team_2': './/div[@class="Team"][2]//div[@class="ChampionImage"]',
    'summoners_team_1': './/div[@class="Team"][1]//div[@class="SummonerName"]',
    'summoners_team_2': './/div[@class="Team"][2]//div[@class="SummonerName"]',
    'champion': './/div/text()',
    'timestamp': './/div[@class="TimeStamp"]//span/text()',
    'profile_link': './/a/@href',
    'name': '//div[@class="Information"]/span//text()'
}


XPATHS_LADDER = {
    '_summoners': '//td[@class="SummonerName Cell"]/a/@href'
}
