from demoproj.comm.dec_inc import increase


def mul_increase(x):
    y = increase(x)
    return increase(y)