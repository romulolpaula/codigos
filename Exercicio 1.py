# Questão 1

#INDICE = 13
#SOMA = 0
#K = 0

#while K<INDICE:
#    K= K + 1
#    SOMA= SOMA + K
    
#print (SOMA)

# Questão 2

n = int(input("Digite o número:"))

x, y = 0,1

while x <= n:
    if x== n:
        print("O número digitado pertence à sequência!")
        break
    x, y = y, x + y
else:
    print("O número digitado não percente à sequência.")