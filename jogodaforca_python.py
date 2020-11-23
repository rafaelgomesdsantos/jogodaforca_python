""""
Código 16 rafgds
"""
import random

palavras = "futebol basquete tenis volei rugby".split ()

bonecoIMG = [""""

  ----+
  |   |
      |
      |
      |
      |
===========""", """

  ----+
  |   |
  O   |
      |
      |
      |
===========""", """

  ----+
  |   |
  O   |
  |   |
      |
      |
===========""", """

  ----+
  |   |
  O   |
 /|   |
      |
      |
===========""", """

  ----+
  |   |
  O   |
 /|\  |
      |
      |
===========""", """

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
===========""", """

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
==========="""]


def main():
    global bonecoIMG

    print ("\033[32m" + "--------------Jogo da Forca---------------")
    print ("\nBem-vindo jogador, vamos jogar forca?")
    print ("\nPara começar gostaria de saber o seu nome")
    nome = (input ("\nQual é o seu nome? "))
    print ("\nO que? Você aqui outra vez", nome,
           "? Sou eu o Botlomeu dentro de outro jogo, agora todo em verde, gostou? =P")
    print ("\nBom... sem mais enrolação, a dica é: ESPORTES")
    print ("Boa sorte", nome, "!")
    letrasErradas = ""
    letrasAcertadas = ""
    palavraSecreta = geraPalavraAleatoria ().upper ()
    jogando = True

    while jogando:

        imprimeJogo (letrasErradas, letrasAcertadas, palavraSecreta)

        palpite = recebePalpite (letrasErradas + letrasAcertadas)

        if palpite in palavraSecreta:

            letrasAcertadas += palpite

            if VerificaSeGanhou (palavraSecreta, letrasAcertadas):
                print ("\nParabéns,", nome, " a palavra secreta era " + palavraSecreta + "! Você joga muito!")
                jogando = False
        else:
            letrasErradas += palpite

            if len (letrasErradas) == len (bonecoIMG) - 1:
                imprimeJogo (letrasErradas, letrasAcertadas, palavraSecreta)

                print ("Game over para você", nome)
                print ("depois de " + str (len (letrasErradas)) + " erros e " + str (len (letrasAcertadas)), end=" ")
                print ("acertos, a palavra era " + palavraSecreta + ".")

                jogando = False

        if not jogando:

            if JogarNovamente ():
                letrasErradas = ""

                letrasAcertadas = ""

                jogando = True
                palavraSecreta = geraPalavraAleatoria ().upper ()


def geraPalavraAleatoria():
    global palavras
    return random.choice (palavras)


def imprimeComEspacos(palavra):
    for letra in palavra:
        print (letra, end=" ")

    print ()


def imprimeJogo(letrasErradas, letrasAcertadas, palavraSecreta):
    global bonecoIMG

    print (bonecoIMG[len (letrasErradas)] + "\n")

    print ("Letras Erradas:", end=" ")

    imprimeComEspacos (letrasErradas)

    vazio = "_" * len (palavraSecreta)

    for i in range (len (palavraSecreta)):

        if palavraSecreta[i] in letrasAcertadas:
            vazio = vazio[:i] + palavraSecreta[i] + vazio[i + 1:]

    imprimeComEspacos (vazio)


def recebePalpite(palpiteFeitos):
    while True:

        palpite = input ("\nVamos lá tente alguma letra: ").upper ()
        if palpite in palpiteFeitos:
            print ("\nVocê já digitou essa letra ")
        else:
            return palpite


def JogarNovamente():
    return input ("Quer jogar novamente? (Sim ou Não)\n").upper ().startswith ("S")


def VerificaSeGanhou(palavraSecreta, letrasAcertadas):
    ganhou = True
    for letra in palavraSecreta:
        if letra not in letrasAcertadas:
            ganhou = False
            break
    return ganhou


main ()