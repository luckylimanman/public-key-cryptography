def deco(x):

    chars = ''
    f = len(x)
    i = 0
    while i < f:
        chars = chars + chr(int(x[i:i+5]))
        i = i + 5
    return chars
