from configs_game.text_configs import *
import random
def scenarys():
    scenary_list = [
        "Buraco Maldito",
        "Flores da Perdição"
    ]
    choosen_scenary = random.choice(scenary_list)
    titulos(choosen_scenary)

def other_ways():
    other_ways_list = [
        "Bifurcação",
        "Direita",
        "Esquerda",
        "Direita ou Esquerda"
    ]
    other_way_choosed = random.choice(other_ways_list)
    return other_way_choosed

def buracoMaldito():
    pass