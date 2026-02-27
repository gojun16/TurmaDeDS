import random

mainDict = [{"word": "maca", "id": 1, "class": "fruta"},
  {"word": "banana", "id": 2, "class": "fruta"},
  {"word": "abacaxi", "id": 3, "class": "fruta"},
  {"word": "manga", "id": 4, "class": "fruta"},
  {"word": "uva", "id": 5, "class": "fruta"},
  {"word": "morango", "id": 6, "class": "fruta"},
  {"word": "laranja", "id": 7, "class": "fruta"},
  {"word": "melancia", "id": 8, "class": "fruta"},
  {"word": "pera", "id": 9, "class": "fruta"},
  {"word": "goiaba", "id": 10, "class": "fruta"},
  {"word": "limao", "id": 11, "class": "fruta"},
  {"word": "caju", "id": 12, "class": "fruta"},
  {"word": "ameixa", "id": 13, "class": "fruta"},
  {"word": "acerola", "id": 14, "class": "fruta"},
  {"word": "pitaya", "id": 15, "class": "fruta"},
   # /* --- CATEGORIA: ANIMAIS (ID 16-40) --- */
  {"word": "cachorro", "id": 16, "class": "animal"},
  {"word": "elefante", "id": 17, "class": "animal"},
  {"word": "girafa", "id": 18, "class": "animal"},
  {"word": "hipopotamo", "id": 19, "class": "animal"},
  {"word": "jacare", "id": 20, "class": "animal"},
  {"word": "leopardo", "id": 21, "class": "animal"},
  {"word": "macaco", "id": 22, "class": "animal"},
  {"word": "onca", "id": 23, "class": "animal"},
  {"word": "papagaio", "id": 24, "class": "animal"},
  {"word": "quati", "id": 25, "class": "animal"},
  {"word": "raposa", "id": 26, "class": "animal"},
  {"word": "tartaruga", "id": 27, "class": "animal"},
  {"word": "urso", "id": 28, "class": "animal"},
  {"word": "veado", "id": 29, "class": "animal"},
  {"word": "zebra", "id": 30, "class": "animal"},
  {"word": "baleia", "id": 31, "class": "animal"},
  {"word": "tubarao", "id": 32, "class": "animal"},
  {"word": "golfinho", "id": 33, "class": "animal"},
  {"word": "pinguim", "id": 34, "class": "animal"},
  {"word": "aguia", "id": 35, "class": "animal"},
  {"word": "coruja", "id": 36, "class": "animal"},
  {"word": "formiga", "id": 37, "class": "animal"},
  {"word": "abelha", "id": 38, "class": "animal"},
  {"word": "aranha", "id": 39, "class": "animal"},
  {"word": "escorpiao", "id": 40, "class": "animal"},

  #/* --- CATEGORIA: FILMES (ID 41-65) --- */
  {"word": "avatar", "id": 41, "class": "filme"},
  {"word": "coringa", "id": 42, "class": "filme"},
  {"word": "gladiador", "id": 43, "class": "filme"},
  {"word": "matrix", "id": 44, "class": "filme"},
  {"word": "shrek", "id": 45, "class": "filme"},
  {"word": "titanic", "id": 46, "class": "filme"},
  {"word": "frozen", "id": 47, "class": "filme"},
  {"word": "inception", "id": 48, "class": "filme"},
  {"word": "interstellar", "id": 49, "class": "filme"},
  {"word": "jaws", "id": 50, "class": "filme"},
  {"word": "parasita", "id": 51, "class": "filme"},
  {"word": "ratatouille", "id": 52, "class": "filme"},
  {"word": "batman", "id": 53, "class": "filme"},
  {"word": "superman", "id": 54, "class": "filme"},
  {"word": "avengers", "id": 55, "class": "filme"},
  {"word": "starwars", "id": 56, "class": "filme"},
  {"word": "duna", "id": 57, "class": "filme"},
  {"word": "moana", "id": 58, "class": "filme"},
  {"word": "pinocchio", "id": 59, "class": "filme"},
  {"word": "godzilla", "id": 60, "class": "filme"},
  {"word": "rambo", "id": 61, "class": "filme"},
  {"word": "rocky", "id": 62, "class": "filme"},
  {"word": "it", "id": 63, "class": "filme"},
  {"word": "scream", "id": 64, "class": "filme"},
  {"word": "alien", "id": 65, "class": "filme"},

  # /* --- CATEGORIA: PAÍSES (ID 66-90) --- */
  {"word": "brasil", "id": 66, "class": "pais"},
  {"word": "argentina", "id": 67, "class": "pais"},
  {"word": "canada", "id": 68, "class": "pais"},
  {"word": "franca", "id": 69, "class": "pais"},
  {"word": "japao", "id": 70, "class": "pais"},
  {"word": "mexico", "id": 71, "class": "pais"},
  {"word": "portugal", "id": 72, "class": "pais"},
  {"word": "espanha", "id": 73, "class": "pais"},
  {"word": "italia", "id": 74, "class": "pais"},
  {"word": "alemanha", "id": 75, "class": "pais"},
  {"word": "egito", "id": 76, "class": "pais"},
  {"word": "india", "id": 77, "class": "pais"},
  {"word": "china", "id": 78, "class": "pais"},
  {"word": "russia", "id": 79, "class": "pais"},
  {"word": "australia", "id": 80, "class": "pais"},
  {"word": "grecia", "id": 81, "class": "pais"},
  {"word": "turquia", "id": 82, "class": "pais"},
  {"word": "angola", "id": 83, "class": "pais"},
  {"word": "chile", "id": 84, "class": "pais"},
  {"word": "peru", "id": 85, "class": "pais"},
  {"word": "colombia", "id": 86, "class": "pais"},
  {"word": "irlanda", "id": 87, "class": "pais"},
  {"word": "suica", "id": 88, "class": "pais"},
  {"word": "noruega", "id": 89, "class": "pais"},
  {"word": "suécia", "id": 90, "class": "pais"},

  #/* --- CATEGORIA: OBJETOS (ID 91-115) --- */
  {"word": "cadeira", "id": 91, "class": "objeto"},
  {"word": "mesa", "id": 92, "class": "objeto"},
  {"word": "lampada", "id": 93, "class": "objeto"},
  {"word": "computador", "id": 94, "class": "objeto"},
  {"word": "celular", "id": 95, "class": "objeto"},
  {"word": "caderno", "id": 96, "class": "objeto"},
  {"word": "caneta", "id": 97, "class": "objeto"},
  {"word": "espelho", "id": 98, "class": "objeto"},
  {"word": "janela", "id": 99, "class": "objeto"},
  {"word": "relogio", "id": 100, "class": "objeto"},
  {"word": "martelo", "id": 101, "class": "objeto"},
  {"word": "escada", "id": 102, "class": "objeto"},
  {"word": "garrafa", "id": 103, "class": "objeto"},
  {"word": "mochila", "id": 104, "class": "objeto"},
  {"word": "travesseiro", "id": 105, "class": "objeto"},
  {"word": "tesoura", "id": 106, "class": "objeto"},
  {"word": "chave", "id": 107, "class": "objeto"},
  {"word": "oculos", "id": 108, "class": "objeto"},
  {"word": "carteira", "id": 109, "class": "objeto"},
  {"word": "bicicleta", "id": 110, "class": "objeto"},
  {"word": "ventilador", "id": 111, "class": "objeto"},
  {"word": "televisao", "id": 112, "class": "objeto"},
  {"word": "sapato", "id": 113, "class": "objeto"},
  {"word": "camisa", "id": 114, "class": "objeto"},
  {"word": "colher", "id": 115, "class": "objeto"}]

def get_random_word(mainDict):
    rannum = random.randint(0, len(mainDict) - 1)
    return mainDict[rannum]

def game():
    secret_word = get_random_word(mainDict)
    tries = 5
    guess_words_set = set()
    
    while True:
        print("A palavra secreta tem", len(secret_word["word"]), "letras.")
        print("A Categoria è:", secret_word["class"])
        print("Você tem", tries, "tentativas restantes.")
        guess = input("\nDigite uma letra: ").lower()
        if guess in guess_words_set:
            print("Você já tentou essa letra. Tente outra.")
        else:
            guess_words_set.add(guess)
            if guess in secret_word["word"]:
                print("\nAcertou uma letra!")
            else:
                    tries -= 1
                    print("Errou! Tentativas restantes:", tries)
game()
        
       
