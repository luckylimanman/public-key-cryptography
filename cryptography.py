import random
from lcm import lcm
from hcf import hcf


def pro(key):
    prime = [503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
    prim1 = random.choice(prime)
    prim2 = random.choice(prime)
    L = lcm(prim1 - 1, prim2 - 1)
    a = list(range(2, L))
    random.shuffle(a)
    N = prim1 * prim2
    for E in a:
        if hcf(E, L) == 1:
            break
    for D in a:
        if (E * D) % L == 1:
            break
    print("Public key", key, ":", "\'" + str(E) + "&" + str(N) + "\'")
    print("Private key", key, ":", "\'" + str(D) + "&" + str(N) + "\'")
    print("The maximum number that can be encrypted is", N - 1, "!!!")


def encryption(pla, pu):
    for i in range(len(pu)):
        if pu[i] == "&":
            N = int(pu[i + 1:])
            E = int(pu[:i])
    cip = (pla ** E) % N
    print("ciphertext is", cip)


def decryption(cip, pr):
    for i in range(len(pr)):
        if pr[i] == "&":
            N = int(pr[i + 1:])
            D = int(pr[:i])
    pla = (cip ** D) % N
    print("plaintext is", pla)
