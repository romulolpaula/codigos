# Questão 1

n = int(input("Digite o número:\n"))

x, y = 0,1

while x <= n:
    if x== n:
        print("O número digitado pertence à sequência!")
        break
    x, y = y, x + y
else:
    print("O número digitado não percente à sequência.")