# Impressão configurada com separador " "
subst = "Python" 
verbo = "é" 
adjetivo = "fantástico" print(subst, verbo, adjetivo, sep="_", end="!\n") 

#Mostra o tipo de variável
preco = 49.99 
type(preco) 

# Soma impossível de inteiro e string 
idade1 = "10"
idade2 = "20" 
print(idade1 + idade2,"a soma as idades em numero é",int(idade1)+int(idade2), sep=" ")

# Soma possível após conversão de string para inteiro
idade1 = 10 
idade2 = int("20") 
print(idade1 + idade2)

# Concatenação de strings
nome = "Nico" 
sobrenome = "Steppat" 
print("nome do usuario é", nome, sobrenome, sep=" ") 
