from weapons import Weapons


class Robots:

    def _init_(self,names_passed_in,Weapons_passed_in):
        self.name=names_passed_in
        self.health=100
        self.active_weapon= Weapons_passed_in()
        
    
    def attack(self,dinosaur):
        pass

