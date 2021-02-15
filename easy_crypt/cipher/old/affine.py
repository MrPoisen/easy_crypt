import string


def even(value):
    r = value % 2
    return r == 0


def encrypt(text:str, a:int, b:int, alphabet=None):
    '''

    :param text: the text that is supposed to be encrypted(type: **str**)
    :param a: key a, must be a coprime to the length of the alphabet (type: **int**)
    :param b: key b (type: **int**)
    :param alphabet: the alphabet that should be used (type: **str**)
    :return: returns encrypted str (type: **str**)
    '''
    standard_alphabet = string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits + "ÄÖÜäöüßÃŸâ€"  # builds the standart alphabet
    if alphabet == None:  # Sets the alphabet to the standard alphabet if None is given
        alphabet = standard_alphabet

    if even(len(alphabet)) and even(a):
        raise ValueError("a must be a coprime")

    if even(len(alphabet)) == False and even(a) == False:
        raise ValueError("a must be a coprime")

    result = ""

    for char in text:
        if char == " ":
            result += char
        else:
            pos = alphabet.index(char)
            newpos = (a * pos + b) % len(alphabet)

            newchar = alphabet[newpos]
            result += newchar
    return result


def decrypt(text:str, a:int, b:int, alphabet=None):
    '''

    :param text: the text that is supposed to be decrypted(type: **str**)
    :param a: key a, must be a coprime to the length of the alphabet (type: **int**)
    :param b: key b (type: **int**)
    :param alphabet: the alphabet that should be used (type: **str**)
    :return: returns decrypted str (type: **str**)
    '''
    standard_alphabet = string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits + "ÄÖÜäöüßÃŸâ€"  # builds the standart alphabet
    if alphabet == None:  # Sets the alphabet to the standard alphabet if None is given
        alphabet = standard_alphabet

    if even(len(alphabet)) and even(a):
        raise ValueError("a must be a coprime")

    if even(len(alphabet)) == False and even(a) == False:
        raise ValueError("a must be a coprime")

    result = ''
    a_inv = 0
    while (a * a_inv) % len(alphabet) != 1:
        a_inv += 1

    for char in text:
        if char == " ":
            result += char
        else:
            pos = alphabet.index(char)
            newpos = (a_inv * (pos - b)) % len(alphabet)

            newchar = alphabet[newpos]
            result += newchar
    return result

