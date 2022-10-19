seg=int(input("Digite o tempo em segundos:"))
horas=int((seg/60)/60)
minutos=int((seg/60)%60)
seg=(seg%60)%60
print(horas,"h",minutos,"m",seg,"s")