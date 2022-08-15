def validatefunction(opcao, numero1, numero2) :
    if opcao == '+' :
        return numero1 + numero2
    elif opcao == '-' :
        return numero1 - numero2
    elif opcao == '/' :
        return numero1/numero2
    elif opcao == '*' :
        return numero1*numero
    else:
        raise ValueError('Insert a valid option')

opcao = input("Digite a opcao desejada: ")
print(validatefunction(opcao, int(input("Digite o primeiro número:")), int(input("Digite o segundo número: "))))