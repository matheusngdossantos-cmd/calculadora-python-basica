# ==========================================================
# CALCULADORA SIMPLES EM PYTHON - AS 4 OPERAÇÕES BÁSICAS
# Criado para iniciantes na programação
# ==========================================================

print("=== CALCULADORA SIMPLES ===")
print("Operações disponíveis:")
print("+ : Adição")
print("- : Subtração")
print("* : Multiplicação")
print("/ : Divisão")
print("===========================")

# 1. Entrada de dados: o usuário escolhe a operação
operacao = input("Digite o símbolo da operação desejada (+, -, *, /): ")

# 2. Entrada dos números: usamos float() para aceitar decimais
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# 3. Estrutura condicional para calcular o resultado
if operacao == "+":
    resultado = num1 + num2
    print(f"Resultado: {num1} + {num2} = {resultado:.2f}")

elif operacao == "-":
    resultado = num1 - num2
    print(f"Resultado: {num1} - {num2} = {resultado:.2f}")

elif operacao == "*":
    resultado = num1 * num2
    print(f"Resultado: {num1} * {num2} = {resultado:.2f}")

elif operacao == "/":
    # Verificação de segurança: não existe divisão por zero!
    if num2 == 0:
        print("Erro: Não é possível dividir um número por zero!")
    else:
        resultado = num1 / num2
        print(f"Resultado: {num1} / {num2} = {resultado:.2f}")

else:
    print(f"Operação inválida: '{operacao}'. Escolha apenas +, -, * ou /.")
