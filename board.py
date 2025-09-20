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


class InvalidBoard:
    """
    The exception raised when board data is invalid.
    """

    # TODO
    pass


class Board:
    # TODO

    def __init__(
        self,
        stations: list[tuple[StationNumber, list[StationKind]]],
        connections: list[tuple[StationNumber, StationNumber, ConnectionMode]],
    ) -> None:
        # TODO
        pass
