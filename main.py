# cria class Dog
class Dog():
    def __init__(self,nome,cor,raca):
        self.nome = nome
        self.cor =cor
        self.raca = raca
    def latir(self):
        print (str(self.nome).title() + ' latindo.')
    def chorar(self):
        print(str(self.nome).title() + ' chorando.')
    def correr(self):
        print(str(self.nome).title() + ' correndo.')
    def sentar(self):
        print(str(self.nome).title() + 'sentado.')
    def deitar(self):
        print(str(self.nome).title() + 'deitado.')
    def rolar(self):
        print(str(self.nome).title() + 'rolando')

#instancia um objeto
dog1 = Dog('luna', 'preta', 'labrador')

#chama cada parametro
dog1.latir()
dog1.chorar()
dog1.correr()
dog1.sentar()
dog1.deitar()
dog1.rolar()