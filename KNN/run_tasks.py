import ast
from KNN.tasks import compare, predict, write_accuracy

# import ipdb; ipdb.set_trace()

db = 'KNN/db.json'
a = {'result': 0, 'team_1': [131, 42, 67, 128,
                             101], 'team_2': [44, 96, 136, 115, 70]}


def main(size, krange, database):
    accuracy = open('celery.txt', 'a')
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
            predictions.append(predict.delay(game, test_set, index, results))
        import ipdb; ipdb.set_trace()
        write_accuracy.delay(str(compare(results, predictions) / size) + '\n')


main(1000, 1, db)
