salario=float(input("Digite o salario por dia do funcionario: "))
dias=int(input("Digite o numero de dias trabalhados: "))
salario=(salario*dias)+(salario*dias*10/100)
print("O salario Liquido do funcionario é :",round(salario,2),"reais")