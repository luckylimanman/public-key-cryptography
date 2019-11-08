def enco(x):

    s = ''
    for i in x:
        s = s + str(ord(i)).zfill(5)
    return s
