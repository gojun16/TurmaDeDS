import random

# Gera um número aleatório entre 1 e 10
numero_secreto = random.randint(1, 10)
max_tentativas = 5
tentativa_atual = 1
bonus_concedido = False  # Flag para conceder o bônus apenas uma vez

print("Bem-vindo ao jogo de adivinhação!")
print(f"Tente adivinhar o número (1-10). Você tem {max_tentativas} tentativas.")

# Loop while para permitir alteração dinâmica do número de tentativas
while tentativa_atual <= max_tentativas:
    # Captura a entrada do usuário
    try:
        palpite = int(input(f"\nTentativa {tentativa_atual}/{max_tentativas}. Digite seu palpite: "))
    except ValueError:
        print("Entrada inválida. Digite um número.")
        continue

    # Verifica o palpite do jogador
    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou o número em {tentativa_atual} tentativas.")
        break
    else:
        # Lógica do bônus: se a diferença for 1, ganha +1 tentativa
        if abs(palpite - numero_secreto) == 1 and not bonus_concedido:
            max_tentativas += 1
            bonus_concedido = True
            print("Quase lá! Bônus: +1 tentativa concedida!")
        elif palpite < numero_secreto:
            print("Tente um número maior.")
        else:
            print("Tente um número menor.")

    # Checa se as tentativas acabaram
    if tentativa_atual == max_tentativas:
        print(f"\nSuas tentativas acabaram. O número era {numero_secreto}.")
        break
    
    tentativa_atual += 1

print("Fim do jogo!")
