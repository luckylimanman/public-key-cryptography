import argparse
import cryptography


parser = argparse.ArgumentParser()
parser.description = 'public-key cryptography'
parser.add_argument("-k")
parser.add_argument("-en", type=int)
parser.add_argument("-de", type=int)
parser.add_argument("-pu")
parser.add_argument("-pr")
args = parser.parse_args()
if args.k:
    cryptography.pro(args.k)
if args.en and args.pu:
    cryptography.encryption(args.en, args.pu)
if args.de and args.pr:
    cryptography.decryption(args.de, args.pr)
