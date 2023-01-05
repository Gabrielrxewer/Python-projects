valores = [1, 6, 3, 2]


def somar(num):
    r = 0
    for n in num:
        r += n
    return r


def valores1(num):
    for z in num:
        print(z)


valores1(valores)
print(somar(valores))
