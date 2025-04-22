class Registros:
    def __init__(self, id, aluno_id, entrada, saida):
        self.id = id
        self.aluno_id = aluno_id
        self.entrada = entrada
        self.saida = saida

    def __str__(self):
        return f"Registros({self.id}, {self.aluno}, {self.entrada}, {self.saida})"
    
    