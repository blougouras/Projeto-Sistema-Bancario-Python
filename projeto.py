import textwrap

def menu():

    print(textwrap.dedent('''
    =====SISTEMA BANCÁRIO=====
          D = Deposito 
          S = Saque 
          E = Extrato
          NU = Criar Usuário
          NC = Criar Conta
          LC = Listar Contas
          Q = Sair
    '''))

def depositoBancario(saldo, extrato, /):
    valorDeposito = float(input("insira um valor: "))

    if valorDeposito > 0:
        saldo += valorDeposito
        print()
        print("Depósito realizado com sucesso!")
        extrato += f"Depósito: R$ {valorDeposito:.2f}\n"
    else:
        print("Valor muito baixo ou negativo, não foi possível realizar a operação. Tente novamente!")
    
    return saldo, extrato

def saqueBancario(*, saldo, extrato, limite, limiteSaques, numeroSaques):
    if numeroSaques >= limiteSaques:
        print("Limite diário de saques atingido! Tente novamente amanhã.")
        return saldo, extrato, numeroSaques
    
    valorSaque = float(input("Insira um valor para saque: "))
    print()

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

def exibirExtrato(saldo, /, *, extrato):
        print("\n===================== EXTRATO =====================")

        if not extrato:
            print("Não foram realizadas movimentações na conta")
        else:
            print(extrato)

        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=====================================================")


def criarUsuario(usuarios):
    cpf = input("Informe o seu CPF (somente números): ")
    usuario = filtrarUsuario(cpf, usuarios)

    if usuario:
        print("\n Já existe um usuário com esse CPF!!")
        return
    
    nome = input("Seu nome completo: ")
    dataNascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe seu endereço (logradouro, nro - bairro - cidade / UF): ")

    usuarios.append({"nome": nome, "dataNascimento": dataNascimento, "cpf": cpf, "endereço": endereco})

def filtrarUsuario(cpf, usuarios):
    usuariosFiltrados = []
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuariosFiltrados.append(usuario)
    
    return usuariosFiltrados[0] if usuariosFiltrados else None


def criarConta(agencia, numeroConta, usuarios):
    cpf = input("Informe o seu CPF (somente números): ")
    usuario = filtrarUsuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso!")
        return {"agencia": agencia, "numeroConta": numeroConta, "usuario": usuario}
    
    print("\n Usuário não encontrado, encerrando fluxo de criação de conta!")

def listarContas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta["agencia"]}
            C/C:\t{conta["numeroConta"]}
            Titular:\t{conta["usuario"]["nome"]}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():

    saldo = 0
    limite = 500
    extrato = ""
    numeroSaques = 0
    limiteSaques = 3

    agencia = "0001"
    usuarios = []
    contas = []


    while True:
        menu()

        opc = input("O que deseja fazer: ")

        if opc == "d":
            saldo, extrato = depositoBancario(saldo, extrato)
        elif opc == "s":
            saldo, extrato, numeroSaques = saqueBancario(saldo = saldo, extrato = extrato, limite = limite, limiteSaques = limiteSaques, numeroSaques = numeroSaques)  
        elif opc == "e":
            exibirExtrato(saldo, extrato = extrato)
        elif opc == "nu":
            criarUsuario(usuarios)
        elif opc == "nc":
            numeroConta = len(contas) + 1
            conta = criarConta(agencia, numeroConta, usuarios)

            if conta:
                contas.append(conta)
        elif opc == "lc":
            listarContas(contas)
        elif opc == "q":
            print("Agradeçemos a preferência, tenha um bom dia!!")
            break
        else:
            print("Operação Inválida, tente novamente!")

if __name__ == "__main__":
    main()