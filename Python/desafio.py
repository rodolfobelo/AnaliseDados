inicio = int(input("Entre com o numero inicio do vetor:"))
fim = int(input("Entre com o numero do final do vetor:"))

for numero in range(inicio, fim + 1):
    if((numero % 2) == 0):
        print(numero)