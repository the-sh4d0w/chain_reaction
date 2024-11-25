"""Option menu screen."""

import textual.app
import textual.containers
import textual.screen
import textual.widgets


class OptionMenuScreen(textual.screen.Screen):
    """Start menu screen."""

    def compose(self) -> textual.app.ComposeResult:
        """Compose the ui."""
        yield textual.widgets.Label("Options")
        yield textual.widgets.Button("Apply", id="apply_button")

    @textual.on(textual.widgets.Button.Pressed, "#apply_button")
    def apply_button_pressed(self, event: textual.widgets.Button.Pressed) -> None:
        """Handle on button pressed for #apply_button."""
        event.stop()
        self.app.pop_screen()
