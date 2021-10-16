from dataclasses import dataclass
from pygame.font import Font

@dataclass
class Config:
  #screen
  width:int
  height:int
  caption:str = "Clicker Smith"
  frame_rate_cap:int = 60
  
