import datetime

date = datetime.datetime.now()
nasc = datetime.datetime(2003,12,31)

print(str(date.day) + "/" + str(date.month) + "/" + str(date.year))
print(str(nasc.strftime("%A")))

# Guia do strftime
#%a = texto dia da semana abreviado
#%A = texto dia da semana 
#%w = num dia da semana
#%d = num dia do mês
#%b = texto mês abreviado
#%B = texto mês
#%m = num do mÊs
#%y = ano com dois digitos
#%Y = ano com quatro digitos
#%H = 00 - 23
#%I = 00 - 12
#%p = AM / PM
#%M = minutos
#%S = segundos
#%f = milisegundos
#%j = dia do ano 365
#%W = numero da semana do ano