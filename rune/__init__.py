from dataclasses import dataclass
from abc import ABC, abstractmethod, abstractproperty
from enum import Enum


class Sect(Enum):

    Swift = 1
    Fatal = 2
    Endure = 3
    Blade = 4
    Violent = 5
    Dispair = 6
    Vampire = 7
    Revenge = 8
    Fight = 9
    Rage = 10
    Energy = 11
    Focus = 12
    Guard = 13
    Will = 14
    Shield = 15
    Nemesis = 16
    Accuracy = 17

class Category(Enum):

    Normal = 1
    Magic = 2
    Rare = 3
    Hero = 4
    Legend = 5


class Slot(Enum):

    one = 1
    two = 2
    three = 3 
    four = 4
    five = 5
    six = 6


class Modifier(Enum):

    Attack = 1
    Defence = 2
    Speed = 3
    Crit_dmg = 4
    Crit_rest = 5


class ModifierType(Enum):

    Percent = 1
    Int = 2


def modifier(mod: Modifier, mtype: ModifierType, value:int) -> dict:
    return dict(mod=mod, mtype=mtype, value=value)


class Rune(object):
    
    def __init__(self, slot, stars) -> None:
        
        self._slot: Slot = slot
        self._stars: int = stars

    @property.setter
    def slot(self, slot: Slot) -> None:
        self._slot = slot

    @property.setter
    def stars(self, stars: int) -> None:
        self._stars = stars


class NormalRune(Rune):

    def __init__(self, slot, stars, modifier: modifier) -> None:
        super(NormalRune).__init__(slot, stars)

        self.modifier: dict = modifier

    @property.setter
    def modifier_value(self, value) -> None:
        self.modifier['value'] = value
    

class MagicRune(Rune):

    def __init__(self, slot, stars, modifier: modifier, modifier2: modifier) -> None:
        super(MagicRune).__init__(slot, stars)

        self.modifier: dict = modifier
        self.modifier2: dict = modifier2

    @property.setter
    def modifier_value(self, value) -> None:
        self.modifier['value'] = value

    @property.setter
    def modifier2_value(self, value) -> None:
        self.modifier2['value'] = value


class RareRune(Rune):

    def __init__(self, slot, stars, modifier: modifier, modifier2: modifier, 
                 modifier3: modifier) -> None:
        super(RareRune).__init__(slot, stars)

        self.modifier: dict = modifier
        self.modifier2: dict = modifier2
        self.modifier3: dict = modifier3

    @property.setter
    def modifier_value(self, value) -> None:
        self.modifier['value'] = value

    @property.setter
    def modifier2_value(self, value) -> None:
        self.modifier2['value'] = value
        
    @property.setter
    def modifier3_value(self, value) -> None:
        self.modifier3['value'] = value


class HeroRune(Rune):

    def __init__(self, slot, stars, modifier: modifier, modifier2: modifier, 
                 modifier3: modifier, modifier4: modifier) -> None:
        super(RareRune).__init__(slot, stars)

        self.modifier: dict = modifier
        self.modifier2: dict = modifier2
        self.modifier3: dict = modifier3
        self.modifier4: dict = modifier4

    @property.setter
    def modifier_value(self, value) -> None:
        self.modifier['value'] = value

    @property.setter
    def modifier2_value(self, value) -> None:
        self.modifier2['value'] = value
        
    @property.setter
    def modifier3_value(self, value) -> None:
        self.modifier3['value'] = value

    @property.setter
    def modifier4_value(self, value) -> None:
        self.modifier4['value'] = value


class LegendRune(HeroRune):

    def __init__(self, slot, stars, modifier: modifier, modifier2: modifier, 
                 modifier3: modifier, modifier4: modifier, modifier5: modifier) -> None:
        super(RareRune).__init__(slot, stars)

        self.modifier: dict = modifier
        self.modifier2: dict = modifier2
        self.modifier3: dict = modifier3
        self.modifier4: dict = modifier4
        self.modifier5: dict = modifier5

    @property.setter
    def modifier_value(self, value) -> None:
        self.modifier['value'] = value

    @property.setter
    def modifier2_value(self, value) -> None:
        self.modifier2['value'] = value
        
    @property.setter
    def modifier3_value(self, value) -> None:
        self.modifier3['value'] = value

    @property.setter
    def modifier4_value(self, value) -> None:
        self.modifier4['value'] = value
        
    @property.setter
    def modifier5_value(self, value) -> None:
        self.modifier5['value'] = value


if __name__ == "__main__":

    mylegend = LegendRune()