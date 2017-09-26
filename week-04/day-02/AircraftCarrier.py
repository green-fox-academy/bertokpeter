class AirCraft(object):
    def __init__(self, type):
        self.ammo_store = 0
        if type == "F16":
            self.max_ammo = 8
            self.base_damage = 30
        elif type == "F35":
            self.max_ammo = 12
            self.base_damage = 50
    
    def fight(self):
        return self.ammo_store*self.base_damage
        self.ammo_store = 0
    
    def refill(self, number):
        return number - self.ammo_store
        self.ammo_store = self.ammo_store + number
        if self.ammo_store > self.max_ammo:
            self.ammo_store = self.max_ammo

