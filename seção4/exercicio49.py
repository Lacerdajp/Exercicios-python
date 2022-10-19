from operator import indexOf


isP=False
while isP==False:
    tempoInicial=input("Digite o tempo inicial em h:m:s (ex:10:20:30) : ")[0:8]
    isP=True
    if tempoInicial.count(":")!=2:
        isP=False
        print("Por Favor Digite o Padrão pedido")
    tempoInicial=tempoInicial.split(":")
    tempoInicial=[int(val) for val in tempoInicial]
    if ((tempoInicial[0]<0)or(tempoInicial[0]>23)
    or (tempoInicial[1]<0)or(tempoInicial[1]>=60)
    or (tempoInicial[1]<0)or(tempoInicial[1]>=60)
    ):
        isP=False
        print("Por Favor Digite horarios reais")
seg=int(input("Digite o tempo de espera em segundos:"))
horas=int((seg/60)/60)
minutos=int((seg/60)%60)
seg=int((seg%60)%60)
espera=list([horas,minutos,seg])
tempoFinal=list([])
for val in range(0,3):
    tempoFinal.append(tempoInicial[val]+espera[val])
if tempoFinal[2]>=60:
    tempoFinal[1]=tempoFinal[1]+int(tempoFinal[2]/60)
    tempoFinal[2]=tempoFinal[2]%60
if tempoFinal[1]>=60:
    tempoFinal[0]=tempoFinal[0]+int(tempoFinal[1]/60)
    tempoFinal[1]=tempoFinal[1]%60
if tempoFinal[0]>=24:
    tempoFinal[0]=tempoFinal[0]-24

print(tempoFinal[0],"h",tempoFinal[1],"m",tempoFinal[2],"s")