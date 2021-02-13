# Old Chiphers
This section talks about every chipher under the easy_crypt.cipher.old section
## Caesar
*This Cipher supports pyprind*

The standard alphabet is:  
`standard_alphabet = string.ascii_lowercase + string.ascii_uppercase + " " + string.punctuation + string.digits + "ÄÖÜäöüßÃŸâ…¤€"`
```` python
from easy_crypt.chipher.old import caeser as c
encr = c.encrypt("Hello",5) #Shift 5
print(encr) #prints "Mjqqt"
decr = c.decrypt(encr,5) #Shift 5 back
print(decr) #prints "Hello"
````
If you want to use pyprind, do it like this:
```` python
from easy_crypt.chipher.old import caeser as c
encr,bar = c.encrypt("Hello",5,progbar=True) #Shift 5
print(bar) # prints final bar; this isn't needed
print(encr) #prints "Mjqqt"
decr,bar = c.decrypt(encr,5,progbar=True) #Shift 5 back
print(bar) # prints final bar; this isn't needed
print(decr) #prints "Hello"
````
`encrypt()` can take 4 arguments:
> `encrypt(text, shift, alphabet=None, progbar=False)`

>:param text: The text that is supposed to be encrypted (type: **str**)
> 
>:param shift: The Change of the text (type: **int**)
> 
>:param alphabet: The used Alphabet for encryption (type: **str**)
> 
>:param progbar: If the pyprind library should be used (type: **bool**)
> 
>:return: The encrypted text (type: **str**)


`decrypt()` can take 4 arguments:
> `decrypt(text, shift, alphabet=None, progbar=False)`

>:param text: The text that is supposed to be decrypted (type: **str**)
> 
>:param shift: The Change of the text (type: **int**)
> 
>:param alphabet: alphabet: The used Alphabet for decryption (type: **str**)
> 
>:param progbar: bool: If the pyprind library should be used (type: **bool**)
> 
>:return: The decrypted text (type: **str**)

##Vigener
*This Cipher supports pyprind*

The standard alphabet is:  
`standard_alphabet = string.ascii_lowercase + string.ascii_uppercase + " " + string.punctuation + string.digits + "ÄÖÜäöüßÃŸâ…¤€"`

``` python
from easy_crypt.chipher.old import vigener as v
encr = v.encrypt("Hello","Hello") #Encrypts with the pw
print(encr) #prints ".iwwC"
decr = c.decrypt(encr,"Hello") #Decrypts with the pw
print(decr) #prints "Hello"
```
If you want to use pyprind, do it like this:
``` python
from easy_crypt.chipher.old import vigener as v
encr, bar = v.encrypt("Hello","Hello",progbar=True) #Encrypts with the pw
print(bar) # prints final bar; this isn't needed
print(encr) #prints ".iwwC"
decr,bar = c.decrypt(encr,"Hello",progbar=True) #Decrypts with the pw
print(bar) # prints final bar; this isn't needed
print(decr) #prints "Hello"
```
`encrypt()` can take 4 arguments:

>`encrypt(text, pw, alphabet=None, progbar=False)`

>:param text: The text that is supposed to be encrypted (type: **str**)
> 
>:param pw: The password for the encryption (type: **str**)
> 
>:param alphabet: The used Alphabet for encryption (type: **str**)
> 
>:param progbar: bool: If the pyprind library should be used (type: **bool**)
> 
>:return: The encrypted text (type: **str**)

`decrypt()` can take 4 arguments:

>`decrypt(text, pw, alphabet=None, progbar=False)`

>:param text: The text that is supposed to be decrypted (type: **str**)
> 
>:param pw: The password for the decryption (type: **str**)
> 
>:param alphabet: The used Alphabet for encryption (type: **str**)
> 
>:param progbar: bool: If the pyprind library should be used (type: **bool**)
> 
>:return: The decrypted text (type: **str**)