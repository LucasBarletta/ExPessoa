class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf



class Paciente(Pessoa):
    def __init__(self, nome, cpf, sintoma):
        super().__init__(nome, cpf)
        self.sintoma = sintoma


        print(nome,cpf,sintoma)

class Medico(Pessoa):

    def __init__(self, nome, cpf, crm):
        super().__init__(nome, cpf)
        self.crm = crm


        print(nome, cpf,crm)

paciente = Paciente('Joao','123456789', 'gripe')
medico = Medico('Jose', '98765413', 'crm')
