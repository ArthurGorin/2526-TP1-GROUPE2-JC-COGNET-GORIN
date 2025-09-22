"""
This module defines the different kinds of moves, for the different kinds of
players.
"""

def move(board : Board, player : Player, station : StationNumber):
    if station not in board.stations:
        raise ValueError(f"Station {station} does not exist on the board.")
    if station == player.position:
        raise ValueError(f"Player {player.name} is already at station {station}.")
    # Check if there is a connection between the player's current position and the target station
    valid_connection = False
    mode_used = None
    for start, end, mode in board.connections:
        if (start == player.position and end == station) or (end == player.position and start == station):
            valid_connection = True
            mode_used = mode
            break
    if not valid_connection:
        raise ValueError(f"No connection between station {player.position} and station {station}.")
    # Move the player to the new station
    if player.tickets[mode_used]==0:
        raise ValueError(f"Player {player.name} does not have a ticket for mode {mode_used}.")
    player.tickets[mode_used] -= 1
    player.position = station



