from pygame import draw, Rect, font
from src.objects.metals import copper, Metal
from src.objects.player import Player
from src.objects.weapons import dagger, Weapon
from src.objects.forge import Forge
from src.game_menus.forge import ForgeOptionMenu, ForgeOption
import os


class Game:

    def __init__(self, width: int, height: int):

        self.screen = (width, height)
        self.forging: bool = False  # this bool is to see if there is an item currently being forged

        self.metal: Metal = None
        self.weapon: Weapon = None

        self.metal_menu: ForgeOptionMenu = None
        self.weapon_menu: ForgeOptionMenu = None

        self.current_forge = None

        self.font_verdana18 = font.SysFont("verdana", 18)
        self.font_verdana32 = font.SysFont("verdana", 32)

        self.player: Player = Player()

    def render(self, surface):
        surface.fill((0, 0, 0))

        if not self.forging:
            """
            Selection Rect: the background for the material/weapon selection list
            for 1600, 900 
            x is 100 
            y is 90 
            width is 600
            height is 720
            """
            selection_rect = Rect(
                (
                    self.screen[0] * .0625,
                    self.screen[1] * .1,
                    self.screen[0] * .375,
                    self.screen[1] * .8
                )
            )
            draw.rect(surface, (42, 55, 61), selection_rect)

            if self.metal is None:
                if self.metal_menu is None:
                    self.metal_menu = ForgeOptionMenu(
                        selection_rect.x + selection_rect.width * .03334,
                        selection_rect.y + selection_rect.height * .11111,
                        selection_rect.width * .9,
                        selection_rect.height * .875
                    )

                select = self.font_verdana18.render("Select a metal to forge", True, (255, 255, 255))

                surface.blit(
                    select,
                    (
                        selection_rect.x + (selection_rect.width / 2 - select.get_width() / 2),
                        selection_rect.y + selection_rect.height * .05
                    )
                )
                if self.metal_menu.get_options():
                    self.metal_menu.render(surface)

            if self.weapon is None and self.metal is not None:
                if self.weapon_menu is None:
                    self.weapon_menu = ForgeOptionMenu(
                        selection_rect.x + selection_rect.width * .03334,
                        selection_rect.y + selection_rect.height * .11111,
                        selection_rect.width * .9,
                        selection_rect.height * .875
                    )
                select = self.font_verdana18.render("Select a weapon to forge", True, (255, 255, 255))

                surface.blit(
                    select,
                    (
                        selection_rect.x + (selection_rect.width / 2 - select.get_width() / 2),
                        selection_rect.y + selection_rect.height * .05
                    )
                )
                if self.weapon_menu.get_options():
                    self.weapon_menu.render(surface)

        if self.forging:

            forging = self.font_verdana32.render(
                self.current_forge.get_name().title(),
                True,
                (255, 255, 255)
            )

            surface.blit(
                forging,
                (
                    self.screen[0] * .15,
                    self.screen[1] * .05
                )
            )

    def update(self, mouse) -> int:
        x, y = mouse.get_pos()
        left, middle, right = mouse.get_pressed(3)

        if not self.forging:
            if self.metal is None:
                if self.metal_menu is not None:
                    self.metal_menu.update(mouse, copper)
            if self.weapon is None and self.metal is not None:
                if self.weapon_menu is not None:
                    self.weapon_menu.update(mouse, dagger)
            if self.metal is not None and self.weapon is not None:
                self.forging = True
                self.current_forge = Forge(self.metal, self.weapon)
        return 2

    def on_click(self, mouse):
        if not self.forging:

            if self.metal is None:
                if self.metal_menu is not None:
                    self.metal = self.metal_menu.on_click(mouse)
            if self.weapon is None and self.metal is not None:
                if self.weapon_menu is not None:
                    self.weapon = self.weapon_menu.on_click(mouse)
