import random
###


class Items:



    def __int__(self, gold, potions, weapons, armour):
        self.gold = gold
        self.potions = potions
        self.weapons = weapons
        self.armour = armour

    
class Weapons(Items):

    def __int__(self, weapons):
        return super().__int__(weapons)
    
    def select_weapons(self):
        self.weapons = ["sword", "axe", "dagger", "hammer", "bow", "crossbow"]


    """def valors_item(self):

        rusty: int = 0
        average: int = 1
        good: int = 2
        overkill: int = 3

        for x in range(4):
            if x == 0:
                return f"""