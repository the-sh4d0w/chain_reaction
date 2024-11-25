"""Tile widget."""

import textual.widgets


class Tile(textual.widgets.Button):
    """Tile widget."""

    def __init__(self) -> None:
        """Initialize the tile."""
        super().__init__(classes="tile")

    def render(self) -> str:
        """Render content."""
        return "*"
