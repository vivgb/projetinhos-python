#declaração de variaveis
sal = float(input("Digite o salário fixo: R$ "))
venda = float(input("Digite o valor das vendas: R$"))

#caso seja menor ou igual a 1500 reais 
if sal <=1500:
    comissao = 0.03 * venda

    #caso ultrapasse o valor
else:
    comissao1500 = 1500 * 0.03
    comissaoextra = (venda - 1500) * 0.05
    comissao = comissao1500 + comissaoextra

#salário total
saltotal = sal + comissao

#saída do total
print("O salário total do vendedor é: ", saltotal)

