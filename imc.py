#...
#autor: Waldinei Santos Gonçalves
#data: 15/02/2023
#finalidade: calculo do imc de uma pessoa
#versão: 0.0
#...

print("Seja Bem vindo!!")
nome=input("Informe seu nome: ")
idade=int(input("Informe a sua idade: "))
peso=float(input("Informe seu peso: "))
altura=float(input("Informe a sua altura: "))
imc=peso//(altura*altura)

print("\n")
print("Nome: ",nome)
print("Idade: ",idade)
print("Altura: ",altura)
print("Seu IMC é de: ", imc)
