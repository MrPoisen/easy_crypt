

This is a simple library. You can use it to hash, encrypt and decrypt data. It allows easy use of the [pychryptodome](https://pypi.org/project/pycryptodome/) library.

You can securely encrypt any msg of any length with encrypt_data(text,public_key). It uses asymmetric and symmetric encryption:
``` python
from easycrypt.cipher.cypherfunct import encrypt_data,decrypt_data,gen_asym_keys

private_key,public_key = gen_asym_keys()
msg = "Hello World"
encrypted_msg = encrypt_data(msg,public_key) # output in bytes
#Now it is encrypted
decrypted_msg = decrypt_data(encrypted_msg, private_key) # output in bytes
print(decrypted_msg) # prints "Hello World"
```
And of course decrypt it.

If you want to store passwords securely, you can use the gen_hash(text) function to create and the compare_hash(text,hash) to compare them
``` python
from easycrypt.hash.hash_funct import gen_hash, compare_hash
pw = "Hello Hash"
hash = gen_hash(pw) #output in hex
to_compare = "Hello Hash"
print(compare_hash(pw,hash)) # prints "True"; The output is a boolean
```

You can use old ciphers too, like Vigener or Caesar. More are being added.  
For cryptographically secure encryption/decryption use `easy_crypt.cipher.cypher_funct`