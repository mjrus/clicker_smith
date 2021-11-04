import pygame
from os import path

from pygame import display, event, time as pytime, Surface, font, mouse
from time import process_time
from src.menu import Menu
from src.game import Game


class App:

    def init_display(self, width, height, caption) -> Surface:
        display.set_mode((width, height))
        display.set_caption(caption)
        return display.get_surface()

    def __init__(self, config):
        pygame.init()
        self.surface = self.init_display(config.width, config.height, config.caption)
        self.game_state: int = 2
        self.config = config
        self.running = True
        if path.isdir("src/save"):
            self.menu = Menu(config.width, config.height, True)
            self.game = Game(config.width, config.height)
        else:
            self.menu = Menu(config.width, config.height, False)
            self.game = Game(config.width, config.height)

    def run(self):
        """
    the run function starts the main loop for the applications
    """
        # before we run the game we need to setup some variables to handle the timing system]
        time_step: float = .0
        last_frame_time: float = .0

        while self.running:
            time: float = process_time()
            time_step = time - last_frame_time
            last_frame_time = time

            self.update()
            self.render()

            pytime.delay(1000 // 60)
        pygame.quit()

    def update(self):
        for e in event.get():
            if e.type == pygame.QUIT:
                self.game_state = 0
            if e.type == pygame.MOUSEBUTTONDOWN:
                self.game.on_click(mouse)
        if self.game_state == 0:
            self.running = False
            return

        if self.game_state == 1:
            self.game_state = self.menu.update(mouse)

        if self.game_state == 2:
            self.game_state = self.game.update(mouse)

        if self.game_state == 3:
            pass

    def render(self):

        if self.game_state == 1:
            self.menu.render(self.surface)

        if self.game_state == 2:
            self.game.render(self.surface)

        display.flip()
        display.update()
        pass
