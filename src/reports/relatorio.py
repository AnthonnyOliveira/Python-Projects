from db.connection import conexao
from datetime import datetime

def tempo_total_permanencia(aluno_id):
    cursor = conexao.cursor()

    # Busca nome do aluno
    cursor.execute("SELECT nome FROM alunos WHERE id = ?", (aluno_id,))
    aluno = cursor.fetchone()
    if not aluno:
        print("Aluno não encontrado.")
        return

    nome = aluno[0]

    # Busca registros com entrada e saída
    cursor.execute("""
        SELECT entrada, saida FROM registros
        WHERE aluno_id = ? AND saida IS NOT NULL
    """, (aluno_id,))
    registros = cursor.fetchall()

    total_tempo = 0
    for entrada, saida in registros:
        entrada_dt = datetime.fromisoformat(entrada)
        saida_dt = datetime.fromisoformat(saida)
        diferenca = (saida_dt - entrada_dt).total_seconds()
        total_tempo += diferenca

    horas = int(total_tempo // 3600)
    minutos = int((total_tempo % 3600) // 60)

    print(f"⏱️ Tempo total de permanência de {nome}: {horas}h {minutos}min")


def media_tempo_por_aluno(aluno_id):
    cursor = conexao.cursor()

    cursor.execute("SELECT nome FROM alunos WHERE id = ?", (aluno_id,))
    aluno = cursor.fetchone()
    if not aluno:
        print("Aluno não encontrado.")
        return

    nome = aluno[0]

    cursor.execute("""
        SELECT entrada, saida FROM registros
        WHERE aluno_id = ? AND saida IS NOT NULL
    """, (aluno_id,))
    registros = cursor.fetchall()

    if not registros:
        print("Nenhum registro com saída para calcular média.")
        return

    total_tempo = 0
    for entrada, saida in registros:
        entrada_dt = datetime.fromisoformat(entrada)
        saida_dt = datetime.fromisoformat(saida)
        total_tempo += (saida_dt - entrada_dt).total_seconds()

    media = total_tempo / len(registros)
    horas = int(media // 3600)
    minutos = int((media % 3600) // 60)

    print(f"📊 Média de permanência por registro de {nome}: {horas}h {minutos}min")

def media_geral_permanencia():
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT entrada, saida FROM registros
        WHERE saida IS NOT NULL
    """)
    registros = cursor.fetchall()

    if not registros:
        print("Nenhum registro com saída para calcular média geral.")
        return

    total_tempo = 0
    for entrada, saida in registros:
        entrada_dt = datetime.fromisoformat(entrada)
        saida_dt = datetime.fromisoformat(saida)
        total_tempo += (saida_dt - entrada_dt).total_seconds()

    media = total_tempo / len(registros)
    horas = int(media // 3600)
    minutos = int((media % 3600) // 60)

    print(f"📈 Média geral de permanência por registro: {horas}h {minutos}min")

def discrepancia_horario_entrada(aluno_id):
    cursor = conexao.cursor()

    cursor.execute("SELECT nome, horario_previsto FROM alunos WHERE id = ?", (aluno_id,))
    aluno = cursor.fetchone()
    if not aluno:
        print("Aluno não encontrado.")
        return

    nome, horario_previsto = aluno
    horario_previsto_dt = datetime.strptime(horario_previsto, "%H:%M")

    cursor.execute("""
        SELECT entrada FROM registros
        WHERE aluno_id = ? AND saida IS NOT NULL
    """, (aluno_id,))
    registros = cursor.fetchall()

    if not registros:
        print("Nenhuma entrada encontrada.")
        return

    print(f"⏰ Discrepâncias para {nome}:")
    for entrada, in registros:
        entrada_dt = datetime.fromisoformat(entrada)
        horario_real = entrada_dt.time()

        minutos_previstos = horario_previsto_dt.hour * 60 + horario_previsto_dt.minute
        minutos_reais = horario_real.hour * 60 + horario_real.minute

        diferenca = minutos_reais - minutos_previstos
        status = "atrasado" if diferenca > 0 else "adiantado" if diferenca < 0 else "pontual"

        print(f"- {entrada_dt.strftime('%d/%m %H:%M')} → {abs(diferenca)} min {status}")




