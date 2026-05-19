from src.Classes.playerClass import Player
from src.guns.barbGuns import barbarianGuns
import random


class Barbarian(Player):
    def __init__(self, charname):
        super().__init__(
            charname=charname,
            role="Варвар",
            hp=random.randint(90, 110),
            gun=random.choice(barbarianGuns),
            spell=None,
        )

    def describe(self):
        print(
            f"{self.charname}, роль {self.role}. Имеет {self.hp} хп, {self.gun.gunname} и не имеет заклинаний."
        )
