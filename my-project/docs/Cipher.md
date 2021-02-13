#Cipher

##Symmetric Encryption
Use `gen_sym_keys()` to gain keys. You can use them to encrypt with `encrypt_sym(text,key)` or decrypt with `decrypt_sym(text,key)`
```` python
from easy_crypt.cipher import cipher_funct as cf
key = cf.gen_keys()
encr = cf.encrypt_sym("I like easy_crypt",key) # Output as bytes
decr = cf.decrypt_sym(encr,key) # Output as str
print(decr) # prints "I like easy_crypt"
````
gen_sym_keys() can take 1 argument:

>`get_sym_keys(bytes=32)`

>:param bytes: (optional) length of the key
> 
>:return: returns key (type: **bytes**)

encrypt_sym() takes 2 arguments:

>`encrypt_sym(text, key)`

>:param text: data that is supposed to be encrypted (type: str, hex or bytes)
> 
>:param key: the key
> 
>:return: returns decrypted data (type: **bytes**)

decrypt_sym() takes 2 arguments:

>`decrypt_sym(text, key)`

>:param text: data that is supposed to be decrypted (type: str, hex or bytes)
> 
>:param key: the key (is the same one as the one used to encrypt)
> 
>:return: returns decrypted data (type: **bytes**)


##Asymmetrical Encryption 
Use `gen_asym_keys()` to gain the private key and public key. You can use the public key to encrypt  
with `encrypt_asym(text,public_key)`and the private key to decrypt with `decrypt_asym(text,private_key)`. Remember, you can only encrypt a <span style="color:red">limited byte size of data</span>.
```` python
from easy_crypt.cipher import cipher_funct as cf
private_key, public_key = cf.gen_asym_keys()
encr = cf.encrypt_asym("Test",public_key)  #The input type must be hex, string or bytes                                       
decr = cf.decrypt_asyn(encr,private_key) # Output as bytes
print(decr.decode('utf-8'))
````

`get_asym_keys()` can take 1 argument:

>`gen_asym_keys(length=2048)`

>:param length: (optional) length of the keys
> 
>:return: returns private key, public key

`encrypt_asym()` takes 2 arguments:

>`encrypt_asym(text, pubkey)`

>:param text: data that is supposed to be encrypted (type: str, hex or bytes)
> 
>:param pubkey: public key
>
>:return: decrypted text (type: **bytes**)

`decrypt_asym()` takes 2 arguments:

>`decrypt_asym(text, prkey)`

>:param text: data that is supposed to be decrypted (type: bytes)
> 
>:param prkey: privat key
> 
>:return: decrypted text (type: **bytes**)

##Combination of Both

A combination results in being ably to encrypt an infinite amount of data and use private and public keys.  
Use `encrypt_data()` to encrypt data and `decrypt_data()` to decrypt data
```` python
from easy_crypt.cipher import cipher_funct as cf
private_key,public_key = cf.gen_asym_keys()
encr = cf.encrypt_data("very long and importan message",public_key) # #The input type must be hex, str or bytes
decr = cf.decrypt_data(encr,private_key) # Output as str
print(decr) #prints "very long and importan message"
````

`encrypt_data()` can take 4 arguments:
>  `encr_data(data, pubkey, bytes=32, output="bytes")`

>
>:param data: the data that is supposed to be decrypted (type: hex, str or bytes)
> 
>:param pubkey: public_key
> 
>:param bytes: (optional) number of bytes of the symmetric key
> 
>:param output: (optional) type of the output (bytes or hex)
>
>:return: returns encrypted data (type: **bytes** or hex)

`decrypt_data()` can take 3 arguments:
>  `decr_data(data, prkey, output="str")`

>:param data: the data that is supposed to be decrypted (type: to str converted hex, hex or bytes)
> 
>:param prkey: private_key
> 
>:param output: (optional) type of the output (bytes, **str**)
> 
>:return: encrypted msg (type: **str**, bytes)
