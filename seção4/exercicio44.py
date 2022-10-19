degrau= float(input("Digite a altura do degrau: "))
alturaDesejada= float(input("Digite a altura desejada: "))
qtd=int(alturaDesejada/degrau)
if(qtd*degrau<alturaDesejada): 
    qtd=qtd+1
print("O numero de degraus que a escade deve ter é: ",qtd)