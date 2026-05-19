from src.my_awesome_project.mechanics.debuff import Debuff


class Burn(Debuff):
    def __init__(self):
        super().__init__(debuffname="Горение", duration=2, debuff_effect_damage=5)


burn = Burn()
