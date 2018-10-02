import json

_base_path = 'C:\\Users\\Marcus\\Desktop\\Projetos\\LOLtools\\db'


champions = ['Aatrox', 'Ahri', 'Akali', 'Alistar', 'Amumu', 'Anivia', 'Annie',
             'Ashe', 'Aurelion Sol', 'Azir', 'Bard', 'Blitzcrank', 'Brand',
             'Braum', 'Caitlyn', 'Camille', 'Cassiopeia', "Cho'Gath", 'Corki',
             'Darius', 'Diana', 'Dr. Mundo', 'Draven', 'Ekko', 'Elise',
             'Evelynn', 'Ezreal', 'Fiddlesticks', 'Fiora', 'Fizz', 'Galio',
             'Gangplank', 'Garen', 'Gnar', 'Gragas', 'Graves', 'Hecarim',
             'Heimerdinger', 'Illaoi', 'Irelia', 'Ivern', 'Janna', 'Jarvan IV',
             'Jax', 'Jayce', 'Jhin', 'Jinx', "Kai'Sa", 'Kalista', 'Karma',
             'Karthus', 'Kassadin', 'Katarina', 'Kayle', 'Kayn', 'Kennen',
             "Kha'Zix", 'Kindred', 'Kled', "Kog'Maw", 'LeBlanc', 'Lee Sin',
             'Leona', 'Lissandra', 'Lucian', 'Lulu', 'Lux', 'Malphite',
             'Malzahar', 'Maokai', 'Master Yi', 'Miss Fortune', 'Mordekaiser',
             'Morgana', 'Nami', 'Nasus', 'Nautilus', 'Nidalee', 'Nocturne',
             'Nunu & Willump', 'Olaf', 'Orianna', 'Ornn', 'Pantheon', 'Poppy',
             'Pyke', 'Quinn', 'Rakan', 'Rammus', "Rek'Sai", 'Renekton',
             'Rengar', 'Riven', 'Rumble', 'Ryze', 'Sejuani', 'Shaco', 'Shen',
             'Shyvana', 'Singed', 'Sion', 'Sivir', 'Skarner', 'Sona', 'Soraka',
             'Swain', 'Syndra', 'Tahm Kench', 'Taliyah', 'Talon', 'Taric',
             'Teemo', 'Thresh', 'Tristana', 'Trundle', 'Tryndamere ',
             'Twisted Fate', 'Twitch', 'Udyr', 'Urgot', 'Varus', 'Vayne',
             'Veigar', "Vel'Koz", 'Vi', 'Viktor', 'Vladimir', 'Volibear',
             'Warwick', 'Wukong', 'Xayah', 'Xerath', 'Xin Zhao', 'Yasuo',
             'Yorick', 'Zac', 'Zed', 'Ziggs', 'Zilean', 'Zoe', 'Zyra']

servers = ['br', 'jp', 'euw', 'oce', 'lan',
           'tr', 'www', 'na', 'eune', 'las', 'ru']

paths = ['\\'.join([_base_path, server]) for server in servers]



def path_join(server, mmr, filetype):
    return _base_path + '\\' + server + '\\' + mmr + '.' + filetype

games = json.load(open(_base_path + '\\' + 'opgg.json'))
stamps = []
for game in games:
    print(games.index(game))
    server = game['server']
    mmr = game['mmr']
    del game['mmr'], game['server']
    f = open(path_join(server, mmr, 'json'), 'a+')
    pre_processed = open('db.json', 'a+')
    if game['timestamp'] in str(stamps) or game['result'] =='Remake':
        continue
    else:
        stamps.append(game['timestamp'])
        del game['timestamp']
        for champion in game['team_1']:
            game['team_1'][game['team_1'].index(
                champion)] = champions.index(champion)
        for champion in game['team_2']:
            game['team_2'][game['team_2'].index(
                champion)] = champions.index(champion)
        if game['result'] == 'Victory':
            game['result'] = 1
        else:
            game['result'] = 0
        f.write(str(game) + "\n")
        pre_processed.write(str(game) + "\n")

    pre_processed.close()
    f.close()
