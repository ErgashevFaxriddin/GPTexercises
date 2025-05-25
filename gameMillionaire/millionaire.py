import tests.json_test as json_test
import users.json_users as json_users

class Millionaire:
    def __init__(self, name, played_games, score):
        self.name = name
        self.played_games = played_games
        self.score = score

    def start_game(self, name):
        self.name = input('ismingizni kiriting: ')
        users.append(name)
        