# ============================================================
# AV3-02/7: Sistema de Gestão de Tarefas e Prazos
# ============================================================

# 1. Entrada de Dados
qtd_tarefas = int(input("Quantas tarefas deseja cadastrar? "))

lista_tarefas = []
for i in range(1, qtd_tarefas + 1):
    nome_tarefa = input(f"Digite a tarefa {i}: ")
    lista_tarefas.append(nome_tarefa)

# 2. Processamento com enumerate() e armazenamento em tuplas
banco_dados_tarefas = []

for id_tarefa, nome_tarefa in enumerate(lista_tarefas, start=1):
    # Lógica de progressão de prazos (ex: Tarefa 1 -> 2 dias, Tarefa 2 -> 4 dias, etc.)
    prazo_dias = id_tarefa * 2
    status = "Pendente"
    
    # Armazena as informações em uma tupla estruturada
    registro_tarefa = (id_tarefa, nome_tarefa, prazo_dias, status)
    banco_dados_tarefas.append(registro_tarefa)

# 3. Saída de Dados e Desempacotamento de Tuplas
print("\n--- RESUMO DO SISTEMA ---")
for id_tarefa, nome_tarefa, prazo_dias, status in banco_dados_tarefas:
    print(f"ID: {id_tarefa} | Tarefa: {nome_tarefa} | Prazo: {prazo_dias} dias | Status: {status}")

print(f"\nTotal de tarefas gerenciadas: {len(banco_dados_tarefas)}")
