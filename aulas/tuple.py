t_carros = ("HRV", "GOLF", "ARGO")
l_carros = list(t_carros)
l_carros[2] = "Focus"
t_carros = tuple(l_carros)

for x in t_carros:  
    print(x)
