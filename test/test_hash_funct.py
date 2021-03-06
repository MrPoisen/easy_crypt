import easy_cryptography.hash.hash_funct as h

text = "This is for testing purposes"

def test_hash():
    hashed = h.gen_hash(text)
    assert h.compare_hash(text,hashed)