from datetime import datetime

# Definição das Constantes

MENU = """
[d] Depositar
[s] Sacar
[e] Extrato
[h] Histórico de transações
[q] Sair
=> """

SALDO_INICIAL = 0
LIMITE_SAQUE = 500
LIMITE_SAQUES = 3

# Variáveis globais

saldo = SALDO_INICIAL
extrato = ""
numero_saques = 0
transacoes = []

# Função Realizar Deposito

def realizar_deposito():
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        global saldo, extrato, transacoes
        saldo += valor
        extrato += "Depósito: R$ {:.2f}\n".format(valor)
        transacoes.append({"data": datetime.now(), "tipo": "Depósito", "valor": valor})
    else:
        print("Operação falhou! O valor informado é inválido.")

# Função Realizar Saque

def realizar_saque():
    global saldo, extrato, numero_saques
    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > LIMITE_SAQUE
    excedeu_saques = numero_saques >= LIMITE_SAQUES
    transacoes.append({"data": datetime.now(), "tipo": "Retirada", "valor": valor})


    if excedeu_saldo:
        print("Saldo insuficiente.")
    elif excedeu_limite:
        print("Saque excede o limite. Tente novamente com um valor menor")
    elif excedeu_saques:
        print("Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += "Saque: R$ {:.2f}\n".format(valor)
        numero_saques += 1
    else:
        print("O valor informado é inválido.")

# Função Mostrar Extrato

def mostrar_extrato():
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato) #"Se o extrato não tiver conteúdo (string vazia), retorne 'Não foram realizadas movimentações.', caso contrário, retorne o próprio extrato."
    print("Saldo: R$ {:.2f}".format(saldo))
    print("===========================================")

# Mostrar Historico

def mostrar_historico():
    print("\n========== HISTÓRICO DE TRANSAÇÕES ==========")
    for transacao in transacoes:
        data = transacao["data"].strftime("%d/%m/%Y %H:%M:%S")
        tipo = transacao["tipo"]
        valor = transacao["valor"]
        print(f"{data} - {tipo}: R$ {valor:.2f}")
    print("==============================================")

# Loop

while True:
    opcao = input(MENU)

    if opcao == "d":
        realizar_deposito()

    elif opcao == "s":
        realizar_saque()

    elif opcao == "e":
        mostrar_extrato()

    elif opcao == "h":
        mostrar_historico()

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
