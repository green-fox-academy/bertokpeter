class Pirates(object):
    def __init__(self):
        self.drunkness = 0
        self.status = "awake"

    def drink_some_rum(self):
        if self.status != "awake":
            return self.get_status()
        else:
            self.drunkness += 1
    
    def how_it_going_mate(self):
        if self.status != "awake":
            return self.get_status()
        elif self.drunkness < 5:
            return "Pour me anudder!"
        else:
            self.status = "sleeping"
            print("Arghh, I'ma Pirate. How d'ya d'ink its goin?")
            return self.get_status()
    
    def get_status(self):
        if self.status == "awake":
            return "The pirate is alive and well"
        if self.status == "sleeping":
            return "The pirate is passed out"
        if self.status == "dead":
            return "He's dead"

    def die(self):
        self.status = "dead"

Jack = Pirates()
Jack.die()
print(Jack.how_it_going_mate())