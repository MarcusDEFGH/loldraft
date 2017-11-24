import ast
from numpy import average

def compare(team_1, team_2):
    return len([i for i, j in zip(team_1, team_2) if i == j])
    #return len(set(team_1) & set(team_2))


def get_distance(game_q, game_t):
    team_1 = compare(game_q['team_1'], game_t['team_1'])
    team_2 = compare(game_q['team_2'], game_t['team_2'])
    normalized = ((team_1 + team_2)/10)**2
    distance = 1 - normalized
    return (distance, game_q['result'])

#import ipdb; ipdb.set_trace()
db = 'C:\\Users\\Marcus\\Desktop\\Projetos\\LOLtools\\utils\\db.json'
a = {'result': 0, 'team_1': [131, 42, 67, 128, 101], 'team_2': [44, 96, 136, 115, 70]}

def get_key(item):
    return item[0]


def get_result(item):
    return item[1]

def knn(game_q, db, k):
    distances = []
    for game in db:
        distancef = get_distance(ast.literal_eval(game), game_q)
        distances.append(distancef)
    k_nearest_neighbors = sorted(distances, key=get_key)[:k]
    win_prob = average([get_result(x) for x in k_nearest_neighbors])
    if win_prob > 0.5:
        return 1
    else:
        return 0


def main(database):
    db_file = open(database, 'r')
    games = db_file.readlines()
    db_file.close()
    train_set = games[:1000]
    teste_set = games[1000:]
    results = []
    predictions = []
    for game in train_set:
        results.append(ast.literal_eval(game)['result'])
        index = train_set.index(game) + 1
        print(str(index) + ' - ' + str(compare(results, predictions)/index))
        predictions.append(knn(ast.literal_eval(game), teste_set, 3))
    print(compare(results, predictions)/1000)

main(db)
