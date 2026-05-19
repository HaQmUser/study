
from src.my_awesome_project.Classes.sorcerer import Sorcerer


class TestSorcererCreation:
    test_sorc = Sorcerer("Sample")

    def test_creation(self):
        assert self.test_sorc.charname == "Sample"
        assert self.test_sorc.role == "Волшебник"
        assert 70 <= self.test_sorc.hp <= 90
        assert self.test_sorc.gun is not None
        assert self.test_sorc.spells is not None


class TestIsAlive:
    test_sorc = Sorcerer("Sample")

    def test_is_alive(self):
        assert self.test_sorc.is_alive() is True
        self.test_sorc.hp = 0
        assert self.test_sorc.is_alive() is False
        self.test_sorc.hp = -10
        assert self.test_sorc.is_alive() is False
        self.test_sorc.hp = 1
        assert self.test_sorc.is_alive() is True


class TestTakingDamage:
    test_sorc = Sorcerer("Sample")

    def test_take_damage(self):
        hp = self.test_sorc.hp
        dmg = 10
        self.test_sorc.take_damage(dmg)
        assert self.test_sorc.hp == hp - dmg
        self.test_sorc.hp = 1
        self.test_sorc.take_damage(dmg)
        assert self.test_sorc.hp == 0


class TestAttacking:
    test_sorc = Sorcerer("Sample")
    test_target = Sorcerer("Target")

    def test_attacking(self):
        target_hp = self.test_target.hp
        dmg = self.test_sorc.gun.damage
        assert dmg == self.test_sorc.gun.damage
        self.test_sorc.attack(self.test_target)
        assert self.test_target.hp == target_hp - dmg
