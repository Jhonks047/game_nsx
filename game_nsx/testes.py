import random
class Enemy():
    def __init__(self, name=""):
        self.name = name



def enemy():
    orc = Enemy(name="OGRO")
    witch = Enemy(name="BRUXA")
    lista = [orc, witch]
    mostrar(lista)


def mostrar(list):
    inimigo = random.choice(list)
    print(inimigo.name)


enemy()

