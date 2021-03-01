import string
from easy_cryptography.cipher.old.unknown import Unknown

un = Unknown()
hex, bas64, coincidence= un.check("HELLO HOW ARE YOU",alphabet=string.ascii_uppercase) #checks if it could be hex and base64
                                                                                       #and calculates the coincidenc
print(hex,bas64,coincidence)