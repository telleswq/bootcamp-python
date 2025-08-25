import re

usuarios = {}  
def validar_cpf(cpf):
    return re.fullmatch(r"\d{11}", cpf) is not None  
def cadastrar_usuario():
    cpf = input("Digite seu CPF (apenas números, 11 dígitos): ").strip()
    if not validar_cpf(cpf):
        print(" CPF inválido! Digite apenas números com 11 dígitos.")
        return None

    if cpf in usuarios:
        print(" Esse CPF já está cadastrado.")
        return None

    usuarios[cpf] = {
        "saldo": 0,
        "extrato": "",
        "numero_saques": 0
    }
    print(" Usuário cadastrado com sucesso!")
    return cpf

def login():
    cpf = input("Digite seu CPF para entrar: ").strip()
    if cpf in usuarios:
        print(" Login realizado com sucesso!")
        return cpf
    else:
        print(" CPF não encontrado. Cadastre-se primeiro.")
        return None

def exibir_menu():
    return input("""
    ======== BANCO WQ ========
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    ==========================
    => """).lower()

def depositar(usuario):
    try:
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            usuario["saldo"] += valor
            usuario["extrato"] += f"Depósito: R$ {valor:.2f}\n"
            print(f" Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print(" Valor inválido! Informe um valor positivo.")
    except ValueError:
        print(" Entrada inválida! Digite apenas números.")

def sacar(usuario, limite, limite_saques):
    try:
        valor = float(input("Informe o valor do saque: "))

        if valor <= 0:
            print(" Valor inválido! Informe um valor positivo.")
        elif valor > usuario["saldo"]:
            print("  Saldo insuficiente.")
        elif valor > limite:
            print(f"  O limite por saque é de R$ {limite:.2f}.")
        elif usuario["numero_saques"] >= limite_saques:
            print("  Limite diário de saques atingido.")
        else:
            usuario["saldo"] -= valor
            usuario["extrato"] += f"Saque: R$ {valor:.2f}\n"
            usuario["numero_saques"] += 1
            print(f"  Saque de R$ {valor:.2f} realizado com sucesso!")
    except ValueError:
        print("  Entrada inválida! Digite apenas números.")

def exibir_extrato(usuario):
    print("\n========== EXTRATO ==========")
    print("Não foram realizadas movimentações." if not usuario["extrato"] else usuario["extrato"])
    print(f"Saldo atual: R$ {usuario['saldo']:.2f}")
    print("==============================")

def main():
    limite = 500
    LIMITE_SAQUES = 3
    usuario_atual = None

    while not usuario_atual:
        print("\n=== SISTEMA DE ACESSO ===")
        escolha = input("[1] Cadastrar novo usuário\n[2] Login\n[0] Sair\n=> ")

        if escolha == "1":
            usuario_atual = cadastrar_usuario()
        elif escolha == "2":
            usuario_atual = login()
        elif escolha == "0":
            print("  Saindo do sistema...")
            return
        else:
            print("  Opção inválida.")

    usuario = usuarios[usuario_atual]

    while True:
        opcao = exibir_menu()

        if opcao == "d":
            depositar(usuario)
        elif opcao == "s":
            sacar(usuario, limite, LIMITE_SAQUES)
        elif opcao == "e":
            exibir_extrato(usuario)
        elif opcao == "q":
            print(" Obrigado por usar o Banco WQ. Até logo!")
            break
        else:
            print("  Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
