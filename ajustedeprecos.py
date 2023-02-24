#...
#autor: Waldinei Santos Gonçalves
#data: 24/02/2023
#finalidade: Sistema de Ajuste de Preco
#versão: 0.0
#...

print("___________________________Sistema de Ajuste de Preços_____________________________")
print("___________________________________________________________________________________")

precocusto=float(input("Informe o preco de custo: R$ "))
precovenda=(precocusto*33/100) + precocusto
precogov=precovenda-precovenda*15/100
lucroreal=precogov-precocusto


print("______________________________Relatório do Produto____________________________________")
print("______________________________________________________________________________________")
print("\n")
print("Preço de custo: R$",("%4.2f " % precocusto))
print("Preco de Venda: R$",("%4.2f " % precovenda))
print("Percentual de lucro encima do valor de custo: 33%")
print("Percentual de desconto exigido pelo governo encima do valor de custo: 15% ")
print("Preco Tabelado: R$",("%4.2f " % precogov))
print("Lucro real: R$",("%4.2f " % lucroreal))