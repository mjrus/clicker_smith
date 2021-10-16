import pygame
from pygame import draw,rect,font
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface
class Menu: 

  def __init__(self,width,height, has_save):
    self.width = width
    self.height = height
    x:int = self.width*0.40625
    y:int = self.height*.5
    self.options = [
      Menu_Options(x,y+75,300, 50,"New Game"),
      Menu_Options(x,y+150,300, 50,"Settings"),
      Menu_Options(x,y+225,300, 50,"Exit")
    ]
    if has_save:
      self.options.append(Menu_Options(x, y, 300, 50, "Continue"))

  def render(self,surface):
    surface.fill((42,55,61))
    menu_tile = font.SysFont("verdana", 64)
    menu_background = draw.rect(surface, (67,87,96), Rect(round(self.width*0.3125),0,self.width*0.375,self.height))
    clicker = menu_tile.render("Clicker", True, (255,255,255))
    smith = menu_tile.render("Smith", True, (255,255,255))
    surface.blit(clicker, (menu_background.x+((menu_background.width/2)-clicker.get_width()/2),self.height*0.05))
    surface.blit(smith, (menu_background.x+((menu_background.width/2)-smith.get_width()/2),self.height*0.05+clicker.get_height()))
    
    for option in self.options:
        option.render(surface)

  def update(self,mouse)->int:
    x,y = mouse.get_pos()
    left,middle,right = mouse.get_pressed(3)

    for option in self.options:
      
      if((x >= option.x and not x >= (option.x +option.width))
        and
        (y >= option.y and not y >= (option.y +option.height))):
        option.set_colour((249,217,114),(0,0,0))
        if(left):
          return option.on_click()
      else:
        option.set_colour((42,55,61),(255,255,255))
    return 1  


class Menu_Options:

  def __init__(self,x,y,width,height,name):
    self.x = x
    self.y = y  
    self.name = name
    self.width = width
    self.height = height
    self.font = font.SysFont("verdana", 36)
    self.background_colour = (42,55,61)
    self.text_colour = (255,255,255)

  def set_colour(self,background, text):
    self.background_colour = background
    self.text_colour = text

  def render(self,surface):
    title = self.font.render(self.name, True, self.text_colour)
    button_background = draw.rect(surface, self.background_colour, Rect(self.x, self.y, self.width, self.height))
    surface.blit(title,(button_background.x+(button_background.width - title.get_width())/2,button_background.y+(button_background.height - title.get_height())/2))

  def on_click(self)->int:
    if(self.name == "New Game"):
      return 2
    if(self.name == "Settings"):
      return 3
    if(self.name == "Exit"):
      return 0
