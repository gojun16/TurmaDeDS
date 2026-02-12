def calculadora():
    print("--- Calculadora Simples ---")
    num1 = float(input("Digite o primeiro número: "))
    operacao = input("Digite a operação (+, -, *, /): ")
    num2 = float(input("Digite o segundo número: "))

    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        resultado = num1 / num2 if num2 != 0 else "Erro: Divisão por zero"
    else:
        resultado = "Operação inválida"

    print(f"Resultado: {resultado}")

calculadora()
