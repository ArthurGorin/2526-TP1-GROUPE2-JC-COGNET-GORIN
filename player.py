"""
This module defines the different kinds of players.
"""

            
class Player:
    def __init__(self, name:str, position: int, tickets: dict[str, int]) -> None:
        self.name = name
        self.position = position
        self.tickets = tickets
        