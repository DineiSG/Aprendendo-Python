#...
#autor: Waldinei Santos Gonçalves
#data: 24/02/2023
#finalidade: Calculo de Faturamento
#versão: 0.0
#...



print("_______________________________Controle de Faturamento___________________________")
print("\n")
qntveiculos=int(input("Informe a quantidade de veículos: "))

#Calculo de Ganho Anual
valoraluguelmes=1500
quant_veic_loc=qntveiculos/3
fat_anual=quant_veic_loc*valoraluguelmes*12

#Calculo de Multas
valormulta=valoraluguelmes*10/100+valoraluguelmes
devol_atrasadas=quant_veic_loc/10
ganhomultas=valormulta*devol_atrasadas

#Calculo de Estoque
veicdanif=qntveiculos*2/100
compreposicao=qntveiculos/10
qnt_veic_final=qntveiculos-veicdanif+compreposicao

print("_______________________________Faturamento  Anual_________________________________")
print("\n")
print("Quantidade de Locações por Mes: ",("%4.0f" %quant_veic_loc))
print("Quantidade de Veículos em Estoque ao Fim do Ano: ",int(qnt_veic_final))
print("Veículos Devolvidos com Atraso por Mes:",("%4.0f" %devol_atrasadas))
print("Lucro com Multas por Atrasos Por Mês:R$",float(ganhomultas))
print("Faturamento Anual:R$",float(fat_anual))
