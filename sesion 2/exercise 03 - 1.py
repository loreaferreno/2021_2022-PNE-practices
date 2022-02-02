# --- Find the error!
#t1 would be zero!!!!

def g(a, b):
    return a - b


def f(a, b, c, d):
    t0 = a + b - g(a, 0)
    t1 = g(c, d)
    try:
        t3 = 2 * (t0 / t1)
        return t0 + 2*t1 + t3*t3
    except ZeroDivisionError:
        return "Cannot calculate with those values"
