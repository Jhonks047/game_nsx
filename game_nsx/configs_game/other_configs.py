import random
from configs_game.text_configs import *
from configs_game.texts_game import *
from configs_game.enemies.main_enemys import *

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
    titulos("INIMIGO ENCONTRADO!")
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
        loading(50, "Lançando ataque ao inimigo...")
        while True:
            sleep(5)
            if not enemy.dodge_enemy():
                print("O inimigo errou a esquiva! Seu ataque foi certeiro.")
                print(f"Vida do inimigo: {enemy.enemy_life(damage=your_character.character_attack(), sit='str')}")
                if enemy.enemy_life(sit="int") <= 0:
                    enemy_status = "died"
                    break
                else:
                    continue
            else:
                print("O inimigo se esquivou do seu ataque.")
                print("Hora do inimigo atacar!")
                if your_character.character_dodge():
                    print("Você esquivou do ataque do inimigo!")
                else:
                    print("Você errou a esquiva...")
                    print(f"Sua vida: {your_character.character_life(damage=enemy.enemy_attack(), sit='str')}")
                    if your_character.character_life(sit="int") <= 0:
                        character_status = "died"
        if enemy_status == "died":
            return True
        elif character_status == "died":
            return False