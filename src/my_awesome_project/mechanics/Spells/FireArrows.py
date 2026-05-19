from src.mechanics.spell import Spell
from src.mechanics.Debuffs.Burn import burn


class FireArrows(Spell):
    def __init__(self):
        super().__init__(spellname="Огненные стрелы", spelldamage=15, debuffs=burn)
