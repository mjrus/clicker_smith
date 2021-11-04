from src.app import App
from src.systems.config import Config
from pathlib import Path
from pygame import font


def load() -> Config:
    pass


def main():
    config_file = Path("src/systems/game.config")
    if config_file.is_file():
        config = load()
    else:
        config = Config(1600, 900)
    App(config).run()


if __name__ == "__main__":
    main()
