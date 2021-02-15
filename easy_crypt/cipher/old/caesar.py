import string

import sys

from easy_crypt.Exceptions import *

pyprind_not_available = False
try:
    import pyprind
except:
    pyprind_not_available = True


def encrypt(text:str, shift:int, alphabet=None, progbar=False):
    ''' Encryption with Caesar

    :param text: The text that is supposed to be encrypted
    :param shift: The Change of the text
    :param alphabet: The used Alphabet for encryption
    :param progbar: bool: If the pyprind library should be used
    :return: The encrypted text
    '''
    if shift < 0: raise ValueError("The Value must be positive") # Checks if the Value is positive or 0
    if progbar and pyprind_not_available: raise MissingPackageError( # Checks if  pyprind is used even though it isn't installed
        "Package pyprind is not installed. Install it or don't use it.")
    if progbar:
        n = len(text)
        bar = pyprind.ProgBar(n, track_time=True, title='Encryption status', stream=sys.stdout, bar_char='█') # Sets up a bar
    standard_alphabet = string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits + "ÄÖÜäöüßÃŸâ€" # builds the standart alphabet
    if alphabet == None: # Sets the alphabet to the standard alphabet if None is given
        alphabet = standard_alphabet
    updated_text = ''
    for letter in text:
        if letter not in alphabet: # Checks if the letter is in the used alphabet
            raise InvalidLetterError(letter, "The letter is not in the used alphabet")
        if letter == " ": # Space will remain
            updated_letter = letter
        else:
            pos = alphabet.index(letter) # gets position in the alphabet
            pos = (pos + shift) % len(alphabet) # Calculates the new position in the alphabet
            updated_letter = alphabet[pos]
        updated_text = updated_text + updated_letter # Adds the new letter to the encrypted text
        if progbar: bar.update()
    if progbar:
        bar.stop()
        return updated_text, bar
    return updated_text


def decrypt(text:str, shift:int, alphabet=None, progbar=False):
    ''' Decryption with Caesar

    :param text: The text that is supposed to be decrypted
    :param shift: The Change of the text
    :param alphabet: alphabet: The used Alphabet for decryption
    :param progbar: bool: If the pyprind library should be used
    :return: The decrypted text
    '''
    if shift < 0: raise ValueError("The Value must be positive")  # Checks if the Value is positive or 0
    if progbar and pyprind_not_available: raise MissingPackageError(  # Checks if pyprind is used even though it isn't installed
        "Package pyprind is not installed. Install it or don't use it.")
    if progbar:
        n = len(text)
        bar = pyprind.ProgBar(n, track_time=True, title='Encryption status', stream=sys.stdout, bar_char='█')  # Sets up a bar
    standard_alphabet = string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits + "ÄÖÜäöüßÃŸâ€" # builds the standart alphabet
    if alphabet == None: # Sets the alphabet to the standard alphabet if None is given
        alphabet = standard_alphabet
    updated_text = ''
    for letter in text:
        if letter not in alphabet: # Checks if the letter is in the used alphabet
            raise InvalidLetterError(letter, "The letter is not in the used alphabet")
        if letter == " ": # Space will remain
            updated_letter = letter
        else:
            pos = alphabet.index(letter) # gets position in the alphabet
            pos = (pos - shift) % len(alphabet) # Calculates the new position in the alphabet
            updated_letter = alphabet[pos]
        updated_text = updated_text + updated_letter # Adds the new letter to the encrypted text
        if progbar: bar.update()
    if progbar:
        bar.stop()
        return updated_text, bar
    return updated_text

encr = encrypt("Hello",5)
print(encr)