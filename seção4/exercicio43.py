total= float(input("Digite o valor total a se pagar: "))
avista=total-(total*10/100)
print("Pagamento avista:",round(avista,2),
"\nParcelas em 3x:",round(total/3,2),
"\nComissão avista: ",round(avista*5/100,2),
"\nComissão parcelada: ",round(total*5/100,2))