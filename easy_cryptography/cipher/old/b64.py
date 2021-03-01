import base64


def encrypt(text: str):
    text_bytes = text.encode('utf-8')
    encoded = base64.b64encode(text_bytes)
    return encoded.decode('utf-8')


def decrypt(text):
    text = text.encode('utf-8')
    encoded = base64.b64decode(text)
    text_str = encoded.decode('utf-8')
    return text_str
