#...
#autor: Waldinei Santos Gonçalves
#data: 15/02/2023
#finalidade: cadastro de funcionario
#versão: 0.0
#...


print("________________________________Informe os dados do novo colaborador________________________________")
print("\n")

nomecompleto=input("Nome Completo: ")
funcao=input("Funçao: ")
setor=input("Setor: ")
valorhoratecnica=float(input("Valor da hora R$: "))
insa=int(input("Valor Adicional Insalubridade (%): "))
peric=int(input("Valor Adicional Periculosidade (%): "))

print("\n")


#informaçoes adicionais para salario

jornadasemanal:int=40
semanasmes:int=4
auxalimdiar:float=75.0*20
auxtransp:float=59.0*20

#condicionando a adição de insalubridade e periculosidade

insalubridade=valorhoratecnica*insa/100 
if insa == 30:
    insalubridade + valorhoratecnica
    
periculosidade=valorhoratecnica*peric/100 
if insa == 20:
    periculosidade + + valorhoratecnica
    
#calculo salario
    
salario=valorhoratecnica+insalubridade+periculosidade
calcsal=salario*jornadasemanal*semanasmes

#informando dados do colaborador

print("____________________________________________Dados do Colaborador_______________________________________")
print("Nome Completo",nomecompleto)
print("Função: ",funcao)
print("Setor: ",setor)
print("Adicional Insalubridade: ",("%4.2f " % insalubridade))
print("Adicional Periculosidade: ", ("%4.2f " % periculosidade))
print("Auxílio Alimentação:R$ ",("%4.2f " % auxalimdiar))
print("Vale Transporte: R$ ",("%4.2f " % auxtransp))
print("Salário Mensal:R$ ",("%4.2f " % calcsal))




    
 


