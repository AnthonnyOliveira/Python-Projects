from db.connection import conexao
from datetime import datetime

def registrar_entrada(aluno_id):
    entrada = datetime.now()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO registros (aluno_id, entrada)
        VALUES (?, ?)
    """, (aluno_id, entrada))
    conexao.commit()
    print("Entrada registrada com sucesso!")

def registrar_saida(aluno_id):
    saida = datetime.now()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT id FROM registros
        WHERE aluno_id = ? AND saida IS NULL
        ORDER BY entrada DESC  
        LIMIT 1
    """, (aluno_id,))
    registro = cursor.fetchone() 
#ORDER BY entrada: ordena pelos horários de entrada.
#DESC (de descending): ordem decrescente, ou seja, da última entrada registrada para a mais antiga.

    if registro:
        cursor.execute("""
            UPDATE registros
            SET saida = ?
            WHERE id = ?
        """, (saida, registro[0]))
        conexao.commit()
        print("Saída registrada com sucesso!")
    else:
        print("Nenhuma entrada encontrada para este aluno ou saída já registrada.")

def historico_registros(aluno_id):
    cursor = conexao.cursor
    cursor.execute("""
        SELECT entrada, saida FROM registros 
        WHERE aluno_id = ?
        ORDER BY entrada DESC
    """, (aluno_id,)) #passando o aluno_id como parâmetro de segurança
    registros = cursor.fetchall()

    for r in registros:
        entrada_formatada = datetime.fromisoformat(r[0]).strftime('%d/%m/%Y %H:%M')
        saida_formatada = datetime.fromisoformat(r[1]).strftime('%d/%m/%Y %H:%M') if r[1] else "Ainda na academia"
        print(f"Entrada: {entrada_formatada}  Saída: {saida_formatada}")

#    if registros:  um jeito que fiz
#      for r in registros:
#           print(f"Entrada:{r[0]} e Saída: {r[1]}")
#    else:
#           print("Nenhum registro foi encontrado.")