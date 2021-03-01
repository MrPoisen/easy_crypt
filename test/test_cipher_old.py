import string
import random
import pytest

from easy_cryptography.cipher.old import affine as af
from easy_cryptography.cipher.old import atbash as at
from easy_cryptography.cipher.old import b64 as b
from easy_cryptography.cipher.old import caesar as ca
from easy_cryptography.cipher.old import hex as h
from easy_cryptography.cipher.old import rail_fence as rf
from easy_cryptography.cipher.old import vigener as v
from easy_cryptography.cipher.old.unknown import Unknown
alphabet = string.ascii_uppercase+string.ascii_lowercase
test_text = "Hello, How are you"
remain = [" ",","]

def test_affine():

    encr = af.encrypt(test_text,3,6,alphabet=alphabet,remain=remain)
    decr = af.decrypt(encr,3,6,alphabet=alphabet,remain=remain)
    assert decr == test_text

def test_atbash():
    encr = at.cipher(test_text,alphabet=alphabet,remain=remain)
    decr = at.cipher(encr,alphabet=alphabet,remain=remain)
    assert decr == test_text

def test_b64():
    encr = b.encrypt(test_text)
    decr = b.decrypt(encr)
    assert decr == test_text

def test_caesar():
    value = random.randint(0,len(alphabet))
    encr = ca.encrypt(test_text, shift=value,alphabet=alphabet, remain=remain)
    decr = ca.decrypt(encr,shift=value, alphabet=alphabet, remain=remain)
    assert decr == test_text

def test_hex():
    encr = h.encrypt(test_text)
    decr = h.decrypt(encr)
    assert decr == test_text

def test_rail_fence():
    value = random.randint(1,len(test_text))
    encr = rf.encrypt(test_text,shift=value)
    decr = rf.decrypt(encr,shift=value)
    assert decr == test_text

def test_vigener():

    length = random.randint(1,10)
    pw = v.gen_keys(length,alphabet=alphabet)
    encr = v.encrypt(test_text,pw=pw,alphabet=alphabet,remain=remain)
    decr = v.decrypt(encr,pw=pw,alphabet=alphabet,remain=remain)
    assert decr == test_text

@pytest.mark.parametrize("cipher, alphabet, expected",[
    ("PPQCAXQVEKGYBNKMAZUYBNGBALJONITSZMJYIMVRAGVOHTVRAUCTKSGDDWUOXITLAZUVAVVRAZCVKBQPIWPOU",string.ascii_uppercase, "THOSEPOLICEOFFICERSOFFEREDHERARIDEHOMETHEYTELLTHEMAJOKETHOSEBARBERSLENTHERALOTOFMONEY"),# Vigenere
("TIRTHTYHFCEAYETONHEOFEHRELESEENSORDIHLKELROEESEDTTOBSAMPCOREEHJARLFOIFEHMEAREOOLFOMBT", string.ascii_uppercase,"THOSEPOLICEOFFICERSOFFEREDHERARIDEHOMETHEYTELLTHEMAJOKETHOSEBARBERSLENTHERALOTOFMONEY"), # Rail Fence
])
def test_Unkown(cipher,alphabet,expected):
    un = Unknown()

    intell=["those","police"]
    broke = un.break_(cipher,alphabet=alphabet, intell=intell, all_intell=False, ignore_capse=True, ignore_punctuation=True, ignore_numbers=True, Bruteforce=False, fast=False, split=False)
    assert broke[1] == expected


