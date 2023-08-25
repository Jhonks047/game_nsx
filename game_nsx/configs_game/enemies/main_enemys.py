from random import randint

class Enemy():
    def __init__(self, life, damage, dodge):
        self.life = life
        self.damage = damage
        self.dodge = dodge
    
    
    def enemy_life(self, damage):
        life_remaining = self.life - damage
        print(f"{life_remaining}/{self.life}")


class Player():
    def __init__(self, attack):
        self.attack = attack
    
    
    def attack(self):
        attack = randint(1, 5)

enemy_list = []
orc = Enemy(life=20, damage=2, dodge=1)
player = Player(attack=randint(1, 5))

orc.enemy_life(player.attack)