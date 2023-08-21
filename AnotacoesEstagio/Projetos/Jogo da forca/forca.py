import random
from unidecode import unidecode

tentativas = 6

with open('palavras.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.readlines()
    linha = random.randint(0, len(conteudo) - 1)
    palavraSecreta = conteudo[linha].strip().upper()

print(palavraSecreta)
underlines = len(palavraSecreta) * '_'

while tentativas > 0:
    print(underlines)
    letra = input('Digite uma letra: ').upper()
    letraSemAcento = unidecode(letra)

    if letra == palavraSecreta:
        print('Parabéns, você venceu!')
        break
    elif letraSemAcento in unidecode(palavraSecreta):
        print('Sim')
        posicoes = []
        for indice, letraSecreta in enumerate(palavraSecreta):
            if unidecode(letraSecreta) == letraSemAcento:
                posicoes.append(indice)

        for posicao in posicoes:
            underlines = underlines[:posicao] + letra + underlines[posicao+1:]

        print(underlines)
        print(f'Número de tentativas restantes: {tentativas}')

        if not '_' in underlines:
            print('Parabéns, você venceu!')
            break
    else:
        tentativas -= 1
        print('Não')
        print(f'Número de tentativas restantes: {tentativas}')


print('Fim de Jogo')
