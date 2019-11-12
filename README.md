# public-key-cryptography

**任意字符可以被加密解密**

**cli.py is the main file**

## 如何产生密钥:
```
python3 cli.py -k <key name>
```
## 如何加密明文：
```
python3 cli.py -en <plaintext>
or
python3 cli.py -en <plaintext> -pu <public key>  
```
## 如何解密密文:
```
python3 cli.py -en <ciphertext>
```
## Examples:
**现在加密明文 “肖战可爱” 并且解密它 !**
> **产生密钥:**
>```
>python3 cli.py -k no.1
>```
> **运行结果:**
>```
>Public key no.1 : '40093&390787'
>Private key no.1 : '161093&390787'
>```

> **加密明文：**
>```
>python3 cli.py -en 肖战可爱
>```
> **运行结果:**
>```
>ciphertext is 226721026509029344138819
>```

> **解密密文:**
>```
>python3 cli.py -de 226721026509029344138819
>```
> **运行结果:**
>```
>plaintext is 肖战可爱
>```
