"""Game screen."""

import textual.app
import textual.containers
import textual.screen
import textual.widgets

import utils.config
import widgets.tile


class PauseScreen(textual.screen.ModalScreen):
    """Pause modal screen."""
    BINDINGS = [
        ("escape", "pause", "Close pause screen.")
    ]

    def compose(self) -> textual.app.ComposeResult:
        """Compose the ui."""
        yield textual.widgets.Label("Pause Menu")
        yield textual.widgets.Button("Resume", id="resume_button")
        yield textual.widgets.Button("Option", id="option_button")
        # TODO: popup to confirm
        yield textual.widgets.Button("Back to Main Menu", id="close_button")

    def action_pause(self) -> None:
        """Handle pause action."""
        self.app.pop_screen()

    @textual.on(textual.widgets.Button.Pressed, "#resume_button")
    def resume_button_pressed(self, event: textual.widgets.Button.Pressed) -> None:
        """Handle on button pressed for #resume_button."""
        event.stop()
        self.app.pop_screen()

    @textual.on(textual.widgets.Button.Pressed, "#option_button")
    def option_button_pressed(self, event: textual.widgets.Button.Pressed) -> None:
        """Handle on button pressed for #option_button."""
        event.stop()
        self.app.push_screen("option_menu")

    @textual.on(textual.widgets.Button.Pressed, "#close_button")
    def close_button_pressed(self, event: textual.widgets.Button.Pressed) -> None:
        """Handle on button pressed for #close_button."""
        event.stop()
        self.app.pop_screen()
        self.app.switch_screen("start_menu")


class GameScreen(textual.screen.Screen):
    """Game screen."""
    BINDINGS = [
        ("escape", "pause", "Open pause screen.")
    ]

    def action_pause(self) -> None:
        """Handle pause action."""
        self.app.push_screen(PauseScreen())

    def compose(self) -> textual.app.ComposeResult:
        """Compose the ui."""
        with textual.containers.Grid(id="tile_grid"):
            for _ in range(utils.config.CONFIG.field_width
                           * utils.config.CONFIG.field_height):
                yield widgets.tile.Tile()
