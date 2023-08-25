from configs_game.text_configs import *
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