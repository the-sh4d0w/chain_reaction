"""Start menu screen."""

import textual.app
import textual.containers
import textual.screen
import textual.widgets


class StartMenuScreen(textual.screen.Screen):
    """Start menu screen."""

    def compose(self) -> textual.app.ComposeResult:
        """Compose the ui."""
        yield textual.widgets.Label("Chain Reaction")
        yield textual.widgets.Button("Start", id="start_button")
        yield textual.widgets.Button("Options", id="option_button")
        yield textual.widgets.Button("Quit", id="quit_button")

    @textual.on(textual.widgets.Button.Pressed, "#start_button")
    def start_button_pressed(self, event: textual.widgets.Button.Pressed) -> None:
        """Handle on button pressed for #start_button."""
        event.stop()
        self.app.switch_screen("game")

    @textual.on(textual.widgets.Button.Pressed, "#option_button")
    def option_button_pressed(self, event: textual.widgets.Button.Pressed) -> None:
        """Handle on button pressed for #option_button."""
        event.stop()
        self.app.push_screen("option_menu")

    @textual.on(textual.widgets.Button.Pressed, "#quit_button")
    def quit_button_pressed(self, event: textual.widgets.Button.Pressed) -> None:
        """Handle on button pressed for #quit_button."""
        event.stop()
        self.app.exit()
