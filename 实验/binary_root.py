import math

def binary_root(a, b, prec, fx):
    fa = fx.replace('x','a')
    print('%.4f' %a, '%.4f' %b, end=' ')
    x = (a + b) / 2
    print('%.4f' %x)

    while b - a > prec:
        if eval(fx) * eval(fa) > 0:
            a = x
            x = (a + b) / 2
            print('%.4f' %a, "      ", '%.4f' %x)

        elif eval(fx) * eval(fa) < 0:
            b = x
            x = (a + b) / 2
            print("      ",'%.4f' %b , '%.4f' %x)

        else:
            break

if __name__ == '__main__':
    a = 1.0
    b = 1.5
    prec = 0.005
    fx = "x*x*x-x-1"
    binary_root(a, b, prec, fx)