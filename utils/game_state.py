"""Game state util."""


class GameState:
    """Game state."""

    def __init__(self, amount_players: int = 2) -> None:
        """Initialize the game state."""
        self.amount_players: int = amount_players
        self.active_players: list[int] = list(range(self.amount_players))
        self.current_player: int = 0

    def next(self) -> None:
        """Go to next player's turn."""
        self.current_player = (self.current_player + 1) % self.amount_players


STATE = GameState()
