import random
from configs_game.text_configs import *
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