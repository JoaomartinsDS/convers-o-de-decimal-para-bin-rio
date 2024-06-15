menu = """
########## CONVERSOR DE DECIMAL PARA BINÁRIO ##########

"""
decimal = int(input("Digite o número a ser convertido: "))
numero_convertido = []

while decimal >= 1:
    if decimal % 2 == 0:
        numero_convertido.append(0)
    elif decimal%2==1:
        numero_convertido.append(1)
    decimal //= 2
print(numero_convertido[::-1])
