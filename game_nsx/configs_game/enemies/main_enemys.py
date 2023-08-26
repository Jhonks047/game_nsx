import random
from configs_game.text_configs import *
from tabulate import tabulate

class Enemy():
    def __init__(self, name="", life="", damage="", dodge=""):
        self.name = name
        self.life = life
        self.damage = damage
        self.dodge = dodge
    
    
    def enemy_life(self, damage=0):
        life_remaining = self.life - damage
        life_enemy = color(f"{life_remaining}/{self.life}", "lgreen")
        return life_enemy
    
    
    def dodge_enemy(self):
        dodge_percentage = random.randint(0, self.dodge)
        if dodge_percentage == self.dodge:
            print("O inimigo se esquivou do seu ataque.")
            return False
        else:
            print("O inimigo errou a esquiva! Sua vez de atacar.")
            return True


def enemy_instances():
    #?-----------------------------------------------------------------------------------------------------------------------------------------------#
    #!  Inimigos iniciais | INSTANCIAS
    engrenitinho_ferrujado_lvl_1 = Enemy(name="Engrenitinho Ferrujado nível 1", life=random.randint(15, 30), damage=random.randint(1, 5), dodge=random.randint(1, 2))
    
    rato_mecanico_lvl_1 = Enemy(name="Rato Mecânico nível 1", life=random.randint(15, 30), damage=random.randint(1, 5), dodge=random.randint(1, 2))
    
    chama_fantasma_lvl_1 = Enemy(name="Chama Fantasma nível 1", life=random.randint(15, 30), damage=random.randint(1, 5), dodge=random.randint(1, 2))
    
    gas_toxico_lvl_1 = Enemy(name="Gás Tóxico nível 1", life=random.randint(15, 30), damage=random.randint(1, 5), dodge=random.randint(1, 2))
    
    carrapato_de_engrenagem_lvl_1 = Enemy(name="Carrapato de Engrenagem nível 1", life=random.randint(15, 30), damage=random.randint(1, 5), dodge=random.randint(1, 2))
    #?-----------------------------------------------------------------------------------------------------------------------------------------------#
    
    #?--------------------------------------#
    #   Lista de instancias dos inimigos    #
    basic_enemy_list_initial = [            #
    engrenitinho_ferrujado_lvl_1,           #
    chama_fantasma_lvl_1,                   #
    carrapato_de_engrenagem_lvl_1,          #
    rato_mecanico_lvl_1,                    #
    gas_toxico_lvl_1                        #
    ]                                       #
    #?--------------------------------------#
    enemy_choice(basic_enemy_list_initial)

def enemy_choice(list):
    enemy = random.choice(list)
    print(tabulate(
            [
            [color("Life", "lgreen"), enemy.enemy_life()], 
            [color("Damage", "lred"), enemy.damage], 
            [color("Dodge", "lblue"), enemy.dodge]
            ],
            [f"{color(enemy.name, 'lcyan')}", f"{color('Atributos', 'lmagenta')}"], "simple_grid"
            ))