def exibir_menu():
    return input("""
    ======== BANCO WQ ========
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    ==========================
    => """).lower()

def depositar(saldo, extrato):
    try:
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f" Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print(" Valor inválido! Informe um valor positivo.")
    except ValueError:
        print(" Entrada inválida! Digite apenas números.")
    return saldo, extrato

def sacar(saldo, extrato, limite, numero_saques, limite_saques):
    try:
        valor = float(input("Informe o valor do saque: "))

        if valor <= 0:
            print("Valor inválido! Informe um valor positivo.")
        elif valor > saldo:
            print(" Saldo insuficiente.")
        elif valor > limite:
            print(f" O limite por saque é de R$ {limite:.2f}.")
        elif numero_saques >= limite_saques:
            print(" Limite diário de saques atingido.")
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f" Saque de R$ {valor:.2f} realizado com sucesso!")
    except ValueError:
        print(" Entrada inválida! Digite apenas números.")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n========== EXTRATO ==========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("==============================")

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = exibir_menu()

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo, extrato, limite, numero_saques, LIMITE_SAQUES)
        elif opcao == "e":
            exibir_extrato(saldo, extrato)
        elif opcao == "q":
            print(" Obrigado por usar o Banco WQ. Até logo!")
            break
        else:
            print(" Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
