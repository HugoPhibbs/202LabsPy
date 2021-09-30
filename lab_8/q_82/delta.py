from heaviside import heaviside as hs

def delta(a, t0, t):
    return (1 / a) * (hs(t, t0) - hs(t, t0+a))


