from view import View
from map import Map

class Game:
    def __init__(self):
        self.mymap = Map()
        self.myview = View()
        self.myview.draw_map(self.mymap.tiles)
        self.myview.draw_hero(self.myview.hero_down, 0, 0)
        self.myview.draw_skeletons()
        self.myview.display()

game = Game()