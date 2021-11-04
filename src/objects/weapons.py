

class Weapon:
    def __init__(self, name, difficulty):
        """

        :param name: the name of the weapon
        :param difficulty: this going to be how hard it is to forge the metal into the weapon shape
        """
        self.name: str = name
        self.difficulty: int = difficulty


dagger: Weapon = Weapon("dagger", 8)