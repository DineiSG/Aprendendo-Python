#...
#autor: Waldinei Santos Gonçalves
#data: 15/02/2023
#finalidade: cadastro de cliente
#versão: 0.0
#...


print ("Por favor informe os dados do cliente")
nome=input("Nome:")
email=input("Email:")
senha=input("Senha:")
confirmesenha=input("Confirme a senha: ")
while confirmesenha != senha:
    breakpoint
endereco=input("Endereco:")
cidade=input("Cidade:")
estado=input("Estado:")
cep=input("CEP:") 
print("\n")

print("---------------------------------------------------------------------")

print("Favor confirmar os dados informados")
print("\n")
print("Nome: ", nome)
print("Email: ", email)
print("Senha: ", senha)
print("Endereco: ", endereco,"/""Cidade: ",cidade,"/""Estado: ",estado,"/""CEP: ",cep)
print("\n")

print("---------------------------------------------------------------------")


print("Os dados estão corretos ?")
confirmação=input("")

print("\n")

print("---------------------------------------------------------------------")

if confirmação =="sim" :
    print("Cadastro realizado com sucesso. O login do cliente será o e-mail fornecido.  ")
else:
    print("Favor informar os dados corretamente")
    

       