# ==========================================================
# CALCULADORA COMPLETA COM LOOP E TRATAMENTO DE EXCEÇÕES
# Programa robusto que não trava com entradas erradas
# ==========================================================

def exibir_menu():
    print("\n" + "=" * 32)
    print("     CALCULADORA PYTHON")
    print("=" * 32)
    print(" [1] Adição (+)")
    print(" [2] Subtração (-)")
    print(" [3] Multiplicação (*)")
    print(" [4] Divisão (/)")
    print(" [0] Sair do programa")
    print("=" * 32)

def ler_numero(mensagem):
    """Lê um número garantindo que o usuário não digite letras ou símbolos."""
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("[Atenção] Valor inválido! Por favor, digite um número.")

def main():
    while True:
        exibir_menu()
        opcao = input("Selecione uma opção: ").strip()

        # Condição de parada do loop
        if opcao == "0":
            print("\nObrigado por usar a calculadora! Bons estudos em Python! 👋")
            break

        if opcao not in ["1", "2", "3", "4"]:
            print("\n[Erro] Opção inválida! Escolha entre 0 e 4.")
            continue

        # Leitura segura dos números
        n1 = ler_numero("Digite o primeiro número: ")
        n2 = ler_numero("Digite o segundo número: ")

        # Processamento da operação
        if opcao == "1":
            print(f"\n>>> SOMA: {n1} + {n2} = {n1 + n2:.2f}")
        elif opcao == "2":
            print(f"\n>>> SUBTRAÇÃO: {n1} - {n2} = {n1 - n2:.2f}")
        elif opcao == "3":
            print(f"\n>>> MULTIPLICAÇÃO: {n1} * {n2} = {n1 * n2:.2f}")
        elif opcao == "4":
            if n2 == 0:
                print("\n>>> [ERRO MATEMÁTICO] Impossível dividir por zero!")
            else:
                print(f"\n>>> DIVISÃO: {n1} / {n2} = {n1 / n2:.2f}")

        # Pausa para o usuário ler o resultado
        input("\nPressione ENTER para continuar...")

if __name__ == "__main__":
    main()
