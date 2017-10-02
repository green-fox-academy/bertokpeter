from view import View
from map import Map

class Game:
    def __init__(self):
        self.mymap = Map()
        self.myview = View()
        self.myview.draw_map(self.mymap.tiles)
        self.myview.display()

game = Game()