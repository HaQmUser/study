from src.Classes.playerClass import Player
from src.guns.sorcGuns import sorcererGuns
import random
from src.mechanics.Spellbooks.SorcererSpellbook import sorcerer_spellbook


class Sorcerer(Player):
    def __init__(self, charname):
        super().__init__(
            charname=charname,
            role="Волшебник",
            hp=random.randint(70, 90),
            gun=random.choice(sorcererGuns),
            spell=random.choice(sorcerer_spellbook),
        )

    def describe(self):
        print(
            f"{self.charname}, роль {self.role}. Имеет {self.hp} хп, {self.gun.gunname} и заклинание {self.spells.get_name()} ."
        )
