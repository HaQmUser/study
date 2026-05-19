from src.my_awesome_project.mechanics.spell import Spell
from src.my_awesome_project.mechanics.Debuffs.Freeze import freeze


class IceArrows(Spell):
    def __init__(self):
        super().__init__(spellname="Ледяные стрелы", spelldamage=8, debuffs=freeze)
