import sqlite3
from db.connection import conexao

def adicionar_aluno(id, nome, dias_frequentados, horario_previsto): #definindo uma função com parâmetros
    cursor = conexao.cursor() #criando um um objeto que é responsável pela execução do sql no banco de dados
    cursor.execute("""
    INSERT INTO aluno(nome, dias_frequentados, horario_frequentado) 
    VALUES (?, ?, ?)""", (nome, dias_frequentados, horario_previsto))
    conexao.commit()
    print(f"Aluno {nome} cadastrado!")
#função de buscar o aluno pelo id
def buscar_aluno(id):
    cursor = conexao.cursor()
    cursor.execute("""
    SELECT * FROM aluno Where id = ?""", (id,))
    aluno = cursor.fetchone()
   
    #se no id achar algum aluno, mostrara o aluno, caso contrário uma mensagem negando
    if aluno:
        print(f"Aluno encontrado: {aluno}")
        return aluno
    else:
        print("Aluno não encontrado")
        return None

def listar_aluno(): #não precisa de parametros pq vamos pegar todos.
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM aluno")
    alunos = cursor.fetchall()

    if alunos:
        for aluno in alunos:
            print(aluno)
        return aluno
    else:
        print("Nenhum aluno encontrado")
        return []

    




