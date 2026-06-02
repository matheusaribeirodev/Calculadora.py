import os
sentinela = 1 

while (sentinela == 1):
    print("*******************")
    print("1 - para adiçao")
    print("2 - para subtraçao")
    print("3 - para multiplicaçao")
    print("4 - para divisao")
    print("*******************")

    operacao = input("Escolha a operaçao: ")
    valor1 = input("digite o primeiro número: ")
    valor2 = input("digite o segundo número: ")

    operacao = int(operacao)
    valor1 = float(valor1)
    valor2 = float(valor2)

    if(operacao == 1):
        resultado = valor1 + valor2
    elif(operacao == 2):
        resultado = valor1 - valor2
    elif(operacao == 3):
        resultado = valor1 * valor2
    elif(operacao == 4):
        resultado = valor1 / valor2
    else:
        resultado = 0
    print("Operaçao nao informada corretamente")

    print("O resultado do cáculo é: ", resultado)

    print("_______________________________________________")
    print("deseja continuar?")
    print("1 - SIM")
    print("2 - NAO")
    
    sentinela = int(input("informe a opcao: "))
    os.system("cl")