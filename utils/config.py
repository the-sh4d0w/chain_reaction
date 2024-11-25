"""Config."""

import pathlib

import pydantic
import pydantic_core


class Config(pydantic.BaseModel):
    """Config representation."""
    language: str = pydantic.Field(default="en", pattern="^[a-z]{2}$")
    field_height: int = 6
    field_width: int = 10
    player1_colour: str = pydantic.Field(default="#FF0000",
                                         pattern="^#[0-9a-fA-F]{6}$")
    player2_colour: str = pydantic.Field(default="#00FF00",
                                         pattern="^#[0-9a-fA-F]{6}$")
    player3_colour: str = pydantic.Field(default="#0000FF",
                                         pattern="^#[0-9a-fA-F]{6}$")
    player4_colour: str = pydantic.Field(default="#FFFF00",
                                         pattern="^#[0-9a-fA-F]{6}$")
    player5_colour: str = pydantic.Field(default="#0000FF",
                                         pattern="^#[0-9a-fA-F]{6}$")
    player6_colour: str = pydantic.Field(default="#FF00FF",
                                         pattern="^#[0-9a-fA-F]{6}$")
    player7_colour: str = pydantic.Field(default="#FF8800",
                                         pattern="^#[0-9a-fA-F]{6}$")
    player8_colour: str = pydantic.Field(default="#FFFFFF",
                                         pattern="^#[0-9a-fA-F]{6}$")

    @classmethod
    def load(cls) -> "Config":
        """Load the config from file."""
        return Config.model_validate(pydantic_core.from_json(
            pathlib.Path("config.json").read_text(encoding="utf-8")))

    def store(self) -> None:
        """Store the config in a file."""
        pathlib.Path("config.json").write_text(self.model_dump_json(),
                                               encoding="utf-8")


CONFIG = Config.load()
