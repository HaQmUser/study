class Debuff:
    def __init__(self, debuffname, duration, debuff_effect_damage):
        self.debuffname = debuffname
        self.duration = duration
        self.debuff_effect_damage = debuff_effect_damage

    def apply_debuff(self, target):
        target.active_debuffs.append(self)

    def remove_debuff(self, target):
        target.active_debuffs.remove(self)

    def perform_debuff_effect(self, target):
        print(f"Сработало {self.debuffname}")
        target.take_damage(self.debuff_effect_damage)
        self.duration -= 1
        if self.duration < 0:
            self.remove_debuff(target)
