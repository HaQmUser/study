from src.mechanics.spell import Spell
from src.mechanics.Debuffs.Freeze import freeze


class IceArrows(Spell):
    def __init__(self):
        super().__init__(spellname="Ледяные стрелы", spelldamage=8, debuffs=freeze)
