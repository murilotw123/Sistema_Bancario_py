import textwrap

def menu():
    menu = """
    [D]\t - Depositar
    [S]\t - Sacar
    [E]\t - Extrato
    [NC]\t - Nova conta
    [LC]\t - Listar contas
    [N]\t - Novo usuário
    [Q]\t - Sair
    """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato): 
    print("\nExtrato")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}\n")

def criar_usuario(usuarios):
    print("Cadastrando novo usuário")
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Já existe um usuário com esse CPF.")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    usuario = {"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf}
    usuarios.append(usuario)
    print("Usuário criado com sucesso.")

def filtrar_usuario(cpf, usuarios):
    return next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)

def criar_conta(contas, usuarios, agencia="0001"):
    cpf = input("Digite o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        numero_conta = len(contas) + 1
        conta = {"agencia": agencia, "numero": numero_conta, "usuario": usuario}
        contas.append(conta)
        print("Conta criada com sucesso.")
    else:
        print("Usuário não encontrado.")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência:\t{conta["agencia"]}
            C/C:\t\t{conta["numero"]}
            Titular:\t{conta["usuario"]["nome"]}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []
    
    while True:
        opcao = menu()
        
        if opcao == "D":
            valor = float(input("Quanto deseja depositar? "))
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "S":
            valor = float(input("Quanto deseja sacar? "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo, 
                valor=valor, 
                extrato=extrato, 
                limite=limite,
                numero_saques=numero_saques, 
                LIMITE_SAQUES=LIMITE_SAQUES
            )
        
        elif opcao == "E":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "NC":
            criar_conta(contas, usuarios, agencia=AGENCIA)
        
        elif opcao == "LC":
            listar_contas(contas)
        
        elif opcao == "N":
            criar_usuario(usuarios)
        
        elif opcao == "Q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
