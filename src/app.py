import pygame
from os import path

from pygame import display, event, time as pytime, Surface,font,mouse
from time import process_time
from src.menu import Menu
class Game: 

  def init_display(self,width,height,caption) -> Surface:
    display.set_mode((width,height))
    display.set_caption(caption)
    return display.get_surface()

  def __init__(self,config):
    pygame.init()
    self.surface = self.init_display(config.width, config.height, config.caption)
    self.game_state:int = 1
    self.config = config
    self.running = True
    if(path.isdir("src/save")):
      self.menu = Menu(config.width,config.height,True)
    else:
      self.menu = Menu(config.width,config.height,False)



  def run(self):
    """
    the run function starts the main loop for the applications
    """
    #before we run the game we need to setup some variables to handle the timing system]
    time_step:float = .0
    last_frame_Time:float = .0
    
    while self.running:
      time:float = process_time()
      time_step = time - last_frame_Time
      last_frame_Time = time
      #print(str(time_step))
      self.update()
      self.render()
      
      pytime.delay(1000//60)
    pygame.quit()

  def update(self):
    for e in event.get():
      if e.type == pygame.QUIT:
        self.running = False

    if self.game_state == 0 :
      self.running = False
    
    if self.game_state == 1:
      self.game_state = self.menu.update(mouse)
    
    if self.game_state == 2:
      pass

    if self.game_state == 3:
      pass

  def render(self):


    if self.game_state == 1:
      self.menu.render(self.surface)
      

    if self.game_state == 2:
      pass


    display.flip()
    display.update()
    pass