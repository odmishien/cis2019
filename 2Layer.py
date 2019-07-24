# 例えば今回は
# y = 5x + 3 を2層のネットワークで解いてみる
def t(x):
    return 5 * x + 3

def f(x):
    return x

def df(x):
    return 1

def u(a, x, b):
    return a * x + b

def y(u):
    return f(u)

a_1, b_1, a_2, b_2 = 1, 1, 1, 1
LOOP = 10000
ALPHA = 0.0001

data = [2, 5, 8]

for i in range(LOOP):
    da_1, db_1, da_2, db_2 = 0, 0, 0, 0
    for d in data:
        uu_1 = u(a_1, d, b_1)
        yy_1 = y(uu_1)
        uu_2 = u(a_2, yy_1, b_2)
        yy_2 = y(uu_2)
        pa_2 = (yy_2 - t(d)) * df(uu_2) * yy_1
        pb_2 = (yy_2 - t(d)) * df(uu_2)
        da_2 += pa_2
        db_2 += pb_2
        pa_1 = (yy_2 - t(d)) * df(uu_2) * a_2 * df(uu_1) * d
        pb_1 = (yy_2 - t(d)) * df(uu_2) * a_2 * df(uu_1)
        da_1 += pa_1
        db_1 += pb_1
    a_1 -= ALPHA * da_1
    b_1 -= ALPHA * db_1
    a_2 -= ALPHA * da_2
    b_2 -= ALPHA * db_2

print(a_1*a_2, a_2*b_1+b_2)
