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
        damage = self.ammo_store*self.base_damage
        self.ammo_store = 0
        return damage
    
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
        self.ammo_store = ammo
        self.health = health

    def addAircraft(self, type):
        self.aircrafts.append(AirCraft(type))

    def fill_aircrafts(self, type):
        for aircraft in self.aircrafts:
                if aircraft.getType() == type:
                    self.ammo_store = aircraft.refill(self.ammo_store)
        return self.ammo_store

    def fill(self):
        if self.ammo_store == 0:
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
        return carrier.health if carrier.health > 0 else carrier.dead()
    
    def total_damage(self):
        self.damage = 0
        for aircraft in self.aircrafts:
            self.damage += aircraft.base_damage*aircraft.ammo_store
        return self.damage

    def getStatus(self):
        if self.health > 0:
            status = "HP: {}, Aircraft count: {}, Ammo Storage: {}, Total Damage {}\nAircrafts:\n".format(
                self.health, len(self.aircrafts), self.ammo_store,
            self.total_damage())
            for aircraft in self.aircrafts:
                status += "Type {}, Ammo: {}, Base Damage: {}, All Damage: {}\n".format(aircraft.type,
                aircraft.ammo_store, aircraft.base_damage, aircraft.ammo_store*aircraft.base_damage)
            return status
        else:
            return self.dead()

    def dead(self):
        return "It's dead, Jim."

protoss = Carrier(400, 5000)
DeathStar = Carrier(40, 4000)

protoss.addAircraft("F16")
protoss.addAircraft("F16")
protoss.addAircraft("F35")
protoss.addAircraft("F35")
protoss.addAircraft("F35")
protoss.addAircraft("F35")
protoss.addAircraft("F35")
protoss.addAircraft("F35")
DeathStar.addAircraft("F16")
DeathStar.addAircraft("F16")

protoss.fill()
DeathStar.fill()
protoss.fight(DeathStar)
print(DeathStar.getStatus())

