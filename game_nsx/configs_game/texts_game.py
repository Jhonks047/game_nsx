from configs_game.text_configs import *
def main_menu_text():
    text = quebraLinha("   Olá novo forasteiro! Seja muito bem vindo ao jogo {unknown}. Apenas um game totalmente interativo por terminal para alegrar seus dias mais cansativos ou estressantes. Você será capaz de avançar até o final? Conseguirá conquistar seu tão aclamado desejo? Meu nome é Maximilian e serei seu guia durante sua jornada. Lembre-se, você encontrará todo tipo de monstro por aqui, então, tome muito cuidado!")
    for linha in text:
        digitacao(linha, 0.01)


def name_text():
    text = quebraLinha("   Sabemos o quão importante é definir o nome de um personagem no começo de sua tragetória, porém, também sabemos o quão difícil é para escolher um nome adequado, portanto, separei algumas sugestões para você, caso queira. Logo abaixo você poderá escolher o nome do seu personagem e para visualizar as sugestões, basta apertar a tecla > ESPAÇO < do seu teclado. Voltarei para te ajudar em breve.")
    for linha in text:
        digitacao(linha, 0.01)


def name_choosen_text(character_name):
    text = quebraLinha(f">> {character_name} << é um ótimo nome! Você realmente parece ter boas escolhas, isso pode te ajudar ao longo da sua jornada então. Bom, estou preparando tudo para você e logo mais irei te explicar como isso funciona, mas, relaxa, não vai ser tão difícil quanto imagina.")
    for linha in text:
        digitacao(linha, 0.01)


def intro_text(character_name):
    text = quebraLinha(f"   Nesse jogo, você seguirá por caminhos totalmente aleatórios a cada vez que iniciar o programa, para que você tenha uma experiência única a cada vez que quiser jogar. Seu personagem recebeu o nome de >> {character_name} << e além do nome, ele também ganha atributos como >> pontos de vida << | >> pontos de dano << e >> pontos de esquiva << | porém, os pontos de dano e de esquiva variam entre 1 a 5 a cada vez que iniciar o programa, como eu falei anteriormente, para tornar sua experiência totalmente única.")
    for linha in text:
        digitacao(linha, 0.01)


def informacoes_character_text():
    text = quebraLinha("    Antes de começar sua jornada, irei mostrar para você seus atributos e informações sobre o seu personagem para que você saiba como prosseguir em seu jogo!")
    for linha in text:
        digitacao(linha, 0.01)


def primeira_trajetoria():
    text = quebraLinha(f"   Como você pode ver, essa tabela são seus atributos iniciais, incluindo um sistema de nível, no qual te dará vantagens ao subir como, ataques especiais, desbloquear novas funções, explorar caminhos ocultos. Antes de você começar sua jornada, eu irei te recomendar um lugar para ir primeiro. O lugar é um vilarejo aqui próximo, chamado Vila da Queda das Estrelas, lá você poderá conversar com outras pessoas, talvez elas gostariam de conhecer você, te pedir algumas tarefas ou até mesmo recompensar você com algum item raro? Quem sabe...")
    for linha in text:
        digitacao(linha, 0.01)


def buraco_maldito_text():
    text = quebraLinha(f"   Você seguiu por um certo caminho e acabou encontrando o >> Buraco Maldito <<")