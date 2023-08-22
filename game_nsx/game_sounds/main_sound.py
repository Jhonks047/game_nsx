from pygame import mixer
from time import sleep


def soundboard(type="", sound=0.0):
    type = type.lower()
    if type == "main_menu":
        mixer.init()
        mixer.music.load(r"C:\Users\jhona\OneDrive\Documentos\MeusProjetos\game_nsx\game_nsx\game_sounds\main_menu.wav")
        mixer.music.set_volume(sound)
        mixer.music.play()
    elif type == "boss_derrotado":
        mixer.init()
        mixer.music.load(r"C:\Users\jhona\OneDrive\Documentos\MeusProjetos\game_nsx\game_nsx\game_sounds\boss_derrotado.mp3")
        mixer.music.play()
    elif type == "boss_entrance":
        mixer.init()
        mixer.music.load(r"C:\Users\jhona\OneDrive\Documentos\MeusProjetos\game_nsx\game_nsx\game_sounds\boss_entrance.mp3")
        mixer.music.play()
    elif type == "buying_item":
        mixer.init()
        mixer.music.load(r"C:\Users\jhona\OneDrive\Documentos\MeusProjetos\game_nsx\game_nsx\game_sounds\buying_item.mp3")
        mixer.music.play()
    elif type == "enemy_died":
        mixer.init()
        mixer.music.load(r"C:\Users\jhona\OneDrive\Documentos\MeusProjetos\game_nsx\game_nsx\game_sounds\enemy_died.mp3")
        mixer.music.play()
    elif type == "enemy_hit":
        mixer.init()
        mixer.music.load(r"C:\Users\jhona\OneDrive\Documentos\MeusProjetos\game_nsx\game_nsx\game_sounds\enemy_hit.mp3")
        mixer.music.play()
    elif type == "entrada_inimigo":
        mixer.init()
        mixer.music.load(r"C:\Users\jhona\OneDrive\Documentos\MeusProjetos\game_nsx\game_nsx\game_sounds\entrada_inimigo.mp3")
        mixer.music.play()
    elif type == "entrada_jogador":
        mixer.init()
        mixer.music.load(r"C:\Users\jhona\OneDrive\Documentos\MeusProjetos\game_nsx\game_nsx\game_sounds\entrada_jogador.mp3")
        mixer.music.play()
    elif type == "fase_concluida":
        mixer.init()
        mixer.music.load(r"C:\Users\jhona\OneDrive\Documentos\MeusProjetos\game_nsx\game_nsx\game_sounds\fase_concluida.mp3")
        mixer.music.play()
    elif type == "jogador_derrotado":
        mixer.init()
        mixer.music.load(r"C:\Users\jhona\OneDrive\Documentos\MeusProjetos\game_nsx\game_nsx\game_sounds\jogador_derrotado.mp3")
        mixer.music.play()
    elif type == "level_up":
        mixer.init()
        mixer.music.load(r"C:\Users\jhona\OneDrive\Documentos\MeusProjetos\game_nsx\game_nsx\game_sounds\level-up-sound-effect.mp3")
        mixer.music.play()
    elif type == "player_hit":
        mixer.init()
        mixer.music.load(r"C:\Users\jhona\OneDrive\Documentos\MeusProjetos\game_nsx\game_nsx\game_sounds\player_hit.mp3")
        mixer.music.play()
    elif type == "digital":
        mixer.init()
        mixer.music.load(r"C:\Users\jhona\OneDrive\Documentos\MeusProjetos\game_nsx\game_nsx\game_sounds\digital_text.wav")
        mixer.music.play()


def fadeout(time_ms):
    mixer.music.fadeout(time_ms)