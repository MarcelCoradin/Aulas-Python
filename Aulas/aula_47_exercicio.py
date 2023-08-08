def adivinhar_palavra(palavra_secreta):
    tentativas = 0
    palavra_adivinhada = ['*'] * len(palavra_secreta)

    print("Adivinhe a palavra secreta!")

    while '*' in palavra_adivinhada:
        letra = input("Digite uma letra: ").lower()
        tentativas += 1

        if letra in palavra_secreta:
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == letra:
                    palavra_adivinhada[i] = letra
        else:
            print("Letra não encontrada na palavra secreta. Tente novamente.")

        print("Palavra atual:", " ".join(palavra_adivinhada))

    print(f"Parabéns! Você adivinhou a palavra secreta '{palavra_secreta}' em {tentativas} tentativas.")

# Palavra secreta para o jogo
palavra_secreta = "python"


adivinhar_palavra(palavra_secreta)
