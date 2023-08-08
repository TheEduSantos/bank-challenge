import textwrap
from datetime import datetime

def menu():
    menu_text = """\n=============== MENU ===============
[d] Depositar
[s] Sacar
[e] Extrato
[h] Histórico de transações
[nc] Nova conta
[lc] Listar contas
[nu] Novo usuário
[q] Sair
=> """

    return input(textwrap.dedent(menu_text))

# Função Realizar Deposito

def realizar_deposito(saldo, valor, extrato, transacoes, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\nDepósito realizado com sucesso!")
    else:
        print("\nO valor informado é inválido.")
    transacoes.append({"data": datetime.now(), "tipo": "Depósito", "valor": valor})
    return saldo, extrato

# Função Realizar Saque

def realizar_saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques, transacoes):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    transacoes.append({"data": datetime.now(), "tipo": "Saque", "valor": valor})

    if excedeu_saldo:
        print("\nVocê não tem saldo suficiente.")

    elif excedeu_limite:
        print("\nO valor do saque excede o limite.")

    elif excedeu_saques:
        print("\nNúmero máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\nSaque realizado com sucesso!")
    else:
        print("\nO valor informado é inválido.")

    return saldo, extrato

# Função Mostrar Extrato

def mostrar_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

# Mostrar Historico

def mostrar_historico(transacoes):
    print("\n========== HISTÓRICO DE TRANSAÇÕES ==========")
    for transacao in transacoes:
        data = transacao["data"].strftime("%d/%m/%Y %H:%M:%S")
        tipo = transacao["tipo"]
        valor = transacao["valor"]
        print(f"{data} - {tipo}: R$ {valor:.2f}")
    print("==============================================")   


# Função Criar Usuario

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

# Função Filtrar Usuario

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


# Função Criar Conta

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado, fluxo de criação de conta encerrado!")

# Função Listar Conta

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


# Função principal

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    transacoes = []

# Loop

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = realizar_deposito(saldo, valor, extrato, transacoes)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = realizar_saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
                transacoes=transacoes,
            )

        elif opcao == "e":
            mostrar_extrato(saldo, extrato=extrato)

        elif opcao == "h":
            mostrar_historico(transacoes)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()

