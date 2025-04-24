#declaração das variaveis 
conta = int(input("Digite o número da conta: "))
saldo = float(input("Digite o saldo da conta: "))
debito = float(input("Digite o debito da conta: "))
credito = float(input("Digite o crédito da conta: "))

#calculando o saldo atual
saldoatual = saldo - debito + credito 

#caso seja positivo
if saldoatual >= 0:
    print("Saldo positivo.")

#caso contrario
else:
    print("Saldo negativo.")
