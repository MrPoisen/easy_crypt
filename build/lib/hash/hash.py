import os
import hashlib

def gen_hash(pw,predefined_salt = None):
    if predefined_salt == None:
        salt = os.urandom(32)
    else:
        salt = bytearray.fromhex(predefined_salt)

    pw = pw.encode()
    key = hashlib.pbkdf2_hmac('sha512', pw, salt, 100000).hex()
    allbytes = salt.hex() + key
    k = allbytes
    return k

def compare_hash(pw, hash):
    salt = hash[:64]  # 32 is the length of the salt
    key = hash[64:]
    testhash = gen_hash(pw,salt)
    testkey = testhash[64:]
    if key == testkey:
        return True
    else:
        return False