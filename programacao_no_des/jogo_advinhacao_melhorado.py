# Importa o módulo 'random', que fornece funções para gerar números aleatórios [1].
# A biblioteca 'random' é parte da biblioteca padrão do Python.
import random 

# Gera um número inteiro aleatório entre 1 e 10 (inclusive) e armazena na variável 'numero_secreto' [1, 2].
numero_secreto = random.randint(1, 10) 

# Inicializa o contador de tentativas do jogador
tentativas = 0 
# Define o limite máximo de tentativas permitidas
max_tentativas = 5 

# Exibe mensagens de boas-vindas ao usuário
print("Bem-vindo ao jogo de adivinhação!") 
print("Tente adivinhar o número que estou pensando, entre 1 e 10.") 

# Inicia o loop 'while' que roda enquanto o jogador não superar o número máximo de tentativas
while tentativas < max_tentativas: 
    # Captura a entrada do usuário e a converte para um número inteiro (int)
    palpite = int(input("Digite seu palpite: ")) 
    
    # Incrementa o número de tentativas em 1 a cada palpite dado
    tentativas += 1 
    
    # Estrutura condicional para verificar se o palpite está correto
    if palpite == numero_secreto: 
        # Se acertar, exibe a mensagem de sucesso e encerra o loop com 'break'
        print(f"Parabéns! Você acertou o número em {tentativas} tentativas.") 
        break 
    # Se o palpite for menor que o número secreto, dá uma dica
    elif palpite < numero_secreto: 
        print("Quase lá! Tente um número maior.") 
    # Se o palpite for maior que o número secreto, dá uma dica
    else: 
        print("Quase lá! Tente um número menor.") 
        
    # Informa ao jogador quantas tentativas restam, se ainda houver
    if tentativas < max_tentativas: 
        print(f"Você tem {max_tentativas - tentativas} tentativas restantes.") 
    else: 
        # Mensagem exibida caso o jogador esgote as tentativas sem acertar
        print("Infelizmente, você não acertou. O número era", numero_secreto) 

# Mensagem final fora do loop
print("Fim do jogo!") 
