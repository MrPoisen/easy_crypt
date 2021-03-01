import string
from easy_cryptography.Exceptions import InvalidLetterError

def cipher(text: str, alphabet=None,remain = [" "]):
    ''' The cipher function is used for encryption and decryption

    :param text: the text that should be used (type: **str**)
    :param alphabet: the alphabet that should be used (type: **str**)
    :return: returns a string (type: **str**)
    '''

    for r in remain:
        if r in alphabet:
            raise InvalidLetterError(r,"Letter in remain can't be in the alphabet")

    standard_alphabet = string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits + "ÄÖÜäöüßÃŸâ€"  # builds the standart alphabet
    if alphabet == None:  # Sets the alphabet to the standard alphabet if None is given
        alphabet = standard_alphabet

    reversed_alph = alphabet[::-1]

    result = ''
    for char in text:
        if char in remain:
            result += char
        else:
            pos = alphabet.index(char)
            result += reversed_alph[pos]
    return result


