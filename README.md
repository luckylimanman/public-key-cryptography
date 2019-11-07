# public-key-cryptography

**cli.py is the main file**

## How to generate keys:
```
python3 cli.py -k <key name>
```
## How to encrypt a plaintext(only int)：
```
python3 cli.py -en <plaintext> -pu <public key>
```
## How to decrypt a ciphertext(only int):
```
python3 cli.py -en <ciphertext> -pr <private key>
```
## Examples:
**Now we encrypt a number 666 and decrypt it !**
> **generate keys:**
>```
>python3 cli.py -k no.1
>```
> **results:**
>```
>Public key no.1 : '40093&390787'
>Private key no.1 : '161093&390787'
>The maximum number that can be encrypted is 390786 !!!
>```

> **Encrypt a number：**
>```
>python3 cli.py -en 666 -pu '40093&390787'
>```
> **results:**
>```
>ciphertext is 79273
>```

> **Decrypt a number:**
>```
>python3 cli.py -en 79237 -pr '161093&390787'
>```
> **results:**
>```
>plaintext is 666
>```
