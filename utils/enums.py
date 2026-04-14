from enum import Enum

class LoadersEnum(Enum):
    FORGE = "forge"
    FABRIC = "fabric"
    NEOFORGE = "neoforge"

class MinecraftVersionsEnum(Enum):
    V1_20_1 = "1.20.1"
    V1_21_1 = "1.21.1"
    V1_12_2 = "1.12.2"
    V1_16_5 = "1.16.5"

class TagsEnum(Enum):
    VANILLA = "vanilla"
    MODDED = "modded"
    TECHNO = "techno"
    HORROR = "horror"
    ADVENTURE = "adventure"
    PUZZLE = "puzzle"
    SIMULATION = "simulation"
    RPG = "rpg"
    STRATEGY = "strategy"
    ACTION = "action"
    ONESHOT = "oneshot"
    MAGIC = "magic"