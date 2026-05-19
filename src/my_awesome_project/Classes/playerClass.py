from abc import ABC
import random


class Player(ABC):
    def __init__(self, charname, role, hp, gun, spell):
        self.charname = charname
        self.role = role
        self.hp = hp
        self.gun = gun
        self.spells = spell
        self.active_debuffs = []

    def describe(self):
        pass

    def is_alive(self):
        if self.hp > 0:
            return True
        else:
            return False

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
        print(f"{self.charname} получает {damage} урона. У него осталось {self.hp} хп")

    def attack(self, target):
        print(f"{self.charname} атакует {target.charname} с помощью {self.gun.gunname}")
        target.take_damage(self.gun.damage)

    def apply_spell(self, target):
        if self.spells is None:
            print(f"{self.charname} безуспешно пытается применить заклинание")
        else:
            print(
                f"{self.charname} применяет заклинание {self.spells.get_name()} на {target.charname}"
            )
            self.spells.be_used(target)

    def has_debuff(self):
        if len(self.active_debuffs) > 0:
            for active_debuff in self.active_debuffs:
                active_debuff.perform_debuff_effect(self)
            return True

        else:
            return False

    def perform_action(self, target):

        if self.role == "Волшебник":
            actions = [self.apply_spell, self.attack]
            weights = [0.8, 0.2]

            chosen_action = random.choices(actions, weights=weights, k=1)[0]
            chosen_action(target)
        elif self.role == "Варвар":
            self.attack(target)
