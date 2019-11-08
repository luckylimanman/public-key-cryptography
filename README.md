# public-key-cryptography
**任意字符可以被加密解密**
**cli.py is the main file**

## How to generate keys:
```
python3 cli.py -k <key name>
```
## How to encrypt a plaintext：
```
python3 cli.py -en <plaintext> -pu <public key>
```
## How to decrypt a ciphertext:
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
>python3 cli.py -en 肖战可爱 -pu '40093&390787'
>```
> **results:**
>```
>ciphertext is 226721026509029344138819
>```

> **Decrypt a number:**
>```
>python3 cli.py -de 226721026509029344138819 -pr '161093&390787'
>```
> **results:**
>```
>plaintext is 肖战可爱
>```
