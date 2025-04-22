class Aluno:
    def __init__(self, id , nome , dias_frequentados , horario_previsto):
        self.id = id
        self.nome = nome
        self.dias_frequentados = dias_frequentados
        self.horario_previsto = horario_previsto

    def __str__(self):
        return f"Aluno({self.id}, {self.nome}, {self.dias_frequentados}, {self.horario_previsto})"

#aluno1 = Aluno(nome = "alessandra")
#print(aluno1.nome)   
#se fosse adicionar manualmente, seria mais ou menos assim colocando None na frente de todos self, id, nome...
           
        