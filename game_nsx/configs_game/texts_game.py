from configs_game.text_configs import *
def main_menu_text():
    text = quebraLinha("   Olá novo viajante! Seja muito bem vindo ao jogo {unknown}. Apenas um game totalmente interativo por terminal para alegrar seus dias mais cansativos ou estressantes, na temática SteamPunk. Você será capaz de avançar até o final? Conseguirá conquistar seu tão aclamado desejo? Meu nome é Maximilian e serei seu guia durante sua jornada. Lembre-se, você encontrará todo tipo de inimigo por aqui, então, tome muito cuidado!")
    for linha in text:
        digitacao(linha, 0.01)


def name_text():
    text = quebraLinha("   Sabemos o quão importante é definir o nome de um personagem no começo de sua tragetória, porém, também sabemos o quão difícil é para escolher um nome adequado, portanto, separei algumas sugestões para você, caso queira. Logo abaixo você poderá escolher o nome do seu personagem e para visualizar as sugestões, basta apertar a tecla > ESPAÇO < do seu teclado. Voltarei para te ajudar em breve. E detalhe, você acabou de acordar, se é que posso falar assim, seus motores voltaram a funcionar e você está em um lixão de eletrônicos.")
    for linha in text:
        digitacao(linha, 0.01)


def name_choosen_text(character_name):
    text = quebraLinha(f">> {character_name} << é um ótimo nome! Você realmente parece ter boas escolhas, isso pode te ajudar ao longo da sua jornada então. Bom, estou preparando tudo para você e logo mais irei te explicar como isso funciona, mas, relaxa, não vai ser tão difícil quanto imagina.")
    for linha in text:
        digitacao(linha, 0.01)


def intro_text(character_name):
    text = quebraLinha(f"   Nesse jogo, você seguirá por caminhos totalmente aleatórios a cada vez que iniciar o programa, para que você tenha uma experiência única a cada vez que quiser jogar. Seu personagem recebeu o nome de >> {character_name} << e além do nome, ele também ganha atributos como >> pontos de vida << | >> pontos de dano << e >> pontos de esquiva << | porém, os pontos de dano e de esquiva variam entre 1 a 10 a cada vez que iniciar o programa, como eu falei anteriormente, para tornar sua experiência totalmente única.")
    for linha in text:
        digitacao(linha, 0.01)


def informacoes_character_text():
    text = quebraLinha("    Antes de começar sua jornada, irei mostrar para você seus atributos e informações sobre o seu personagem para que você saiba como prosseguir em seu jogo!")
    for linha in text:
        digitacao(linha, 0.01)


def primeira_trajetoria_text():
    text = quebraLinha(f"   Como você pode ver, essa tabela são seus atributos iniciais, incluindo um sistema de nível, no qual te dará vantagens ao subir como, ataques especiais, desbloquear novas funções, explorar caminhos ocultos. Antes de você começar sua jornada, eu irei te recomendar um lugar para ir primeiro. O lugar é uma cidade caída aqui próximo, chamado Cidade da Queda das Estrelas, lá você poderá conversar com outras pessoas, talvez elas gostariam de conhecer você, te pedir algumas tarefas ou até mesmo recompensar você com algum item raro? Quem sabe... ")
    for linha in text:
        digitacao(linha, 0.01)


def caminho_livre_text():
    text = quebraLinha("    Você teve a sorte de encontrar um caminho livre! Ultimamente essa região anda muito perigosa por questões de saques que alguns bandidos andam fazendo com quem passa por aqui, ou até mesmo certos animais e humanos que foram corrompidos pelo vapor, bom, podemos prosseguir.")
    for linha in text:
        digitacao(linha, 0.01)


def bifurcacao():
    text = quebraLinha("    Parece que você encontrou uma bifurcação. Eu até poderia te ajudar a decidir qual caminho seguir, mas, como disse anteriormente, cada caminho é totalmente aleatório, ou seja, nem eu vou saber qual caminho virá em seguida... Boa sorte!")
    for linha in text:
        digitacao(linha, 0.01)


def primeiroInimigo_text():
    text = quebraLinha("    Você encotrou seu primeiro inimigo! Ele não aparenta ser tão forte, acho que você da conta de derrotá-lo. Escolha qual ação deseja executar. Por você ainda estar no nível 1, você terá apenas duas ações para executar.")
    for linha in text:
        digitacao(linha, 0.01)


def primeiraVitoria_text():
    text = quebraLinha("    Você venceu seu primeiro inimigo e ganhou alguns pontos de experiência. Essa experiência serve para você desbloquear novos itens, novos lugares, novos mapas e até mesmo ao decorrer do game, você pode desbloquear novos tipos de inimigos por ter ficado mais forte! Continue sua jornada e alcance a vitória.")
    for linha in text:
        digitacao(linha, 0.01)


def buraco_maldito_text():
    text = quebraLinha(f"   Você seguiu por um certo caminho e acabou encontrando o >> Buraco Maldito <<")
    pass