from src.objects.metals import Metal
from src.objects.weapons import Weapon


class Forge:
    def __init__(self, metal: Metal, weapon: Weapon):
        self.name: str = str(f"{metal.name} {weapon.name}")
        self.difficulty: int = metal.difficulty * weapon.difficulty
        self.progress: int = 0
        
    def get_name(self):
        return self.name
