from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, Salsa20
from Crypto.Random import get_random_bytes

def gen_Keys():
    prkey = RSA.generate(2048)
    pubkey = prkey.publickey()
    return prkey,pubkey

def encrypt(text,pubkey):
    if type(text) != bytes:
        print(type(text)," _ to byte ")
        text = text.encode('utf-8')
    cypher = PKCS1_OAEP.new(pubkey)
    print(len(text))
    encrmsg = cypher.encrypt(text)
    return encrmsg
def decrypt(text,prkey):
    if type(text) != bytes:
        print(type(text)," _ to byte ")
        text = text.encode('utf-8')
    cypher = PKCS1_OAEP.new(prkey)
    decrmsg = cypher.decrypt(text)
    return decrmsg

def get_sym_keys():
    key = get_random_bytes(32)
    return key

def encrypt_sym(text,key):
    if type(text) != bytes:
        print(type(text)," _ to byte ")
        text = text.encode('utf-8')
    cipher = Salsa20.new(key=key)
    ciphertext = cipher.encrypt(text)
    msg = cipher.nonce + ciphertext
    return msg

def decrypt_sym(text:bytes,key):
    cipher = Salsa20.new(key=key,nonce=text[:8])
    pl = cipher.decrypt(text[8:])
    return pl

def encr_data(data,pubkey):
    key = get_sym_keys()
    d = encrypt_sym(data,key)
    k = encrypt(key,pubkey)
    print(len(k),k,"k")
    space = b'$$$$'
    all = k+space+d
    print("d",d)
    print("all:",all)
    print("all",type(all))
    return all

def decr_data(data,prkey):
    key,da = data.split(b'$$$$')
    print("key:",len(key),key)
    key = decrypt(key,prkey)
    msg = decrypt_sym(da,key)
    return msg
