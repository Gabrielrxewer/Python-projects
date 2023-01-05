def soma(a, b): return a+b
def mul(a, b, c): return (a+b)*c


r2 = mul(2, 9, 3)
r = soma(2, 5)
print(r)
print(r2)


def v(x, func): return x+func(x)


res = v(2, lambda x: x*x)
print(res)
