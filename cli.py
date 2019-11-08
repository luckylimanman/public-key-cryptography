import argparse
import cryptography


parser = argparse.ArgumentParser()
parser.description = 'public-key cryptography'
parser.add_argument("-k")
parser.add_argument("-en")
parser.add_argument("-de")
args = parser.parse_args()
if args.k:
    cryptography.pro(args.k)
if args.en:
    cryptography.encryption(args.en)
if args.de:
    cryptography.decryption(args.de)
