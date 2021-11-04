from pygame import draw, Rect, font, event
import pygame
from src.objects.metals import Metal


class ForgeOptionMenu:
    """
    Selection Menu: this creates and populates with menu options. \n
    for 1600, 900 \n
    x is 120 \n
    y is 170 \n
    width is 540 \n
    height is 630 \n
    """

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.menu_pos = 0
        self.font = font.SysFont("verdana", 36)
        self.options: list = []

    def render(self, surface):
        draw.rect(surface, (255, 255, 255), (self.x, self.y, self.width, self.height), 1)
        if len(self.options) >= (self.menu_pos + 5):
            limit: int = self.menu_pos + 5
        else:
            limit: int = len(self.options)
        temp_list: list = []
        for i in range(self.menu_pos, limit):
            self.options[i].render(
                surface,
                self.x,
                self.y + (self.height / 5) * i,
                self.width,
                self.height / 5,
                self.font
            )

    def update(self, mouse, forge_object):
        x, y = mouse.get_pos()
        left, middle, right = mouse.get_pressed(3)
        if not self.get_options():
            self.add_option(forge_object)
        if self.get_options():
            for obj in self.get_options():
                if obj.get_rect() is not None:
                    obj.set_colour()
                    if obj.get_x() <= x <= obj.get_x() + obj.get_width() \
                            and obj.get_y() <= y <= obj.get_y() + obj.get_height():
                        obj.set_colour((255, 255, 0))

        return None

    def add_option(self, option):
        self.options.append(
            ForgeOption(option)
        )

    def get_options(self):
        return self.options

    def set_menu_position(self, position):
        self.menu_pos = position

    def on_click(self, mouse):
        x, y = mouse.get_pos()
        left, middle, right = mouse.get_pressed(3)
        if self.get_options():
            for obj in self.get_options():
                if obj.get_rect() is not None:
                    if obj.get_x() <= x <= obj.get_x() + obj.get_width() \
                            and obj.get_y() <= y <= obj.get_y() + obj.get_height():
                        if left:
                            return obj.get_object()


class ForgeOption:

    def __init__(self, option, colour: tuple = (255, 255, 255)):
        self.object = option
        self.option_rect: Rect = None
        self.colour: tuple = colour

    def render(self, surface, x: int, y: int, width: int, height: int, option_font: font):
        self.option_rect = Rect((
            x,
            y,
            width,
            height
        ))
        draw.rect(surface, (67, 87, 96), self.option_rect)
        option_image = Rect(x, self.option_rect.y, self.option_rect.height, self.option_rect.height)
        draw.rect(surface, (42, 55, 61), option_image)  # Option Image

        start_pos = (option_image.x + option_image.width, self.option_rect.y + (self.option_rect.height / 2))
        end_pos = (x + (width * .99999), self.option_rect.y + (self.option_rect.height / 2))
        draw.line(surface, (255, 255, 255), start_pos, end_pos)

        surface.blit(
            option_font.render(self.object.name.title(), True, (255, 255, 255)),
            (
                option_image.x + option_image.width * 1.1,
                self.option_rect.y + self.option_rect.height * .0625
            )
        )

        draw.rect(surface, (255, 255, 255), option_image, 1)
        draw.rect(surface, self.colour, self.option_rect, 1)

    def set_colour(self, colour: tuple = (255, 255, 255)):
        self.colour = colour

    def get_x(self):
        return self.option_rect.x

    def get_y(self):
        return self.option_rect.y

    def get_width(self):
        return self.option_rect.width

    def get_height(self):
        return self.option_rect.height

    def get_rect(self):  #
        return self.option_rect

    def get_object(self):
        return self.object
