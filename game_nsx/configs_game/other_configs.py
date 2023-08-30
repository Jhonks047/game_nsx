from configs_game.text_configs import *
from configs_game.texts_game import *
from configs_game.enemies.main_enemys import *
from game_sounds.main_sound import *

def choices(*options):
    """Validar as ações do player
    
    Raises:
        ValueError: Causar uma exceção quando digitado um valor não permitido

    Returns:
        STR: Retornar a option para o menu na qual ele foi chamado.
    """
    while True:
        try:
            option = str(input(f"Digite uma ação: ")).strip().upper()
            if option not in options:
                raise ValueError("Valor inválido!")
            else:
                break
        except ValueError as error:
            print(f"Erro: {error}")
    return option


def random_events_enemy():
    #choice = random.randint(1, 5)
    choice = 1
    if choice == 1 or choice == 3:
        return True
    else:
        return False


def combat(your_character):
    sleep(1)
    soundboard("entrada_inimigo", 0.5)
    titulos("INIMIGO ENCONTRADO!")
    sleep(1)
    enemy = enemy_instances()
    locutor()
    primeiroInimigo_text()
    print(f"""
        {color("[ A ] Atacar o inimigo", "lgreen")}
        {color("[ B ] Fugir", "lyellow")}
        
    {color("[ X ] Sair do jogo.", "red")}""")
    action = choices("A", "B", "X")
    if action == "A":
        print("Você escolheu atacar!")
        titulos("COMBATE")
        while True:
            if not enemy.edodge():
                loading(25, "Lançando ataque ao inimigo...")
                print(color(">> Ataque bem-sucedido!", 'lgreen'))
                soundboard("enemy_hit", 0.5)
                sleep(1)
                print(f"Sua vida: {your_character.clife(sit='str')}", end=" | ")
                print(f"Vida do inimigo: {enemy.show_life(damage=your_character.attack(), sit='str')}")
                print()
                if enemy.show_life(sit="int") <= 0:
                    enemy_status = "died"
                    titulos("VOCÊ DERROTOU O INIMIGO!")
                    soundboard("enemy_died", 0.5)
                    fadeout(1000)
                    break
                else:
                    continue
            else:
                sleep(1)
                print(color(">> Você errou!", 'lred'))
                sleep(1)
                loading(25, "Inimigo lançando ataque... Cuidado!")
            if your_character.cdodge():
                print(color(">> Você esquivou !", 'lcyan'))
            else:
                sleep(1)
                print(color(">> Você errou a esquiva!", 'lred'))
                soundboard("player_hit", 0.5)
                sleep(1)
                print(f"Sua vida: {your_character.clife(damage=enemy.attack(), sit='str')}", end=" | ")
                print(f"Vida do inimigo: {enemy.show_life(sit='str')}")
                if your_character.clife(sit="int") <= 0:
                    character_status = "died"
                    soundboard("jogador_derrotado", 0.5)
        if enemy_status == "died":
            soundboard("fase_concluida", 0.5)
            return True
        elif character_status == "died":
            return False


def enemy_experience(type=""):
    if type == "basic":
        exp = random.randint(1, 50)
        return exp