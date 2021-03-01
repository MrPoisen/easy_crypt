import string

from easy_cryptography.Exceptions import InvalidLetterError


def test_for_divisors(value, divisors):

    for element in divisors:
        result = value / element
        if result == int(result):
            return True
        else:
            pass
    return False


def get_divisor(alphabet):
    divisors = []
    for i in range(2, len(alphabet) - 1):  # checks for values
        p = len(alphabet) / i
        if p == int(p):  # Checks if it divides without rest
           divisors.append(i)  # saves value
        else:
            pass
    return divisors


def encrypt(text:str, a:int, b:int, alphabet=None,remain = [" "]):
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

    for r in remain:
        if r in alphabet:
            raise InvalidLetterError(r,"Letter in remain can't be in the alphabet")

    divisors = get_divisor(alphabet)
    if test_for_divisors(a,divisors):
        raise ValueError("a must be a coprime")

    result = ""

    for char in text:
        if char in remain:
            result += char
        else:
            pos = alphabet.index(char)
            newpos = (a * pos + b) % len(alphabet)

            newchar = alphabet[newpos]
            result += newchar
    return result


def decrypt(text:str, a:int, b:int, alphabet=None,remain = [" "]):
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

    for r in remain:
        if r in alphabet:
            raise InvalidLetterError(r,"Letter in remain can't be in the alphabet")

    divisors = get_divisor(alphabet)
    if test_for_divisors(a, divisors):
        raise ValueError("a must be a coprime")

    if a <= 0:
        raise ValueError("a must be bigger than 0")
    result = ''
    a_inv = 0
    while (a * a_inv) % len(alphabet) != 1:
        a_inv += 1

    for char in text:
        if char in remain:
            result += char
        else:
            pos = alphabet.index(char)
            newpos = (a_inv * (pos - b)) % len(alphabet)

            newchar = alphabet[newpos]
            result += newchar
    return result

