salario=30.00
dias=int(input("Digite o numero de dias trabalhados: "))
salario=(salario*dias)-(salario*dias*8/100)
print("O salario Liquido do funcionario é :",round(salario,2),"reais")