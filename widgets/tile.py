"""Tile widget."""

import textual.widgets

import utils.config
import utils.game_state


class Tile(textual.widgets.Button):
    """Tile widget."""
    TILES: list[list["Tile"]] = [[] for _ in range(
        utils.config.CONFIG.field_height)]

    def __init__(self, count: int) -> None:
        """Initialize the tile."""
        super().__init__(classes="tile")
        self.atoms: int = 0
        self.owner: int = -1
        self.x = count % utils.config.CONFIG.field_width
        self.y = count // utils.config.CONFIG.field_width
        self.TILES[self.y].append(self)

    def left(self) -> "Tile | None":
        """Get left neighbour.

        Returns:
            Left neighbour if it exists, None otherwise.
        """
        return self.TILES[self.y][self.x - 1] if self.x != 0 else None

    def right(self) -> "Tile | None":
        """Get right neighbour.

        Returns:
            Right neighbour if it exists, None otherwise.
        """
        return self.TILES[self.y][self.x + 1] \
            if self.x != utils.config.CONFIG.field_width - 1 else None

    def top(self) -> "Tile | None":
        """Get top neighbour.

        Returns:
            Top neighbour if it exists, None otherwise.
        """
        return self.TILES[self.y - 1][self.x] if self.y != 0 else None

    def bottom(self) -> "Tile | None":
        """Get bottom neighbour.

        Returns:
            Bottom neighbour if it exists, None otherwise.
        """
        return self.TILES[self.y + 1][self.x] \
            if self.y != utils.config.CONFIG.field_height - 1 else None

    def limit(self) -> int:
        """Get limit (amount of neighbours).

        Returns:
            The amount of neighbours.
        """
        return bool(self.left()) + bool(self.right()) + bool(self.top()) + bool(self.bottom())

    def add(self, owner: int) -> None:
        """Add one atom."""
        self.atoms += 1
        self.owner = owner
        if self.atoms == self.limit():
            self.atoms = 0
            self.owner = -1
            if self.left() is not None:
                self.left().add(owner)  # type: ignore
            if self.right() is not None:
                self.right().add(owner)  # type: ignore
            if self.top() is not None:
                self.top().add(owner)  # type: ignore
            if self.bottom() is not None:
                self.bottom().add(owner)  # type: ignore
        self.refresh()

    def render(self) -> str:
        """Render content."""
        return f"[{utils.config.CONFIG.colours[self.owner]}]{self.atoms}[/]" \
            if self.atoms != 0 else ""

    def on_button_pressed(self, event: textual.widgets.Button.Pressed) -> None:
        """Handle on button pressed."""
        event.stop()
        if self.owner in (-1, utils.game_state.STATE.current_player):
            self.add(utils.game_state.STATE.current_player)
            utils.game_state.STATE.next()
            self.app.theme = f"player{utils.game_state.STATE.current_player}"
