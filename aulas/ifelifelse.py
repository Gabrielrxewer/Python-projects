clima = "sol"
lugar = ""
dinheiro = 399

if clima == "sol" and (dinheiro > 300 and dinheiro < 650):
    lugar = "clube"
else:
    lugar = "cinema"

print("Porque está fazendo "+clima + " eu vou ao "+lugar)

# AND
# V V = V
# V F = F
# F V = F
# F F = F

# OR
# V V = V
# V F = V
# F V = V
# F F = F
