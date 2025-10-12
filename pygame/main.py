import pygame
from pygame.locals import *
from sys import exit
from lista_objetos import fase
import random


pygame.init()

# Configurações da tela
largura = 1050
altura = 700
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Palavras Cruzadas')
relogio = pygame.time.Clock()

# Imagem de fundo
try:
    fundo = pygame.image.load('img/fundo.png')
    fundo = pygame.transform.scale(fundo, (largura, altura))
except:
    print('Imagem de fundo não encontrada. Usando cor sólida')
    fundo = None
# Cores RGB
AZUL_CLARO = (173, 216, 230)
BRANCO = (255, 255, 255)
AZUL_VITORIA = (81, 103, 138)
PRETO = (0, 0, 0)

# Lista de letras
letras = []
for animal in fase:
    for letra in animal.nome.lower():
        letras.append(letra)

random.shuffle(letras)

# Loop registro posições letras
posicoes = []
x_pos = 20
y_pos = 525

for letra in letras:
    letra_info = {
        'letra': letra,
        'x': x_pos,
        'y': y_pos,
        'rect': pygame.Rect(x_pos, y_pos, 80, 80),
        'arrastando': False,
        'encaixada': False,
        'pos_original': (x_pos, y_pos),
        'visivel': True
    }
    x_pos += 92
    if x_pos >= 950:
        x_pos = 20
        y_pos = 610
    posicoes.append(letra_info)

# Slots para as palavras cruzadas
slots = []
x_central = 340
y_central = 266

# GATO - Horizontal
gato_letras = 'gato'
for i, letra in enumerate(gato_letras):
    slot_info = {
        "x": x_central + i * 85,
        "y": y_central,
        "letra_correta": letra,
        "ocupado": False,
        "rect": pygame.Rect(x_central + i * 85, y_central, 80, 80),
        "animal": next(animal for animal in fase if animal.nome.lower() == "gato")
    }
    slots.append(slot_info)

# CÃO - Vertical
cao_letras = "cão"
pos_o_gato = gato_letras.index('o')
for i, letra in enumerate(cao_letras):
    slot_info = {
        "x": x_central + pos_o_gato * 85,
        "y": y_central + (i - 2) * 85,
        "letra_correta": letra,
        "ocupado": False,
        "rect": pygame.Rect(x_central + pos_o_gato * 85, y_central + (i - 2) * 85, 80, 80),
        "animal": next(animal for animal in fase if animal.nome.lower() == "cão")
    }
    slots.append(slot_info)

# RATO - Vertical
rato_letras = "rato"
pos_a_gato = gato_letras.index('a')
for i, letra in enumerate(rato_letras):
    slot_info = {
        "x": x_central + pos_a_gato * 85,
        "y": y_central + (i - 1) * 85,
        "letra_correta": letra,
        "ocupado": False,
        "rect": pygame.Rect(x_central + pos_a_gato * 85, y_central + (i - 1) * 85, 80, 80),
        "animal": next(animal for animal in fase if animal.nome.lower() == "rato")
    }
    slots.append(slot_info)

# Imagens das LETRAS
lista_imagens = {}
for letra_info in posicoes:
    letra = letra_info['letra']
    try:
        caminho_imagem = f'img/{letra}_divertida.png'
        carregando_imagem = pygame.image.load(caminho_imagem)
        carregando_imagem = pygame.transform.scale(carregando_imagem, (80, 80))
        lista_imagens[letra] = carregando_imagem
    except:
        print(f"Imagem da letra {letra} não encontrada, criando fallback")
        surf = pygame.Surface((80, 80))
        surf.fill(BRANCO)
        font = pygame.font.Font(None, 60)
        text = font.render(letra.upper(), True, PRETO)
        text_rect = text.get_rect(center=(40, 40))
        surf.blit(text, text_rect)
        lista_imagens[letra] = surf

# Variáveis para controle
letra_arrastando = None
offset_x = 0
offset_y = 0
fonte = pygame.font.Font(None, 36)
vitoria = False


def verificar_vitoria():
    return all(slot["ocupado"] for slot in slots)


def atualizar_encaixe_animais():
    for animal in fase:
        slots_animal = [slot for slot in slots if slot['animal'].nome == animal.nome]
        animal.encaixado = all(slot['ocupado'] for slot in slots_animal)


while True:
    relogio.tick(60)

    if fundo:
        tela.blit(fundo, (0, 0))
    else:
        tela.fill(AZUL_CLARO)

    # Processamento de eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if not vitoria:
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    for letra_info in posicoes:
                        if (letra_info['visivel'] and not letra_info['encaixada']
                                and letra_info['rect'].collidepoint(event.pos)):
                            letra_arrastando = letra_info
                            offset_x = letra_info['rect'].x - event.pos[0]
                            offset_y = letra_info['rect'].y - event.pos[1]
                            letra_info['arrastando'] = True
                            break

            if event.type == MOUSEBUTTONUP:
                if event.button == 1 and letra_arrastando:
                    letra_arrastando['arrastando'] = False

                    encaixou = False
                    for slot in slots:
                        if (letra_arrastando['rect'].colliderect(slot['rect']) and
                                not slot['ocupado'] and
                                letra_arrastando['letra'] == slot['letra_correta']):

                            letra_arrastando['x'] = slot['x']
                            letra_arrastando['y'] = slot['y']
                            letra_arrastando['rect'].x = slot['x']
                            letra_arrastando['rect'].y = slot['y']
                            letra_arrastando['encaixada'] = True
                            slot['ocupado'] = True
                            encaixou = True

                            atualizar_encaixe_animais()

                            if verificar_vitoria():
                                vitoria = True
                                print("PARABÉNS! Vitória alcançada!")
                            break

                    if not encaixou and not letra_arrastando['encaixada']:
                        letra_arrastando['x'], letra_arrastando['y'] = letra_arrastando['pos_original']
                        letra_arrastando['rect'].x = letra_arrastando['x']
                        letra_arrastando['rect'].y = letra_arrastando['y']

                    letra_arrastando = None

            if event.type == MOUSEMOTION:
                if letra_arrastando and letra_arrastando['arrastando'] and not letra_arrastando['encaixada']:
                    letra_arrastando['x'] = event.pos[0] + offset_x
                    letra_arrastando['y'] = event.pos[1] + offset_y
                    letra_arrastando['rect'].x = letra_arrastando['x']
                    letra_arrastando['rect'].y = letra_arrastando['y']

    # Desenhar todas as letras
    for posicao in posicoes:
        if posicao['visivel']:
            tela.blit(lista_imagens[posicao['letra']], (posicao['x'], posicao['y']))

    # Mensagem de vitória
    if vitoria:
        texto = fonte.render("PARABÉNS! Você completou!", True, AZUL_VITORIA)
        tela.blit(texto, (largura // 2 - 150, 50))

    pygame.display.update()