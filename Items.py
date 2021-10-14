from random import randint


class Weapon:
    def __init__(self, damage: list = [1, 2], name: str = 'Sword'):
         self.damage = damage
         self.name = name 
         self.__check()

    def get_dmg(self, protect = 0):
        dmg = float(randint(self.damage[0], self.damage[1]))
        dmg -= dmg*0.01*protect
        return round(dmg, 1)

    


    









    def __check(self):
        if type(self.damage) != list:
            raise ValueError("Damage not list!")
        if len(self.damage) > 2:
            raise ValueError("Damage list greater than 2")
        if type(self.damage[0]) != int or type(self.damage[1]) != int:
            raise ValueError("Damage not int") 
        if type(self.name) != str:
            raise ValueError("Name not str!")
        if self.damage[0] > self.damage[1]:
            raise ValueError("The first number is greater than the second!")

class Armor():
    def __init__(self, protect: int = 0, name: str = 'armor'):
        self.protect = protect
        self.name = name
        self.__check()






    def __check(self):
        if type(self.protect) != int:
            raise ValueError("protect not int!")
        if type(self.name) != str:
            raise ValueError("name not str!")
        

class Item():
    def __init__(self, name: str = 'item'):
        self.name = name
        self.__check()

    def __check(self):
        if type(self.name) != str:
            raise ValueError("name not str!")

    