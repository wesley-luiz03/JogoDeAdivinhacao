print("Sejam bem-vindos! Tente adivinhar o número que seu amigo escolheu!")

number1 = int(input("Digite o número para adivinhar: "))
print("\n" * 500)

tentativas = 0

while True:

    tentativas += 1

    number2 = int(input("Qual número o 1º jogador digitou? "))
    if number2 == number1:
        print("Uau! Você acertou! Parabéns!")
        break
    elif tentativas == 5:
        print("Que pena! Você usou todas as suas tentativas.")
        break
    