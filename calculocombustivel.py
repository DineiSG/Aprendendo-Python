#...
#autor: Waldinei Santos Gonçalves
#data: 24/02/2023
#finalidade: Calculo de Combustivel
#versão: 0.0
#...

print("---------------------------Dados da Viagem------------------------")

veiculo=input("Veículo: ")
kmlitro=int(input("Km/l: "))                
tipocombustivel=input("Combustível utilizado: ")
valorlitro=float(input("Valor por litro:R$ "))
tempoviagem=float(input("Tempo de viagem (h): "))
velmedia=float(input("Velocidade Média (km): "))


conversaotempo=tempoviagem*0.60
distancia=conversaotempo*velmedia
quantlitros=distancia/kmlitro
valorgasto=distancia/kmlitro*valorlitro

print("\n")
print("---------------------------Dados Informados------------------------")
print("Veículo: ",veiculo)
print("Km/l: ",kmlitro,"litros")
print("Tempo de Viagem: ",tempoviagem,"h")
print("Distância Percorrida: ",distancia,"Km")
print("Quantidade de Combustivel Gasto (l):  ",("%4.3f " % quantlitros))
print("Valor Gasto:R$ ",("%4.2f " % valorgasto))




    