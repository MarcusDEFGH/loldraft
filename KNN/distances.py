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


def main(size, krange, database):
    accuracy = open('accuracy.txt', 'a')
    db_file = open(database, 'r')
    games = db_file.readlines()
    db_file.close()
    train_set = []
    test_set = []
    for i in range(krange):
        if size * i == 0:
            size_i = 1
        else:
            size_i = size * i
        train_set = games[size + (size * i):][:size]
        test_set = games[:size + (size * i)] + \
            games[size + (size * (i + 1)):]
        results = []
        predictions = []
        for game in train_set:
            results.append(ast.literal_eval(game)['result'])
            index = train_set.index(game) + 1
            predictions.append(knn(ast.literal_eval(game), test_set, 3))
            accuracy.write((str(index) + ' - ' + str(compare(results, predictions)/index)) + '\n')
        accuracy.write(str(compare(results, predictions) / size) + '\n')



# def kfold(size, krange, db):
#     train_set = []
#     test_set = []
#     games = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
#     for i in range(krange):
#         import ipdb; ipdb.set_trace()
#         if size*i == 0:
#             size_i = 1
#         else:
#             size_i = size*i
#         train_set = games[size + (size * i):][:size]
#         test_set = games[:size + (size * i)] + \
#             games[size + (size * (i + 1)):]
#         print(train_set)
#         print(test_set)


main(1000, 16, db)
