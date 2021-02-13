#Hash

## Generating a Hash
Use the `gen-hash()` function to create a hash. The input type should be bytes or str.
``` python
from easycrypt.hash.hash_funct import gen_hash
pw = "Test"
hash = gen_hash(pw) #output in hex
```
The `gen_hash()` function can take 5 arguments: 

>`gen_hash(text, predefined_salt=None, hash_type='sha512', iterations=100000, data_type='hex')`

>:param text: the text that is supposed to be hashed (type: bytes, bytearray, str or hex)
> 
>:param predefined_salt: (optional) specific salt that should be used
> 
>:param hash_type: (optional) defines what hash algorithm should be used
> 
>:param iterations: (optional) defines the amount of iterations
> 
>:param data_type: (optional) defines the output type; hex and bytes are available
> 
>:return: returns hash (type: **hex** or bytes)

## Comparing a Hash
Use `compare_hash()` to compare a text to a hash.
``` python
hash = 'df70b9c795527ee3efcf3b0f36e669307d98895d402bd3c34dd7bd92222bdb8fde4e04ac169b9f27e1327e87e7e337b93d65c858a08fce7f3d1624e7fdb692807957b496801e5621b0f949f96d5811ff27125b9f866da3eaf9197f15703d335e'
to_compare = "Test"
print(compare_hash(pw,hash)) # prints "True"
```
This function can take 4 arguments:

>`compare_hash(to_compare, hash, hash_type='sh512', iterations=100000)`

>:param to_compare: the text that should be compared with the hash (type:hex, to str converted hex or bytes)
> 
>:param hash: the hash that should be compared with the text
> 
>:param hash_type: (optional) defines what hash algorithm should be used
> 
>:param iterations: (optional) defines the amount of iterations
> 
>:return: returns True or False (type: bool)
