import enum

"""
This module contains the classes used to represent a board.
"""
# Type synonym, used for better readability
StationNumber = int


class StationKind(enum.Enum):
    """
    The possible station kinds (used for display, and thus excluding ferries).
    """

    BUS = "bus"
    TAXI = "taxi"
    UNDERGROUND = "underground"


class ConnectionMode(enum.Enum):
    """
    The possible transportation modes, for connections between stations.
    """

    BUS = "bus"
    TAXI = "taxi"
    UNDERGROUND = "underground"
    FERRY = "ferry"


class InvalidBoard(Exception):
    pass


class Board:
    def __init__(
        self,
        stations: list[tuple[StationNumber, list[StationKind]]],
        connections: list[tuple[StationNumber, StationNumber, ConnectionMode]],
    ) -> None:
        # Store stations in a dict and connections in a list
        self.stations = {num: kinds for num, kinds in stations}
        self.connections = connections

        # Check that all connections refer to existing stations
        for start, end, mode in connections:
            if start not in self.stations or end not in self.stations or start == end:
                raise InvalidBoard(f"Invalid connection: {start} <-> {end} (mode: {mode})")
            # Check that the connection mode is valid for the station (except FERRY)
            if mode != ConnectionMode.FERRY and (mode not in self.stations[start] or mode not in self.stations[end]):
                raise InvalidBoard(f"Connection mode {mode} not available at station {start}")
    

