"""Main code for chain reaction."""

import pathlib

import click
import textual.app
import textual.containers
import textual.theme
import textual.widget

import screens.game
import screens.option
import screens.start_menu
import utils.config


class ChainReactionApp(textual.app.App):
    """Chain Reaction app."""
    ENABLE_COMMAND_PALETTE = False
    CSS_PATH = list(pathlib.Path("styles").iterdir())

    def __init__(self, debug: bool = False) -> None:
        """Initialize chain reaction."""
        super().__init__()
        self._debug: bool = debug

    def on_mount(self) -> None:
        """Do stuff on mount."""
        for i in range(8):
            self.register_theme(textual.theme.Theme(name=f"player{i}",
                                primary=utils.config.CONFIG.colours[i]))
        self.theme = "player0"
        self.install_screen(screens.start_menu.StartMenuScreen(), "start_menu")
        self.install_screen(screens.game.GameScreen(), "game")
        self.install_screen(screens.option.OptionMenuScreen(), "option_menu")
        self.push_screen("start_menu")


@click.command()
@click.option("-d", "--debug", is_flag=True, help="Add debug options.")
def main(debug: bool = False) -> None:
    """Chain Reaction game."""
    ChainReactionApp(debug=debug).run()


if __name__ == "__main__":
    main()
