from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
import textwrap
from configs_game.text_configs import *
from time import sleep
from game_sounds.main_sound import *

import random

#! BIBLIOTECAS A SEREM USADAS:
#? soundfile | textwrap | time | random | prompt_toolkit (as vezes) | tabulate | 


class Character:
    def __init__(self, life, damage, dodge):
        self.life = life
        self.damage = damage
        self.dodge = dodge
    
    
    def run(self):
        loading(100, "Carregando arquivos locais...")
        soundboard("main_menu", 0.6)
        titulos("BEM VINDO FORASTEIRO")
        loading(30, "Carregando...")
        locutor()
        main_text = quebraLinha("   Olá novo forasteiro! Seja muito bem vindo ao jogo {unknown}. Apenas um game totalmente interativo por terminal para alegrar seus dias mais cansativos ou estressantes. Você será capaz de avançar até o final? Conseguirá conquistar seu tão aclamado desejo? Meu nome é Maximilian e serei seu guia durante sua jornada. Lembre-se, você encontrará todo tipo de monstro por aqui, então, tome muito cuidado!")
        for main_linha in main_text:
            digitacao(main_linha, 0.05)
        name_options = ["Cedric Ironhart", "Isabella Cogsworth", "Percival Steamweaver", "Elara Gearstone", "Victorina Copperhelm"]
        name_completer = WordCompleter(name_options)
        while True:
            titulos("ESCOLHA UM NOME PARA O SEU PERSONAGEM!")
            name_text = quebraLinha(f"   Sabemos o quão importante é definir o nome de um personagem no começo de sua tragetória, porém, também sabemos o quão difícil é para escolher um nome adequado, portanto, separei algumas sugestões para você, caso queira. Logo abaixo você poderá escolher o nome do seu personagem e para visualizar as sugestões, basta apertar a tecla > ESPAÇO < do seu teclado. Voltarei para te ajudar em breve.")
            for name_linha in name_text:
                digitacao(name_linha, 0.05)
            character_name = prompt("Digite o nome do seu personagem: ", completer=name_completer).strip()
            print(f"O nome que você escolheu para o seu personagem é {color(character_name, 'lcyan')}")
            try:
                confirm = prompt("Confirma seu novo nome? [S / N]: ").strip().upper()
            except ValueError as error:
                print(f"ERRO: Valor inválido. Tipo de erro: {error}")
            else:
                if confirm == "S":
                    titulos(character_name)
                    locutor()
                    name_text2 = quebraLinha(f">> {character_name} << é um ótimo nome! Você realmente parece ter boas escolhas, isso pode te ajudar ao longo da sua jornada então. Bom, estou preparando tudo para você e logo mais irei te explicar como isso funciona, mas, relaxa, não vai ser tão difícil quanto imagina.")
                    for name_linha2 in name_text2:
                        digitacao(name_linha2, 0.05)
                    titulos("INTRODUÇÃO")
                    locutor()
                    text = quebraLinha(f"Nesse jogo, você seguirá por caminhos totalmente aleatórios a cada vez que iniciar o programa, para que você tenha uma experiência única a cada vez que quiser jogar. Seu personagem recebeu o nome de >> {character_name} << e além do nome, ele também ganha atributos como >> pontos de vida << | >> pontos de dano << e >> pontos de esquiva << | porém, os pontos de dano e de esquiva variam entre 1 a 5 a cada vez que iniciar o programa, como eu falei anteriormente, para tornar sua experiência totalmente única. Atualmente seu personagem possui os seguintes atributos.")
                    for linha in text:
                        digitacao(linha, 0.05)
                    break
                else:
                    continue


#! Programa principal
if __name__ == "__main__":
    damage = random.randint(1, 5)
    dodge = random.randint(1, 5)
    new_character = Character(life=100, damage=damage, dodge=dodge).run()