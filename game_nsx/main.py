from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from configs_game.text_configs import *
from configs_game.texts_game import *
from time import sleep
from game_sounds.main_sound import *
from tabulate import tabulate
from configs_game.other_configs import *

import random

#! BIBLIOTECAS A SEREM USADAS:
#? soundfile | textwrap | time | random | prompt_toolkit (as vezes) | tabulate | 


class Character:
    def __init__(self, name="UNKNOWN", life=100, damage=0, dodge=0):
        self.life = life
        self.damage = damage
        self.dodge = dodge
        self.name = name
        self.level = 1
        self.experience = 0
        self.experience_requirements = [0, 150]
    
    
    def gain_experience(self, amount):
        self.experience += amount
        while self.experience >= self.experience_requirements[self.level]:
            self.level_up
    
    
    def level_up(self):
        self.level += 1
        next_requirement = self.experience_requirements[-1] + 100
        self.experience_requirements.append(next_requirement)
        print(f"{color('Parabéns!', 'lgreen')} O seu personagem {color(self.name, 'lcyan')} subiu para o nível {color(self.level, 'lwhite')}!")
    
    def character_info(self):
        exp = f"{self.experience}/{self.experience_requirements[-1]}"
        print(tabulate(
            [
            [color("Life", "lgreen"), self.life], 
            [color("Damage", "lred"), self.damage], 
            [color("Dodge", "lblue"), self.dodge],
            [color("Experience", "lyellow"), exp],
            ],
            [f"{color(self.name, 'lcyan')}", f"{color('Level', 'lmagenta')}: {color(self.level, 'lwhite')}"], "simple_grid"
            ))
    
    def run(self):
        loading(100, "Carregando arquivos locais...")
        soundboard("main_menu", 0.6)
        titulos("BEM VINDO FORASTEIRO")
        loading(30, "Carregando...")
        locutor()
        main_menu_text() # Texto da apresentação
        name_options = ["Cedric Ironhart", "Isabella Cogsworth", "Percival Steamweaver", "Elara Gearstone", "Victorina Copperhelm"]
        name_completer = WordCompleter(name_options)
        titulos("ESCOLHA UM NOME PARA O SEU PERSONAGEM!")
        name_text() # Texto para a escolha do nome do jogador
        while True:
            character_name = prompt("Digite o nome do seu personagem: ", completer=name_completer).strip()
            print(f"O nome que você escolheu para o seu personagem é {color(character_name, 'lcyan')}")
            confirm = options_SN(text="Gostaria de confirmar seu nome? [ S / N ]")
            if confirm == "S":
                break
            else:
                print(color("Voltando a seleção de nomes.", "lcyan"))
        damage = random.randint(1, 10)
        dodge = random.randint(1, 10)
        your_character = Character(name=character_name, damage=damage, dodge=dodge)
        titulos(character_name)
        locutor()
        name_choosen_text(character_name) # Elogiando a escolha do nome e preparando cenário.
        titulos("INTRODUÇÃO")
        locutor()
        intro_text(character_name) # Explicação de como será o jogo
        informacoes_character_text() # Mostrar os atributos
        titulos("INFORMAÇÕES DO PERSONAGEM")
        your_character.character_info()
        locutor()
        primeira_trajetoria() # Texto da primeira trajetória
        titulos(f"ESCOLHA O QUE DESEJA FAZER > > {self.name} < <")
        print(f"""
    {color("[ A ] Explorar a floresta antes de seguir.", "lgreen")}
    {color("[ B ] Perguntar ao locutor se há outra coisa a se fazer.", "lyellow")}
    {color("[ C ] Ir para a Vila da Queda das Estrelas.", "lmagenta")}
    
{color("[ X ] Sair do jogo.", "red")}
    """)
        choice = choices("A", "B", "C", "X")
        if choice == "A":
            titulos("CAMINHANDO ATÉ A FLORESTA")
            loading(50, "Explorando...")
        


#! Programa principal
if __name__ == "__main__":
    Character().run()