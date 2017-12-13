class Aircraft(object):
    def __init__(self, type):
        self.type = type
        if type == "F16":
            self.max_ammo = 8
            self.base_damage = 30
        else:
            self.max_ammo = 12
            self.base_damage = 50

    def fight(self):
        self.damage = self.max_ammo * self.base_damage
        print("All Damage: " + self.damage.__str__())

    def refill(self, amount_ammo = 2300):
        self.amount_ammo = amount_ammo
        if self.type == "F16":
            self.max_ammo = 8
            self.amount_ammo -= 8
        else:
            self.max_ammo = 12
            self.amount_ammo -= 12
        print("Remaining ammo: " + self.amount_ammo.__str__())

    def get_type(self):
        print("Type: " + self.type.__str__())

    def get_status(self):
        result = ""
        result += "Type " + self.type.__str__() + "," + " Ammo: " + self.max_ammo.__str__() + " Base Damage: " \
                + self.base_damage.__str__() + " All Damage: " + (self.max_ammo * self.base_damage).__str__()
        print(result)

class Carrier:
    def __init__(self, health = 5000):
        self.health = health
        self.carrier = []

    def add_air(self, airc):
        self.carrier.append(airc)

    def fill(self):
        pass

    def get_status(self):
        total_damage = 0
        for item in self.carrier:
            total_damage += (item.base_damage * item.max_ammo)
        print("HP: " + self.health.__str__()+ " Aircraft count : " + len(self.carrier).__str__() +
              " Ammo Storage: 2300, Total damage: " + str(total_damage))
        print("Aircrafts:")
        for item in self.carrier:
            item.get_status()



f16_01 = Aircraft("F16")
aircraft = Aircraft("F16")
aircraft.get_status()
aircraft.get_type()
aircraft.refill()
aircraft.fight()
aircraft.fight()
f35_01 = Aircraft("F35")
f16_02 = Aircraft("F16")
f35_02 = Aircraft("F35")
carrier = Carrier()
carrier.add_air(f16_01)
carrier.add_air(f35_01)
carrier.add_air(f16_02)
carrier.add_air(f35_02)

carrier.get_status()






