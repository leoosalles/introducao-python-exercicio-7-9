# Exercício 7.9
# Escreva um jogo da forca para dois jogadores. Utilize listas de strings para desenhar o boneco da forca. Utilize uma lista de palavras. No início, pergunte um número e calcule o índice da palavra a utilizar pela fórmula:
# índice = (número * 776) % len(lista_de_palavras).

print("\n======== Exercício 7.9 ========\n")

número = int(input("Digite um número: "))

lista_de_palavras = ["faca", "garfo", "prato", "colher", "mesa", "cadeiras", "copo", "garrafa", "comida", "sala", "sofá", "poltrona", "cozinha"]

palavra = lista_de_palavras[(número * 776) % len(lista_de_palavras)]

digitadas = []
acertos = []
erros = 0

linhas_txt = """
X==:==
X  :  
X     
X     
X     
X     
===========

"""

linhas = []

for linha in linhas_txt.splitlines():
    linhas.append(list(linha))

while True:
    senha = ""

    for letra in palavra:
        senha += letra if letra in acertos else "."

    print(senha)

    if senha == palavra:
        print("Você acertou!")
        break

    tentativa = input("\nDigite uma letra:").lower().strip()

    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas += tentativa

        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")

            if erros == 1:
                linhas[3][3] = "O"
            elif erros == 2:
                linhas[4][3] = "|"
            elif erros == 3:
                linhas[4][2] = "\\"
            elif erros == 4:
                linhas[4][4] = "/"
            elif erros == 5:
                linhas[5][2] = "/"
            elif erros == 6:
                linhas[5][4] = "\\"

    for l in linhas:
        print("".join(l))

    if erros == 6:
        print("Enforcado!")
        print(f"A palavra secreta era: {palavra}")
        break
