import json

_base_path = 'C:\\Users\\Marcus\\Desktop\\Projetos\\LOLtools\\db'

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
    if game['timestamp'] in str(stamps) or game['result'] == 'Remake':
        continue
    else:
        stamps.append(game['timestamp'])
        del game['timestamp']
        if game['result'] == 'Victory':
            game['result'] = 1
        else:
            game['result'] = 0
        f.write(str(game) + "\n")
        pre_processed.write(str(game) + "\n")

    pre_processed.close()
    f.close()
