"""
This module is the entry point of the application, defining the `Game` class,
which combines all elements to represent Scotland Yard games.
"""

import random
from board import Board
from player import Player
import board_data
import rules
import move


class Game:

    def __init__(self,board : Board, players : list[str]) -> None:
        self.board = board
        self.players = players

if __name__ == "__main__":
    main()

