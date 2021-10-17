from random import randint
import typing

DamageInfo = typing.Sequence[int]
ArgsChecker = typing.Dict[str, typing.Sequence]

NORMAL_DAMAGE_LENGTH = 2
NORMAL_DAMAGE_TYPE = int


def real_damage(damage: float, defence: float) -> int:
    return round(damage-(damage*0.01*defence))


class Item:
    arg_types: ArgsChecker = {"name": [str, "raise ValueError(f'Name must be str, got {arg}({type(arg)})')"]}

    @staticmethod
    def check_args(args: typing.Dict[str, typing.Any], arg_types: ArgsChecker):
        for (arg, normalType) in arg_types.items():
            if not isinstance(args[arg], normalType[0]):
                exec(normalType[1], {"ValueError": ValueError, "arg": arg})
        return True


class Weapon(Item):
    arg_types: ArgsChecker = {"damage": [typing.Sequence, "raise ValueError(f'Damage is not subclass of typing.Sequence type, got {arg}({type(arg)})')"],
                              "name": [str, "raise ValueError(f'Wrong type for name str or bytes excepted, got {arg}({type(arg)})')"]}

    def __init__(self, damage: DamageInfo, name: typing.AnyStr):
        if self.check_args({"damage": damage, "name": name}, self.arg_types):
            self._damage = damage
            self._name = name
    @property
    def damage(self):
        return float(randint(self._damage[0], self._damage[1]))

    @property
    def name(self):
        return self._name

    def check_args(self, args: typing.Dict[str, typing.Any], arg_types: ArgsChecker):
        super().check_args(args, self.arg_types)
        if any(not isinstance(damageConfig, int) for damageConfig in args["damage"]):
            raise ValueError(f"Wrong types in damage: {type(args['damage'])}")
        elif len(args["damage"]) != 2:
            raise ValueError(f"Damage length must be 2, got {len(args['damage'])}")
        return True


class Armor(Item):
    arg_types: ArgsChecker = {"name": [str, "raise ValueError(f'Wrong type for name str or bytes excepted, got {arg}({type(arg)})')"],
                              "defence": [int, 'raise ValueError(f"Defence must be int, got {arg}({type(arg)})")']}

    def __init__(self, defence: int, name: typing.AnyStr):
        if super().check_args({"defence": defence, "name": name}, self.arg_types):
            self._defence = defence
            self._name = name


Weapon([1, 2], "stuka")
