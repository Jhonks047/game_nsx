from colorama import Fore, Style, Back, init
import textwrap
from time import sleep
from prompt_toolkit import prompt

init(autoreset=True)


def color(text, sit):
    """Alterar a cor da frase/texto

    Args:
        text (STRING): Aqui será definido o texto/mensagem que o usuário irá colocar cores.
        sit (STRING): Definir a cor que será usada.
            Cores disponíveis:
            
                - red  |  lred
                - green  |  lgreen
                - blue  |  lblue
                - magenta  |  lmagenta
                - cyan  |  lcyan
                - yellow  |  lyellow
                - white  |  lwhite
                
            As cores que possuem o " l " antes do tipo da cor é para indicar que a cor é mais clara
    """
    sit = str(sit).lower()
#TODO......................NORMAL COLORS......................

    if sit == "red":
        return f"{Fore.RED+Style.BRIGHT}{text}"
    elif sit == "green":
        return f"{Fore.GREEN+Style.BRIGHT}{text}"
    elif sit == "blue":
        return f"{Fore.BLUE+Style.BRIGHT}{text}"
    elif sit == "magenta":
        return f"{Fore.MAGENTA+Style.BRIGHT}{text}"
    elif sit == "cyan":
        return f"{Fore.CYAN+Style.BRIGHT}{text}"
    elif sit == "yellow":
        return f"{Fore.YELLOW+Style.BRIGHT}{text}"
    elif sit == "white":
        return f"{Fore.WHITE+Style.BRIGHT}{text}"
    
#TODO......................LIGHT COLORS......................

    elif sit == "lred":
        return f"{Fore.LIGHTRED_EX+Style.BRIGHT}{text}"
    elif sit == "lgreen":
        return f"{Fore.LIGHTGREEN_EX+Style.BRIGHT}{text}"
    elif sit == "lblue":
        return f"{Fore.LIGHTBLUE_EX+Style.BRIGHT}{text}"
    elif sit == "lmagenta":
        return f"{Fore.LIGHTMAGENTA_EX+Style.BRIGHT}{text}"
    elif sit == "lcyan":
        return f"{Fore.LIGHTCYAN_EX+Style.BRIGHT}{text}"
    elif sit == "lyellow":
        return f"{Fore.LIGHTYELLOW_EX+Style.BRIGHT}{text}"
    elif sit == "lwhite":
        return f"{Fore.LIGHTWHITE_EX+Style.BRIGHT}{text}"


def titulos(msg):
    """FORMATAR TÍTULOS

    Args:
        msg (STRING): Mensagem que irá formatar em formato TÍTULO
    """
    msg = str(msg)
    width = 60
    print()
    print("-~" * 30)
    print(f"{msg.center(width)}")
    print("-~" * 30)
    print()
    sleep(1)


def quebraLinha(msg):
    new_text = textwrap.wrap(msg, 60)
    return new_text


def digitacao(msg, delay_ms=0.1):
    for letra in msg:
        print(f"{color(letra, 'lgreen')}", end="")
        sleep(delay_ms)
    print()

def loading(time_ms, msg="loading"):
    """Barra de carregamento

    Args:
        total (INT): Definir o tamanho do tempo de carregamento
        msg (str, optional): Mensagem para ser exibida ao lado da barra de carregamento. Padrão "loading".
    """
    from time import sleep
    from tqdm import tqdm
    print()
    for _ in tqdm(range(time_ms), desc=Fore.LIGHTWHITE_EX+Style.BRIGHT+f"{msg}", ascii=False, ncols=50, bar_format="{l_bar}{bar}"+Style.RESET_ALL):
        sleep(0.05)
    print()


def options_SN(text):
    """Validar opções
    
    Raises:
        ValueError: Causar uma exceção quando digitado um valor não permitido

    Returns:
        STR: Retornar a option para o menu na qual ele foi chamado.
    """
    while True:
        try:
            option = prompt(f"{text}: ").strip().upper()
            if option not in ["S", "N"]:
                raise ValueError("Valor inválido!")
            else:
                break
        except ValueError as error:
            print(color(f"Erro: {error}","r"))
    return option
    


def locutor():
    digitacao(r"""
           .-----.
 \ ' /   _/    )/
- ( ) -('---''--)
 / . \((()\^_^/)()
  \\_\ (()_)-((()()
   '- \ )/\._./(()
     '/\/( X   ) \
     (___)|___/ ) \
          |.#_|(___)
         /\    \ ( (_
         \/\/\/\) \\
         | / \ |
         |(   \|
        _|_)__|_\_
        )...()...(
         | (   \ |     
      .-'__,)  (  \
                '\_-,
""", 0.01)


def dead():
    print(r"""
                   .-'''''-.
                  /         \
         .-.      |  _   _  |      .-.
        (_. '._   | |_\ /_| |   _.' ._)
           '-._'-.(_   A   _).-'_.-'
               '-._| _____ |_.-'
              _.-'_\`'''''`/_'-._
         .-.-'_.-'  `-----'  '-._'-.-.
        (,_.'`                   `'._,)
""")


def character_walking():
    pass