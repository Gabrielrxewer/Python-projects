num = "Gabriel"

if not type(num) is int:
    raise Exception("Apenas números são permitidos!")
else:
    print(str(num))

#try: 
#    print(x)
#except: 
#    print("Erro")
#else:
#    print("Tudo certo")
#finally:
#    print("Fim do tratamento!")