#...
#autor: Waldinei Santos Gonçalves
#data: 15/02/2023
#finalidade: cadastro de cliente
#versão: 0.0
#...

print("---------------------------Dados da Viagem------------------------")

veiculo=input("Veículo: ")
kmlitro=int(input("Kilometro por litro: "))                
tipocombustivel=input("Combustível utilizado: ")
valorlitro=float(input("Valor por litro:R$ "))
tempoviagem=float(input("Tempo de viagem (h): "))
velmedia=float(input("Velocidade Média (km): "))

conversaotempo=tempoviagem==0.
distancia=conversaotempo*velmedia
quantlitros=distancia/kmlitro
valorgasto=valorlitro*distancia

print("\n")
print("---------------------------Dados Informados------------------------")
print("Veículo: ",veiculo)
print("Km/l: ",kmlitro,"litros")
print("Tempo de Viagem: ",tempoviagem,"h")
print("Distância: ",distancia,"Km")
print("Quantidade de Combustivel Gasto: ",quantlitros,"l")
print("Valor Gasto:R$ ",valorgasto)




    