import random

class Player:
    def __init__(self, nickname: str):
        self.nickname = nickname
        self.balance = 100
        self.spins = 0
        self.max_balance = 100

    def spin(self):
        cost = 10
        if self.balance < cost:
            return None
        self.balance -= cost
        result = random.randint(1, 20)
        self.balance += result
        self.spins += 1
        if self.balance > self.max_balance:
            self.max_balance = self.balance
        return result


class Game:
    def __init__(self):
        self.players = {}

    def add_player(self, nickname: str):
        player = Player(nickname)
        self.players[nickname] = player
        return player

    def get_player(self, nickname: str):
        return self.players.get(nickname)
