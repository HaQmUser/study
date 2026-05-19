from src.my_awesome_project.mechanics.debuff import Debuff


class Freeze(Debuff):
    def __init__(self):
        super().__init__(debuffname="Обморожение", duration=4, debuff_effect_damage=2)


freeze = Freeze()
