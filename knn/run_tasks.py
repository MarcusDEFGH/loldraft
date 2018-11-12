from knn.tasks import train


db = 'knn/db.json'
a = {'result': 0, 'team_1': [131, 42, 67, 128, 101],
                  'team_2': [44, 96, 136, 115, 70]}


def main(size, krange, database):
    db_file = open(database, 'r')
    games = db_file.readlines()
    db_file.close()
    train_set = []
    test_set = []
    for i in range(krange):
        train.delay(size, i, games)


main(1000, 5, db)

 
