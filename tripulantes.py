
import random

numeros = {}

def gerar(numeros):
    cod = random.randint(1,256)
    if cod in numeros.keys():
       return  gerar(numeros)
    return cod

class Tripulantes:
    def __init__(self, nome, idade, cod):
        self.nome = nome
        self.idade = idade
        self.cod = cod

    def __str__(self) -> str:
        return f"\nNome: {self.nome},\nIdade: {self.idade},\nCodigo: {self.cod}"


i=10
while(i != 0):

    print("\nDigite 1 para inserir seus dados: ")
    print("Digite 2 para acessar sues dados: ")
    print("Digite 0 para finalizar: ")
    i = int(input("O que deseja realizar? "))
    
    

    if i == 1:
        if len(numeros) <= 50:
            nome = input("\nNome: ")
            idade  = input("Idade: ")
            cod = gerar(numeros)
            print('Código:', cod )
            pessoa = Tripulantes(nome, int(idade), cod)
            numeros[cod] = pessoa
        else:
            print("Esgotado")

    if i == 2:
        cod = int(input('\nCódigo: '))
        if cod in numeros:
            pessoa = numeros[cod]
            print(pessoa)
        else:
            print("\nCódigo não existe.")

