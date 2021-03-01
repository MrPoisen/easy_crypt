import hashlib
import os

from easy_cryptography.Exceptions import *


def gen_hash(text, predefined_salt=None, hash_type='sha512', iterations=100000, data_type='hex'):
    ''' Generates a hash from a text, standard in type sh512 and returns it with the salt as a prefix in bytes (or in hex)

    :param text: the text that is supposed to be hashed
    :param predefined_salt: (optional) specific salt that should be used
    :param hash_type: (optional) defines what hash algorithm should be used
    :param iterations: (optional) defines the amount of iterations
    :param data_type: (optional) defines the output type
    :return: returns hash
    '''
    if predefined_salt == None:
        salt = os.urandom(32)  # Generates random bytes
    else:
        if type(predefined_salt) == bytes or type(predefined_salt) == bytearray or type(predefined_salt) == str or type(
                predefined_salt) == hex:  # Checks if it is a valid data typ
            if type(predefined_salt) == str or type(predefined_salt) == hex:
                predefined_salt = bytearray.fromhex(predefined_salt)  # Trys to convert  to binary
            salt = predefined_salt
        else:
            raise WrongSaltTypeError(predefined_salt,
                                     " It should be bytes, bytearray, str or hex.")  # Raises Error
    if type(text) != bytes:
        text = text.encode('utf-8')  # Trys to convert text
    h = hashlib.pbkdf2_hmac(hash_type, text, salt, iterations)  # Generates hash
    if data_type == 'hex':  # Converts to hex
        salt = salt.hex()
        h = h.hex()
    if data_type == 'bytes':
        # Standard output type is bytes
        pass
    allbytes = salt + h  # Adds it up
    return allbytes


def compare_hash(to_compare, hash, hash_type='sh512', iterations=100000):
    ''' Compares a text with a hash

    :param to_compare: the text that should be compared with the hash
    :param hash: the hash that should be compared with the text
    :param hash_type: (optional) defines what hash algorithm should be used
    :param iterations: (optional) defines the amount of iterations
    :return: returns True or False
    '''
    if type(hash) == bytes or type(hash) == bytearray:  # Checks type of hash
        hash = hash.hex()
    elif type(hash) == hex or type(hash) == str:
        pass
    else:
        raise WrongTypeError(hash, "It should be bytes, bytearray, str or hex.")
    salt = hash[:64]  # 64 is the length of the salt in hex
    hash_text = hash[64:]
    testhash = gen_hash(to_compare, salt, hash_type=hash_type, iterations=iterations)
    test = testhash[64:]
    return hash_text == test
