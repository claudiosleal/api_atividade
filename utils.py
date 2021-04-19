from models import Pessoas

#Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Galleani', idade=25)
    print(pessoa)
    pessoa.save()

#Realiza consulta dados na tabela pessoas
def consulta_pessoas():
    pessoa = Pessoas.query.all()
    print(pessoa)
    pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    print(pessoa.idade)

#Altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Galleani').first()
    pessoa.nome = 'Felipe'
    pessoa.save()

#Exclui dados na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Galleani').first()
    pessoa.delete()

if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoa()
    exclui_pessoa()
    consulta_pessoas()