import easy_cryptography.cipher.cipher_funct as cipher


text = "This is for testing purposes"

def test_asym():
    private_key,public_key = cipher.gen_asym_keys()
    encr = cipher.encrypt_asym(text,public_key)
    decr = cipher.decrypt_asym(encr,private_key)
    assert decr == text

def test_sym():
    key = cipher.get_sym_keys()
    encr = cipher.encrypt_sym(text,key)
    decr = cipher.decrypt_sym(encr,key)
    assert decr == text

def test_data():
    private_key, public_key = cipher.gen_asym_keys()
    encr = cipher.encr_data(text,public_key)
    decr = cipher.decr_data(encr,private_key)
    assert decr == text