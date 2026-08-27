import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

# Conexão com o banco de dados SQLite
conn = sqlite3.connect("clientes.db")
cursor = conn.cursor()

# Criação da tabela de clientes, se não existir
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    telefone TEXT NOT NULL
)
"""
)
conn.commit()


# Função para salvar os dados
def salvar_cliente():
  nome = entry_nome.get()
  email = entry_email.get()
  telefone = entry_telefone.get()

  if nome and email and telefone:
    cursor.execute(
        "INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)",
        (nome, email, telefone),
    )
    conn.commit()
    messagebox.showinfo("Sucesso", "Cliente salvo com sucesso!")
    limpar_formulario()
  else:
    messagebox.showwarning(
        "Atenção", "Todos os campos devem ser preenchidos!"
    )


# Função para limpar os campos
def limpar_formulario():
  entry_nome.delete(0, tk.END)
  entry_email.delete(0, tk.END)
  entry_telefone.delete(0, tk.END)


# Função para visualizar clientes cadastrados
def visualizar_clientes():
  janela_visualizacao = tk.Toplevel()
  janela_visualizacao.title("Clientes Cadastrados")

  tree = ttk.Treeview(
      janela_visualizacao,
      columns=("ID", "Nome", "Email", "Telefone"),
      show="headings",
  )
  tree.heading("ID", text="ID")
  tree.heading("Nome", text="Nome")
  tree.heading("Email", text="Email")
  tree.heading("Telefone", text="Telefone")
  tree.pack(fill=tk.BOTH, expand=True)

  cursor.execute("SELECT * FROM clientes")
  for row in cursor.fetchall():
    tree.insert("", tk.END, values=row)


# Janela Principal
janela = tk.Tk()
janela.title("Cadastro de Clientes")

# Rótulos e Entradas
tk.Label(janela, text="Nome:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_nome = tk.Entry(janela, width=30)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

tk.Label(janela, text="Email:").grid(
    row=1, column=0, padx=10, pady=5, sticky="e"
)
entry_email = tk.Entry(janela, width=30)
entry_email.grid(row=1, column=1, padx=10, pady=5)

tk.Label(janela, text="Telefone:").grid(
    row=2, column=0, padx=10, pady=5, sticky="e"
)
entry_telefone = tk.Entry(janela, width=30)
entry_telefone.grid(row=2, column=1, padx=10, pady=5)

# Botões
btn_salvar = tk.Button(janela, text="Salvar", command=salvar_cliente)
btn_salvar.grid(row=3, column=0, pady=10)

btn_limpar = tk.Button(janela, text="Limpar", command=limpar_formulario)
btn_limpar.grid(row=3, column=1, pady=10)

btn_visualizar = tk.Button(
    janela, text="Visualizar Clientes", command=visualizar_clientes
)
btn_visualizar.grid(row=4, column=0, columnspan=2, pady=5)

janela.mainloop()

conn.close()
