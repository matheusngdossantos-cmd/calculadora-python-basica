# ==========================================================
# CALCULADORA COM FUNÇÕES EM PYTHON
# Padrão modular e boas práticas de desenvolvimento
# ==========================================================

# 1. Definição das funções para cada operação matemática
def somar(a, b):
    """Retorna a soma de dois números."""
    return a + b

def subtrair(a, b):
    """Retorna a diferença entre dois números."""
    return a - b

def multiplicar(a, b):
    """Retorna o produto de dois números."""
    return a * b

def dividir(a, b):
    """Retorna a divisão de 'a' por 'b', tratando divisão por zero."""
    if b == 0:
        return None  # Indica que a divisão é impossível
    return a / b

# 2. Função principal que coordena o programa
def calculadora():
    print("=== CALCULADORA MODULAR ===")
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    print("---------------------------")
    
    opcao = input("Escolha uma opção (1 a 4): ")
    
    if opcao not in ["1", "2", "3", "4"]:
        print("Opção inválida! Escolha um número de 1 a 4.")
        return

    # Entrada dos números
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    # Chamada da função correspondente à opção escolhida
    if opcao == "1":
        res = somar(num1, num2)
        print(f"Resultado da Soma: {num1} + {num2} = {res:.2f}")
    elif opcao == "2":
        res = subtrair(num1, num2)
        print(f"Resultado da Subtração: {num1} - {num2} = {res:.2f}")
    elif opcao == "3":
        res = multiplicar(num1, num2)
        print(f"Resultado da Multiplicação: {num1} * {num2} = {res:.2f}")
    elif opcao == "4":
        res = dividir(num1, num2)
        if res is None:
            print("Erro matemático: Divisão por zero não permitida!")
        else:
            print(f"Resultado da Divisão: {num1} / {num2} = {res:.2f}")

# 3. Execução do programa
if __name__ == "__main__":
    calculadora()
