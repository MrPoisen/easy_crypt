def encrypt(text):
    text_bytes = text

    if type(text) == str:
        text_bytes = text.encode('utf-8')

    if type(text_bytes) != bytes:
        raise TypeError("Type must be str or bytes")

    text_hex = text_bytes.hex()
    return text_hex


def decrypt(text: bytes):
    text_bytes = bytearray.fromhex(text)
    text_str = text_bytes.decode('utf-8')
    return text_str
