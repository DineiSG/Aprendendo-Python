print("_______________Informe a Temperatura em Celsius_____________")
tempC=float(input("Temperatura C:"))
print("\n")
print("_______________Informe a Temperatura em Farenheit_____________")
tempF=float(input("Temperatura em F:"))


convF=(tempC*9/5)+32
convC=(tempF-32)*5/9

print("A temperatura em Farenheit é: ",("%4.2f " % convF))
print("\n")
print("A temperatura em Celsius é: ",("%4.2f " % convC))
