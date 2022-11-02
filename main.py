
from robots import Robots
from dinosaur import Dinosaur
from weapons import Weapons
from battlefields import Battlefields
intro=print("Dino Slayer")
intro2=print("Welcome to Dino Slayer, Choose Your Robot")

Player_one=Robots("chuckie")
print(Player_one.name)
print(Player_one.health)

Weapon=print('choose your weapon of choice')
print(Player_one.active_weapon.name,(Player_one.active_weapon.attack))

opponent="vs"
if opponent == "vs":
 print(opponent)

Computer=Dinosaur("Destroyer")
print(Computer.name)
print(Computer.health)
print(Computer.attack_power)


Back_Up_Weapon_Optional=Weapons
print(Back_Up_Weapon_Optional.name)
print(Back_Up_Weapon_Optional.attack)



Arenas = Battlefields
print(Battlefields.robot)
print(Battlefields.dinosaur)

