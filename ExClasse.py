class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

        print(nome,cpf)

class Paciente(Pessoa):
    def __init__(self, nome, cpf, sintoma):
        super().__init__(nome, cpf)
        self.sintoma = sintoma

    def sintoma(self):
        print('Gripe')

class Medico(Pessoa):

    def __init__(self, nome, cpf, crm):
        super().__init__(nome, cpf)
        self.crm = crm

    def crm(self):
        print('Numero crm')

paciente = Paciente('Joao','123456789', 'gripe')
medico = Medico('Jose', '98765413', 'crm')
pessoa = Pessoa('nome', 'cpf')

print(paciente.sintoma)
print(medico.crm)