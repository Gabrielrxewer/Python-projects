print('Calculadora de Bhaskara')
print('Formula: Ax² + Bx + C = 0')
while True:
    print('Digite um número')
    a1 = input('Digite o A:')
    try:
        a1 = float(a1)
    except ValueError:
        print("Não é número, Digite somente números.")
    if type(a1) == float:
        break
while True:
    print('Digite um número')
    b1 = input('Digite o B:')
    try:
        b1 = float(b1)
    except ValueError:
        print("Não é número, Digite somente números.")
    if type(b1) == float:
        break
while True:
    print('Digite um número')
    c1 = input('Digite o C:')
    try:
        c1 = float(c1)
    except ValueError:
        print("Não é número, Digite somente números.")
    if type(c1) == float:
        break
a = float(a1)
b = float(b1)
c = float(c1)
delta = b**2 - 4*a*c
raiz = delta ** (1/2)
x1 = (-b+raiz)/(2*a)
x2 = (-b-raiz)/(2*a)
if delta < 0:
    exit('Delta negativo, Bhaskara sem solução')
if x1 == x2:
    exit(f'X1 e X2 são iguais. Resultado X = {x1}')
if x1 != x2:
    exit(f'X1= {x1} X2= {x2}')
