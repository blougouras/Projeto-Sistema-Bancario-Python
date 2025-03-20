def menu():

    print('''
    =====SISTEMA BANCÁRIO=====
          D = Deposito 
          S = Saque 
          E = Extrato
    ''')


def depositoBancario(saldo, extrato):
    valorDeposito = float(input("insira um valor: "))

    if valorDeposito > 0:
        saldo += valorDeposito
        extrato += f"Depósito: R$ {valorDeposito:.2f}\n"
    else:
        print("Valor muito baixo ou negativo, não foi possível realizar a operação. Tente novamente!")
    
    return saldo, extrato

def saqueBancario(saldo, extrato, limite, limiteSaques, numeroSaques):
    if numeroSaques >= limiteSaques:
        print("Limite diário de saques atingido! Tente novamente amanhã.")
        return saldo, extrato, numeroSaques
    
    valorSaque = float(input("Insira um valor para saque: "))

    if valorSaque <= 0:
        print("O valor do saque deve ser positivo.")
    elif valorSaque > saldo:
        print("Saldo insuficiente para realizar o saque.")
    elif valorSaque > limite:
        print(f"Não é possível sacar valores acima de R$ {limite:.2f} por vez.")
    else:
        saldo -= valorSaque
        extrato += f"Saque: R$ {valorSaque:.2f}\n"
        numeroSaques += 1
        print(f"Saque realizado com sucesso!")

    return saldo, extrato, numeroSaques

def exibirExtrato(extrato, saldo):
        print("\n===================== EXTRATO =====================")

        if not extrato:
            print("Não foram realizadas movimentações na conta")
        else:
            print(extrato)

        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=====================================================")

saldo = 0
limite = 500
extrato = ""
numeroSaques = 0
limiteSaques = 3

while True:
    menu()

    opc = input("O que deseja fazer: ")

    if opc == "d":
        saldo, extrato = depositoBancario(saldo, extrato)
    elif opc == "s":
        saldo, extrato, numeroSaques = saqueBancario(saldo, extrato, limite, limiteSaques, numeroSaques)  
    elif opc == "e":
        exibirExtrato(extrato, saldo)
    else:
        break