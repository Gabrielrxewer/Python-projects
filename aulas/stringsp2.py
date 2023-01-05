curso = "Curso de Python"

res = "Python" in curso  # in // not in
print(res)

cidade = "Mondaí"
dia = 15
mes = "Dezembro"
ano = 2022
data = "{}, {} de {} de {} \n \"{}\""

# \' \" \n \r \t \b

if (res == True):
    print(data.format(cidade, dia, mes, ano, curso))
