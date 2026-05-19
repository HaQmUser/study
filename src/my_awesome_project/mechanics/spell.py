class Spell:
    def __init__(self, spellname, spelldamage, debuffs):
        self.spellname = spellname
        self.spelldamage = spelldamage
        self.debuff = debuffs

    def get_name(self):
        return self.spellname

    def be_used(self, target):
        target.take_damage(self.spelldamage)
        print(
            f"{self.spellname} наклалдывает на {target.charname} {self.debuff.debuffname}"
        )
        self.debuff.apply_debuff(target)
