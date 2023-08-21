from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
import textwrap
from configs_game.text_configs import *
from time import sleep
from pydub import AudioSegment
from pydub.playback import play

import random

#! BIBLIOTECAS A SEREM USADAS:
#? soundfile | textwrap | time | random | prompt_toolkit (as vezes) | tabulate | 


class Character:
    def __init__(self, life, damage, dodge):
        self.life = life
        self.damage = damage
        self.dodge = dodge
    
    
    def run(self):
        titulos("BEM VINDO FORASTEIRO")
        
        main_text = quebraLinha("   Olá novo forasteiro! Seja muito bem vindo ao jogo {unknown}. Apenas um game totalmente interativo por terminal para alegrar seus dias mais cansativos ou estressantes. Você será capaz de avançar até o final? Conseguirá conquistar seu tão aclamado desejo? Meu nome é Maximilian e serei seu guia durante sua jornada. Lembre-se, você encontrará todo tipo de monstro por aqui, então, tome muito cuidado!")
        for linha in main_text:
            print(color(f"{linha}", "lgreen"))
            sleep(0.5)
        name_options = ["Cedric Ironhart", "Isabella Cogsworth", "Percival Steamweaver", "Elara Gearstone", "Victorina Copperhelm"]
        name_completer = WordCompleter(name_options)
        while True:
            titulos("ESCOLHA UM NOME PARA O SEU PERSONAGEM")
            name_text = quebraLinha("   Sabemos o quão importante é definir o nome de um personagem no começo de sua tragetória, porém, também sabemos o quão difícil é para escolher um nome adequado, portanto, separei algumas sugestões para você, caso queira. Logo abaixo você poderá escolher o nome do seu personagem e para visualizar as sugestões, basta apertar a tecla {ESPAÇO} do seu teclado. Voltarei para te ajudar em breve.")
            audio_file = "C:\Users\jhona\OneDrive\Documentos\MeusProjetos\game_nsx\game_nsx\game_sounds\boss_derrotado.mp3"
            character_name = prompt("Digite o nome do seu personagem: ", completer=name_completer).strip()
            print(f"O nome que você escolheu para o seu personagem é {character_name}")
            try:
                confirm = prompt("Confirma seu novo nome? [S / N]: ").strip().upper()
            except ValueError as error:
                print(f"ERRO: Valor inválido. Tipo de erro: {error}")
            else:
                if confirm == "S":
                    audio = AudioSegment.from_mp3(audio_file)
                    play(audio)
                    break
                else:
                    continue
        


#! Programa principal
if __name__ == "__main__":
    damage = random.randint(1, 5)
    dodge = random.randint(1, 5)
    new_character = Character(life=100, damage=damage, dodge=dodge).run()