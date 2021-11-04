from pygame import Surface, draw, Rect
from pygame.font import Font


class Metal:
    def __init__(self, name: str, difficulty: int, cost: int):
        """

        :param name: the name of the metal
        :param difficulty: this going to be how hard the metal is to forge
        """
        self.name: str = name
        self.difficulty: int = difficulty
        self.cost: int = cost
        self.base_price: int = round(cost * 0.834)
        print(self.base_price)


copper: Metal = Metal("copper", 8, 60)
iron: Metal = Metal("iron", 16, 90)
