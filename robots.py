from tkinter.font import names
from weapons import Weapons


class Robots:

    def __init__(self,names):
        self.name=names
        self.health=100
        self.active_weapon= Weapons("crossbow",500)
        
    
    def attack(self,dinosaur):
        pass

