from knn.tasks import predict
from match_reader.pattern-match import identify_champions
import pyscreenshot as ImageGrab


def main():
    im = ImageGrab.grab()
    im.save('match.png')
    game = identify_champions('match.png')
    db = 'scrapy/db.json'
    db_file = open(database, 'r')
    games = db_file.readlines()
    db_file.close()
    if predict(str(game), games):
        return "Arrocha papai!"
    else:
        return "Quita men"

main()
