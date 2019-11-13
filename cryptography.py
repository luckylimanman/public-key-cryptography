import random


def generate_key(key):
    prime_number = [503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587,
                    593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653,
                    659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739,
                    743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823,
                    827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907,
                    911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991,
                    997]
    prime_number1 = random.choice(prime_number)
    prime_number2 = random.choice(prime_number)
    L = lowest_common_multiple(prime_number1 - 1, prime_number2 - 1)
    a = list(range(2, L))
    random.shuffle(a)
    N = prime_number1 * prime_number2
    for E in a:
        if highest_common_factor(E, L) == 1:
            break
    for D in a:
        if (E * D) % L == 1:
            break
    with open('public_key.txt', 'w') as f:
        f.write(str(E) + "O" + str(N))
    with open('private_key.txt', 'w') as f:
        f.write(str(D) + "O" + str(N))
    return (str(E) + "O" + str(N)), (str(D) + "O" + str(N))


def encryption(plaintext, public_key=None):
    if public_key is None:
        with open('public_key.txt', 'r') as f:
            public_key = f.read()
    for i in range(len(public_key)):
        if public_key[i] == "O":
            N = int(public_key[i + 1:])
            E = int(public_key[:i])
    ciphertext = ''
    j = 0
    encode_plaintext = encoding(plaintext)
    while j < len(encode_plaintext):
        ciphertext = ciphertext + str((int(encode_plaintext[j:j+5]) ** E) % N).zfill(len(str(N)))  # noqa
        j = j + 5
    print("ciphertext is", ciphertext)
    return ciphertext


def decryption(ciphertext):
    with open('private_key.txt', 'r') as f:
        private_key = f.read()
    for i in range(len(private_key)):
        if private_key[i] == "O":
            N = int(private_key[i + 1:])
            D = int(private_key[:i])
    plaintext = ''
    j = 0
    while j < len(ciphertext):
        plaintext = plaintext + str((int(ciphertext[j:j+len(str(N))]) ** D) % N).zfill(5)  # noqa
        j = j + len(str(N))
    print("plaintext is", decoding(plaintext))
    return decoding(plaintext)


def lowest_common_multiple(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lowest_common_multiple = greater
            break
        greater += 1
    return lowest_common_multiple


def highest_common_factor(x, y):
    if x > y:
        smaller = x
    else:
        smaller = y
    for i in range(1, smaller + 1):
        if((x % i == 0) and (y % i == 0)):
            highest_common_factor = i
    return highest_common_factor


# decode x(unicode) to chars
def decoding(x):
    chars = ''
    f = len(x)
    i = 0
    while i < f:
        chars = chars + chr(int(x[i:i+5]))
        i = i + 5
    return chars


# encode x(chars) to unicode
def encoding(x):
    s = ''
    for i in x:
        s = s + str(ord(i)).zfill(5)
    return s
