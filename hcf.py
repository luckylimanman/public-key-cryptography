def hcf(E, L):
    if E > L:
        smaller = E
    else:
        smaller = L
    for i in range(1, smaller + 1):
        if((E % i == 0) and (L % i == 0)):
            hcf = i
    return hcf
