class AirCraft(object):
    def __init__(self, type):
        self.ammo_store = 0
        self.type = type
        if self.type == "F16":
            self.max_ammo = 8
            self.base_damage = 30
        elif self.type == "F35":
            self.max_ammo = 12
            self.base_damage = 50
    
    def fight(self):
        return self.ammo_store*self.base_damage
        self.ammo_store = 0
    
    def refill(self, number):
        fill_amount = self.max_ammo - self.ammo_store
        self.ammo_store = self.ammo_store + number
        if self.ammo_store > self.max_ammo:
            self.ammo_store = self.max_ammo
        return 0 if fill_amount > number else number - fill_amount

    def getType(self):
        return self.type

    def getStatus(self):
        return "Type: {}, Ammo: {}, Base Damage: {}, All Damage {}".format(self.type, self.ammo_store,
        self.base_damage,self.base_damage*self.ammo_store)

class Carrier(AirCraft):
    def __init__(self, ammo, health):
        self.aircrafts = []
        self.ammo_store = int(ammo)
        self.health = health

    def addAircraft(type):
        self.aircrafts.append(AirCraft(type))

    def fill_aircrafts(self, type):
        for aircraft in self.aircrafts:
                if aircraft.getType() == type:
                    self.ammo_store = aircraft.refill(self.ammo_store)
        return self.ammo_store

    def fill(self):
        if ammo_store = 0:
            print("Not enough ammo")
        else:
            self.fill_aircrafts("F35")
            if self.ammo_store > 0:
                self.fill_aircrafts("F16")
    
    def fight(self, carrier):
        self.damage = 0
        for aircraft in self.aircrafts:
            self.damage += aircraft.fight()
        carrier.health -= self.damage