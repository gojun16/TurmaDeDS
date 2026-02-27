def calcular_desconto():
    print("--- Calculadora de Desconto ---")
    
    try:
        # Solicita o preço do produto
        preco = float(input("Digite o preço do produto: R$ "))
        
        # Solicita o código de desconto
        codigo = input("Digite o código de desconto (A, B ou C): ").upper()
        
        desconto = 0
        
        # Aplica o desconto correspondente
        if codigo == 'A':
            desconto = 0.10  # 10%
        elif codigo == 'B':
            desconto = 0.20  # 20%
        elif codigo == 'C':
            desconto = 0.30  # 30%
        else:
            print("Código inválido! Nenhum desconto aplicado.")
        
        # Calcula o preço final
        preco_final = preco * (1 - desconto)
        
        # Exibe o resultado
        print(f"Preço original: R$ {preco:.2f}")
        print(f"Desconto aplicado: {desconto*100:.0f}%")
        print(f"Preço final: R$ {preco_final:.2f}")
        
    except ValueError:
        print("Erro: Por favor, digite um valor numérico válido para o preço.")

# Executa a função
calcular_desconto()
