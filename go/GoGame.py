from Game import Game
from dlgo.goboard_fast import Board, GameState, Move, Point
from dlgo.encoders.oneplane import OnePlaneEncoder

class GoGame(Game):
    def __init__(self, n):
        self.n = n

    def getInitBoard(self):
        new_game = GameState.new_game(self.n)
        return OnePlaneEncoder((self.n, self.n)).encode(new_game)

    def getBoardSize(self):
        return (self.n, self.n)

    def getActionSize(self):
        return self.n * self.n + 1

    def getNextState(self, board, player, action):
        
