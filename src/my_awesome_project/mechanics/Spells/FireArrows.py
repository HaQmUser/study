from src.my_awesome_project.mechanics.spell import Spell
from src.my_awesome_project.mechanics.Debuffs.Burn import burn


class FireArrows(Spell):
    def __init__(self):
        super().__init__(spellname="Огненные стрелы", spelldamage=15, debuffs=burn)
