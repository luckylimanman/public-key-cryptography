import argparse
import cryptography


parser = argparse.ArgumentParser()
parser.description = ' before encryption or decryption should generates keys'
parser.add_argument("-k", help="usage:[python3 cli.py -k key-name]")
parser.add_argument("-en", help="usage:[python3 cli.py -en plaintext]")
parser.add_argument("-pu", help="usage:[python3 cli.py -en plaintext -pu public key]")
parser.add_argument("-de", help="usage:[python3 cli.py -en ciphertext]")
args = parser.parse_args()
if args.k:
    cryptography.generate_key(args.k)
elif args.en and args.pu:
    cryptography.encryption(args.en, args.pu)
elif args.en:
    cryptography.encryption(args.en)
elif args.de:
    cryptography.decryption(args.de)
else:
    raise NameError
