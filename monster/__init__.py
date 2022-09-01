from dataclasses import dataclass


class Monster(dataclass):

    experiance: int
    level: int
    hp: int
    hp_modifier: int
    attack: int
    attack_modifier: int
    defence: int
    defence_modifier: int
    speed: int
    speed_modifier: int

    crit_rate: int
    crit_dmg: int
    resistance: int
    accuracy: int

    

