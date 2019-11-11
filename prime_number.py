import argparse


p = argparse.ArgumentParser()
p.add_argument("-start", type=int)
p.add_argument("-end", type=int)
args = p.parse_args()
print(args.start, args.end)
prime = []
for i in range(args.start, args.end + 1):
    j = 2
    for j in range(2, i):
        if(i % j == 0):
            break
    else:
        prime.append(i)
print(prime)
