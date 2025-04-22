import sqlite3 #importando o SQLite 


conexao = sqlite3.connect("academia.db")
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE aluno(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    dias_frequentados TEXT NOT NULL,
    horario_previsto TEXT NOT NULL
);
""")

cursor.execute("""
    CREATE TABLE registros(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    aluno_id INTEGER NOT NULL,
    entrada DATETIME,
    saida DATETIME,
    FOREIGN KEY (aluno_id) REFERENCES aluno(id)
);
""")

#Salvando 
conexao.commit()

#fechando o banco de dados 
conexao.close()

print("Criado com sucesso.")






