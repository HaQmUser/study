from src.my_awesome_project.Classes.sorcerer import Sorcerer
from src.my_awesome_project.Classes.barbarian import Barbarian
import random


class Duel:
    def __init__(self):
        self.first_char = random.choice([Barbarian("Варвар1"), Sorcerer("Волшебник1")])
        self.second_char = random.choice([Barbarian("Варвар2"), Sorcerer("Волшебник2")])

    def describe_participants(self):
        return self.first_char.describe(), self.second_char.describe()

    def begin_duel(self):
        count = 1
        while self.first_char.is_alive() and self.second_char.is_alive():
            print(f"Начинается {count} ход")
            count += 1
            self.first_char.has_debuff()
            self.second_char.has_debuff()
            self.first_char.perform_action(self.second_char)
            self.second_char.perform_action(self.first_char)
        if self.first_char.is_alive():
            print(f"{self.first_char.charname} победил")
        else:
            print(f"{self.second_char.charname} победил")


x = Duel()
x.describe_participants()
x.begin_duel()
