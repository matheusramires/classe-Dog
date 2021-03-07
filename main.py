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
dog1 = Dog('nome_do_dog_1', 'cor_do_dog_1', 'raca_do_dog_1')
dog2 = Dog('nome_do_dog_2', 'cor_do_dog_2', 'raca_do_dog_2')
#quantos dogs forem necessarios

#chama cada parametro para o dog 1
dog1.latir()
dog1.chorar()
dog1.correr()
dog1.sentar()
dog1.deitar()
dog1.rolar()

#chama cada parametro para o dog 2
dog2.latir()
dog2.chorar()
dog2.correr()
dog2.sentar()
dog2.deitar()
dog2.rolar()
