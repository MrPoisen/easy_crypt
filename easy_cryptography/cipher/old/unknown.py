import operator
import string
from collections import OrderedDict

from easy_cryptography.Exceptions import WrongTypeError

pyprind_not_available = False
try:
    import pyprind
except ImportError:
    pyprind_not_available = True


class Generator:
    '''
    class contains a list, representing letters which together form a vigener password
    '''

    def __init__(self, alphabet=None):
        if alphabet is not None:
            self.__alphabet = alphabet
        else:
            self.__alphabet = string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits + "ÄÖÜäöüßÃŸâ€"
        self.__pos = [0]
        self.__a_lenght = len(self.__alphabet)
        self.__costum_alphabet = string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits + "ÄÖÜäöüßÃŸâ€"

        # custom

        self.__costum_values = []
        self.__costum_dic = {}

    # Costum list

    def set_custom_alphabet(self, alphabet=None):
        if alphabet is not None:
            self.__costum_alphabet = alphabet
        else:
            self.__costum_alphabet = string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits + "ÄÖÜäöüßÃŸâ€"

    def set_custom_dic(self, dic: dict):
        self.__costum_values = []
        for _ in range(len(dic)):
            self.__costum_values.append(0)
        self.__costum_dic = dic

    def change_custom_values(self, costum_values: list):
        self.__costum_values = costum_values

    def custom_increase(self, amount_of_increases=1):
        for _ in range(amount_of_increases):
            v = self.__costum_values[0]
            v += 1
            self.__costum_values[0] = v

            for number, i in enumerate(self.__costum_values):

                if int(i) == len(self.__costum_dic.get(number)):
                    i = 0
                    self.__costum_values[number] = i
                    try:
                        pos = self.__costum_values[number + 1]
                        pos += 1
                        self.__costum_values[number + 1] = pos
                    except:

                        return False

    def return_custom_pw(self):
        result = ''
        for number, element in enumerate(self.__costum_values):
            part = self.__costum_dic.get(number)
            real = part[element]
            result += real

        return result

    def return_custom_list(self):
        return self.__costum_values

    # normal lists

    def increase(self, amount_of_increases=1):
        if type(amount_of_increases) != int:
            raise WrongTypeError(amount_of_increases, "amount_of_increases should be type int")
        if amount_of_increases < 1:
            raise ValueError("amount_of_increases shouldn't be less than 1")

        for i in range(amount_of_increases):
            pos = self.__pos[0]
            pos += 1  # increases the first position
            self.__pos[0] = pos

            for value, i in enumerate(self.pos):
                if int(i) == self.__a_lenght:
                    i = 0
                    self.__pos[value] = i

                    try:
                        pos = self.__pos[value + 1]
                        pos += 1
                        self.__pos[value + 1] = pos
                    except:
                        self.__pos.append(0)

        return self.pos

    def convert(self):
        self.__pos.reverse()
        all = ''
        for number in self.pos:
            all += self.__alphabet[number]
        self.__pos.reverse()
        return all

    def return_list(self):
        pos = self.pos
        pos.reverse()
        return list(pos)

    def set_list(self, list_):
        list_.reverse()
        self.pos = list_


class Analys:  # "Help" from https://inventwithpython.com/hacking/chapter20.html
    def __init__(self, alphabet=None):
        self.__text = ''
        self.__frequenz = {"en": "ETAOINSHRDLCUMWFGYPBVKJXQZ", "ger": "ENISRATDHULCGMOBWFKZVÜPÄßÖYQX"}
        if alphabet != None:
            self.__alphabet = alphabet
        else:
            self.__alphabet = string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits + "ÄÖÜäöüßÃŸâ€"
        from easy_cryptography.cipher.old import vigener as v
        self.__vigener = v

        self.__generator = Generator(self.__alphabet)
        self.__max_factor = 15

    def change_max_length(self, length:int):
        self.__max_factor = length

    def add_frequency(self, dic: dict):
        self.__frequenz.update(dic)

    def __get_seq_spacing(self, ciphertext):
        seqSpacings = {}
        for seq_length in range(3, 6):
            for seq_start in range(len(ciphertext) - seq_length):
                seq = ciphertext[seq_start:seq_start + seq_length]
                for i in range(seq_start + seq_length, len(ciphertext) - seq_length):
                    if ciphertext[i:i + seq_length] == seq:
                        if seq not in seqSpacings:
                            seqSpacings[seq] = []
                        seqSpacings[seq].append(i - seq_start)

        return seqSpacings

    def __get_useful_factors(self, num):
        divisors = []
        for i in range(2, num + 1):  # checks for values
            if num % i == 0:  # Checks if it divides without rest
                divisors.append(i)  # saves value
            else:
                pass
        return divisors

    def __get_table(self, spacings: dict):
        table = {}
        for spacing in spacings.values():
            for element in spacing:
                divisors = self.__get_useful_factors(int(element))

                for divis in divisors:
                    if divis not in table.keys():
                        table[divis] = 0
                    anzahl = int(table.get(divis))
                    anzahl += 1
                    table[divis] = anzahl

        return table

    def __best_factor(self, table: dict):
        factors = []
        highest = 0
        for value in table.values():
            if int(value) > highest:
                highest = int(value)
        for key, value in table.items():
            if value == highest:
                if key < self.__max_factor:  # makes sure the factor isn't too large
                    factors.append(key)
        return factors

    def __split_text(self, ciphertext, number):
        splited = {}
        for value, char in enumerate(ciphertext):
            position = value % number
            if position not in splited.keys():
                splited[position] = char
            elif position in splited.keys():
                chars = splited.get(position)
                chars += char
                splited[position] = chars
        return splited

    def frequency_analyse(self,text ,language='en'):
        ETAOIN = self.__frequenz.get(language)  # Gets the letters of a language sorted by it's frequenz

        text = text.upper()
        text = text.replace(" ", "")

        def getLetterCount(message):
            letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0,
                           'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0,
                           'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
            for letter in message.upper():
                if letter in string.ascii_uppercase:
                    if letter not in letterCount.keys():
                        letterCount[letter] = 0
                    letterCount[letter] += 1
            return letterCount

        def getItemAtIndexZero(x):
            return x[0]

        def getFrequencyOrder(message):
            letterToFreq = getLetterCount(message)
            freqToLetter = {}
            for letter in string.ascii_uppercase:
                if letterToFreq[letter] not in freqToLetter:
                    freqToLetter[letterToFreq[letter]] = [letter]
                else:
                    freqToLetter[letterToFreq[letter]].append(letter)
            for freq in freqToLetter:
                freqToLetter[freq].sort(key=ETAOIN.find, reverse=True)
                freqToLetter[freq] = ''.join(freqToLetter[freq])
            freqPairs = list(freqToLetter.items())
            freqPairs.sort(key=getItemAtIndexZero, reverse=True)
            freqOrder = []
            for freqPair in freqPairs:
                freqOrder.append(freqPair[1])
            return ''.join(freqOrder)

        def convert(text:str):
            order = getFrequencyOrder(text)
            copy = text
            for char_e,char_o in zip(ETAOIN,order):
                copy = copy.replace(char_o,char_e)
            return copy

        return convert(text)

    def __get_frequenz_analys(self, text, language="en"):

        ETAOIN = self.__frequenz.get(language)  # Gets the letters of a language sorted by it's frequenz

        text = text.upper()
        text = text.replace(" ", "")

        def getLetterCount(message):
            letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0,
                           'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0,
                           'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
            for letter in message.upper():
                if letter in string.ascii_uppercase:
                    letterCount[letter] += 1
            return letterCount

        def getItemAtIndexZero(x):
            return x[0]

        def getFrequencyOrder(message):
            letterToFreq = getLetterCount(message)
            freqToLetter = {}
            for letter in string.ascii_uppercase:
                if letterToFreq[letter] not in freqToLetter:
                    freqToLetter[letterToFreq[letter]] = [letter]
                else:
                    freqToLetter[letterToFreq[letter]].append(letter)
            for freq in freqToLetter:
                freqToLetter[freq].sort(key=ETAOIN.find, reverse=True)
                freqToLetter[freq] = ''.join(freqToLetter[freq])
            freqPairs = list(freqToLetter.items())
            freqPairs.sort(key=getItemAtIndexZero, reverse=True)
            freqOrder = []
            for freqPair in freqPairs:
                freqOrder.append(freqPair[1])
            return ''.join(freqOrder)

        def FreqMatchScore(message):
            freqOrder = getFrequencyOrder(message)
            matchScore = 0
            for commonLetter in ETAOIN[:6]:
                if commonLetter in freqOrder[:6]:
                    matchScore += 1
            for uncommonLetter in ETAOIN[-6:]:
                if uncommonLetter in freqOrder[-6:]:
                    matchScore += 1
            return matchScore

        result = FreqMatchScore(text)
        return result

    def __gen_pws(self, dic: dict):
        pws = []
        how_many = 1
        for item in dic.values():
            how_many = how_many * (len(item))

        self.__generator.set_custom_dic(dic)
        first = ''
        first_time = True
        for _ in range(how_many):
            if self.__generator.return_custom_pw() == first:
                break
            if first_time:
                first = self.__generator.return_custom_pw()
            pws.append(self.__generator.return_custom_pw())

            self.__generator.custom_increase()
        return pws

    def get_keys(self, ciphertext, language="en"):
        ciphertext.replace(" ", "")
        ciphertext = ciphertext.upper()
        spacings = self.__get_seq_spacing(ciphertext)
        table = self.__get_table(spacings)
        factors = self.__best_factor(table)  # factors are the most likely lenghts
        sorted_after_length = {}
        for factor in factors:  # For each possible length
            splited = self.__split_text(ciphertext, factor)
            most_likely = {}
            for value, split in enumerate(splited.values()):  # For each segment
                subkeys = {}
                for element in self.__alphabet:  # gets the matches
                    decr = self.__vigener.decrypt(split, element, alphabet=self.__alphabet)
                    match = self.__get_frequenz_analys(decr, language)
                    subkeys[str(element)] = match
                sortedDict = OrderedDict(sorted(subkeys.items(), key=operator.itemgetter(1)))  # sorts the Dict

                best = []  # stores the best keys
                # can be optimised
                #
                key = list(sortedDict.keys())[-1]
                item = sortedDict.get(key)
                best.append(key)
                biggest = int(item)
                for number in range(len(sortedDict) - 1, -1, -1):  # gets all possible keys for the segment
                    key = list(sortedDict.keys())[number]
                    item = sortedDict.get(key)
                    if int(item) == biggest:
                        best.append(key)
                    else:
                        break
                best = list(set(best))
                #
                #
                most_likely[value] = best
            pws = self.__gen_pws(most_likely)
            sorted_after_length[factor] = pws
        return sorted_after_length

    def key_dict_to_key_list(self, dic: dict):
        keys = []
        for pw_list in dic.values():
            for pw in pw_list:
                keys.append(pw)
        return keys


class Unknown:
    '''
    class with the power to decrypt unknown ciphers
    '''

    def __init__(self):
        self.__generator = Generator()
        self.__all_intel = False
        from easy_cryptography.cipher.old import affine as a
        from easy_cryptography.cipher.old import atbash as ab
        from easy_cryptography.cipher.old import b64 as b
        from easy_cryptography.cipher.old import caesar as c
        from easy_cryptography.cipher.old import hex as h
        from easy_cryptography.cipher.old import rail_fence as r
        from easy_cryptography.cipher.old import vigener as v
        self.__affine = a
        self.__atbash = ab
        self.__b64 = b
        self.__caesar = c
        self.__hex = h
        self.__rail = r
        self.__vigener = v
        self.__hex_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        self.__b64_list = []

        self.__wall = 0.055

        for char in (str(string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/=")):
            self.__b64_list.append(char)

        self.__pw_dic = {
            'vigener': ['123456', '123456789', 'qwerty', 'password', '1234567', '12345678', '12345', 'iloveyou',
                        '111111', '123123', 'abc123', 'qwerty123', '1q2w3e4r', 'admin', 'qwertyuiop', '654321',
                        '555555', 'lovely',
                        '7777777', 'welcome', '888888', 'princess', 'dragon', 'password1']}
        self.__alphabet_standart = string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits + "ÄÖÜäöüßÃŸâ€"
        self.__ko = dict()
        self.__divisors = []
        self.__common_words = {"en": ["the", "of", "and", "a"]}


    def get_max_time(self, text, alphabet=None, fast=True, addpwlist=None):
        if alphabet == None:  # Sets the alphabet to the standard alphabet if None is given
            alphabet = self.__alphabet_standart
        if fast:
            time = 2 + len(alphabet)
            time += int(len(text) / 2) - 2
            time += len(alphabet) ** 2
            pwlist = self.__pw_dic.get("vigener")  # gets the passwords from the standard list
            if addpwlist != None:  # if given adds new ones
                pwlist.extend(addpwlist)
            time += len(pwlist)
            time += 1000
            return time
        if fast == False:
            time = 2 + len(alphabet)
            time += len(text) - 2
            time += len(alphabet) ** 2
            time += 1000
            time += len(alphabet) ** 5
            return time

    def test_for_divisors(self, a, divisors=None):
        if divisors == None:
            divisors = self.__divisors
        teiler = False
        for element in divisors:
            if a % element == 0:
                teiler = True
                return teiler
            else:
                pass
        return teiler

    def __get_divisor(self):
        self.__divisors = []
        for i in range(2, len(self.__alphabet) - 1):  # checks for values
            p = len(self.__alphabet) / i
            if p == int(p):  # Checks if it divides without rest
                self.__divisors.append(i)  # saves value
            else:
                pass

    def __koinzidenz(self,
                   char):  # Adds a char to a dictionary with the amount of specific chars appearing in the ciphertext
        if char in self.__ko:
            count = int(self.__ko.get(char))
            count += 1
            self.__ko[char] = count
        else:
            self.__ko.update({char: 1})

    def __calc_koinzidenz(self, text):  # calc
        for char in self.__alphabet:
            if char not in self.__ko.keys():
                self.__ko.update({char: '0'})
        ko = 0
        for key, item in self.__ko.items():
            ko += int(item) * (int(item) - 1)
        ko = ko / (len(text) * (len(text) - 1))
        self.__reset_koinzidenz()
        return float(ko)

    def __reset_koinzidenz(self):
        self.__ko = {}

    def check(self,text):  # Checks which methods could be used for decrypting
        hex = True
        bas64 = True
        for char in text:
            self.__koinzidenz(char)
            if char not in self.__hex_list:
                hex = False
            if char not in self.__b64_list:
                bas64 = False
        if text[len(text) - 1] == "=":
            bas64 = True
        calc_koinzidenz = self.__calc_koinzidenz(text)
        self.__ko = dict()
        return hex, bas64, calc_koinzidenz

    def find(self, text: str, list_: list, split=" ", ignore_capse=False, ignore_punctuation=False,
             ignore_numbers=False, all_intell=None):  # searches for words in a text

        if all_intell == None:
            pass
        else:
            self.__all_intel = all_intell

        if ignore_capse:
            text = text.upper()
            for number, word in enumerate(list_):
                word = word.upper()
                list_[number] = word

        if ignore_punctuation:
            for char in string.punctuation:
                text = text.replace(char, "")

        if ignore_numbers:
            for num in string.digits:
                text = text.replace(str(num), "")

        if type(self.__all_intel) == float or type(self.__all_intel) == int:  # if all intell should be in the text
            count = 0
            if split == False:  # If the text shouldn't be split
                for word in list_:
                    if word in text:
                        count += text.count(word)

            if split != False:
                for word in text.split(split):
                    if word in list_:
                        count += 1

            if type(self.__all_intel) == float and len(text) > 0 or type(self.__all_intel) == int and len(text) > 0:
                perc = float(count) / len(text.split(split))
                return perc > self.__all_intel
            return count >= len(list_)

        if self.__all_intel == True:
            for word in list_:
                if word not in list_:
                    return False
            return True

        if self.__all_intel == False:
            if split == False:
                for word in list_:
                    if word in text:
                        return True

            if split != False:
                for word in text.split(split):
                    if word in list_:
                        return True

            return False

    def check_pw(self, pw, alphabet):
        for letter in pw:
            if letter not in alphabet:
                return False
        return True

    def break_(self, text, **kwargs):  # breaks the ciphertext #old: intell=False,all_intell = False,ignore_capse = False,ignore_punctuation = False,ignore_numbers=False,alphabet=None,Bruteforce=True,fast=True,progbar = False,addpwlist = None,language="en",split=" ",remain=[" "]
        # setting default for keyword arguments
        self.__intelligence = []
        intell = False
        self.__all_intel = False
        ignore_capse = False
        ignore_punctuation = False
        ignore_numbers = False
        self.__alphabet = self.__alphabet_standart
        Bruteforce = True
        fast = True
        progbar = False
        addpwlist = None
        language = "en"
        split = " "
        remain = [" "]
        self.__add_frequency = False
        max_length = 15


        for kwarg in kwargs:  # getting the values of the keyword arguments
            value = kwargs.get(kwarg)

            if kwarg == "intell":
                if type(value) != list:
                    raise WrongTypeError(value, "intell should be type list")
                self.__intelligence = value
                intell = True

            if kwarg == "all_intell":
                if type(value) != bool and type(value) != float and type(value) != int:
                    raise WrongTypeError(value, "all_intell should be bool, float or int")

                if type(value) == float and value > 1 or type(value) == int and value > 1:
                    raise ValueError("all_intell can't be larger than 1")
                self.__all_intel = value

            if kwarg == "ignore_capse":
                if type(value) != bool:
                    raise WrongTypeError(value, "ignore_capse should be type bool")
                ignore_capse = value

            if kwarg == "ignore_punctuation":
                if type(value) != bool:
                    raise WrongTypeError(value, "ignore_punctuation should be type bool")
                ignore_punctuation = value

            if kwarg == "ignore_numbers":
                if type(value) != bool:
                    raise WrongTypeError(value, "ignore_numbers should be type bool")
                ignore_numbers = value

            if kwarg == "alphabet":
                if type(value) != str:
                    raise WrongTypeError(value, "alphabet should be type str")
                self.__alphabet = value

            if kwarg == "bruteforce":
                if type(value) != bool:
                    raise WrongTypeError(value, "bruteforce should be type bool")
                Bruteforce = value

            if kwarg == "fast":
                if type(value) != bool:
                    raise WrongTypeError(value, "fast should be type bool")
                fast = value

            if kwarg == "progbar":
                if pyprind_not_available and type(value) != bool:
                    raise ImportError("pyprind can't be imported and used")
                progbar = value

            if kwarg == "addpwlist":
                if type(value) != list:
                    raise WrongTypeError(value, "add_pwlist should be type list")
                addpwlist = value

            if kwarg == "language":
                if type(value) != str:
                    raise WrongTypeError(value, "language should be type list")
                language=value

            if kwarg == "split":
                if type(value) != str and type(value) != bool:
                    raise WrongTypeError(value, "split should be type str")
                split = value


            if kwarg == "add_frequency":
                if type(value) != bool and type(value) != dict:
                    raise WrongTypeError(value, "add_frequency should be False or type dict")
                self.__add_frequency = value

            if kwarg == "remain":
                if type(value) != list:
                    raise WrongTypeError(value, "remain should be type list")
                remain = value

            if kwarg == "max_length":
                if type(value) != int:
                    raise WrongTypeError(value, "max_length should be type int")
                max_length = value


        hex, bas64, koi = self.check(text, self.__alphabet)
        returns = []

        # hex cipher
        if hex:
            if progbar != False: progbar.update()
            result = self.__hex.decrypt(text)
            if self.find(result, self.__intelligence, split, ignore_punctuation=ignore_punctuation,
                         ignore_capse=ignore_capse, ignore_numbers=ignore_numbers) and intell != False:
                if progbar != False: progbar.stop()
                if progbar != False: return ("Hex", result), progbar
                return result
            if intell == False:
                returns.append(("Hex", result))

        # base64 cipher
        if bas64:
            if len(text) % 4 == 0:
                if progbar != False: progbar.update()
                result = self.__b64.decrypt(text)
                if self.find(result, self.__intelligence, split, ignore_punctuation=ignore_punctuation,
                             ignore_capse=ignore_capse, ignore_numbers=ignore_numbers) and intell != False:
                    if progbar != False: progbar.stop()
                    if progbar != False: return ("Base64", result), progbar
                    return result
                if intell == False:
                    returns.append(("Base64", result))

        # caesar cipher
        for shift in range(len(self.__alphabet)):
            if progbar != False: progbar.update()
            result = self.__caesar.decrypt(text, shift, alphabet=self.__alphabet, remain=remain)
            if self.find(result, self.__intelligence, split, ignore_punctuation=ignore_punctuation,
                         ignore_capse=ignore_capse, ignore_numbers=ignore_numbers) and intell != False:
                if progbar != False: progbar.stop()
                if progbar != False: return ("Caesar", result, shift), progbar
                return ("Caesar", result, shift)
            if intell == False: returns.append(("Caesar", result, shift))

        # rail fence cipher
        if fast == False:
            for i in range(2, len(text)):
                if progbar != False: progbar.update()
                result = self.__rail.decrypt(text, i)
                if self.find(result, self.__intelligence, split, ignore_punctuation=ignore_punctuation,
                             ignore_capse=ignore_capse, ignore_numbers=ignore_numbers) and intell != False:
                    if progbar != False: progbar.stop()
                    if progbar != False: return ("Rail Fence", result, i), progbar
                    return ("Rail Fence", result, i)
                if intell == False: returns.append(("Rail Fence", result, i))
        if fast == True:
            for i in range(2, int(len(text) / 2)):
                if progbar != False: progbar.update()
                result = self.__rail.decrypt(text, i)
                if self.find(result, self.__intelligence, split, ignore_punctuation=ignore_punctuation,
                             ignore_capse=ignore_capse, ignore_numbers=ignore_numbers) and intell != False:
                    if progbar != False: progbar.stop()
                    if progbar != False: return ("Rail Fence", result, i), progbar
                    return ("Rail Fence", result, i)
                if intell == False: returns.append(("Rail Fence", result, i))

        # affine cipher
        self.__generator.set_list([1, 1])
        self.__get_divisor()
        for i in range(1, len(self.__alphabet) ** 2):
            if progbar != False: progbar.update()
            l = self.__generator.return_list()
            self.__generator.increase()
            a = l[0]
            b = l[1]
            if self.test_for_divisors(a):
                continue
            try:
                result = self.__affine.decrypt(text, a, b, alphabet=self.__alphabet, remain=remain)
            except:
                continue
            if self.find(result, self.__intelligence, split, ignore_punctuation=ignore_punctuation,
                         ignore_capse=ignore_capse, ignore_numbers=ignore_numbers) and intell != False:
                if progbar != False: progbar.stop()
                if progbar != False: return ("Affine", result, (a, b)), progbar
                return ("Affine", result)
            if intell == False:
                returns.append(("Affine", result, (a, b)))

        print("V")
        # Vigenere cipher
        if koi <= self.__wall:
            if fast:  # if fast mode is active

                # Dictonary attack
                pwlist = self.__pw_dic.get("vigener")  # gets the passwords from the standard list
                if addpwlist != None:  # if given adds new ones
                    pwlist.extend(addpwlist)
                for pw in pwlist:
                    if self.check_pw(pw, self.__alphabet):  # checks if the password can be used for decryption
                        if progbar != False: progbar.update()  # updates progresbar
                        result = self.__vigener.decrypt(text, pw, self.__alphabet,
                                                      remain=remain)  # decrypts with the given password
                        if self.find(result, self.__intelligence, split, ignore_punctuation=ignore_punctuation,
                                     ignore_capse=ignore_capse,
                                     ignore_numbers=ignore_numbers) and intell != False:  # checks if a word from the wordlist is in the result
                            if progbar != False: progbar.stop()
                            if progbar != False: return ("Vigener", result, pw), progbar
                            return ("Vigener", result, pw)
                        if intell == False: returns.append(("Vigener", result, pw))  # saves the result

                # Analays
                an = Analys(self.__alphabet)
                if self.__add_frequency is not False:
                    an.add_frequency(self.__add_frequency)

                an.change_max_length(max_length)
                keys = an.get_keys(text, language)  # Returns dict with the keys for every length
                Key_list = an.key_dict_to_key_list(keys)

                for key in Key_list:
                    result = self.__vigener.decrypt(text, key, alphabet=self.__alphabet, remain=remain)
                    if self.find(result, self.__intelligence, split, ignore_punctuation=ignore_punctuation,
                                 ignore_capse=ignore_capse,
                                 ignore_numbers=ignore_numbers) and intell != False:  # checks if a word from the wordlist is in the result
                        if progbar != False: progbar.stop()
                        if progbar != False: return ("Vigener", result, key), progbar
                        return ("Vigener", result, key)
                    if intell == False: returns.append(("Vigener", result, key))  # saves the result

                # short Bruteforce
                if Bruteforce:
                    for lenght in range(
                            int(len(self.__alphabet) ** 2.72)):  # checks for all possible pws from a lenght of 1 to 2.72
                        if progbar != False: progbar.update()
                        pw = self.__generator.convert()  # gets the pw in string
                        self.__generator.increase()  # increases to the next pw
                        result = self.__vigener.decrypt(text, pw, remain=remain)  # decrypts with the given password
                        if self.find(result, self.__intelligence, split, ignore_punctuation=ignore_punctuation,
                                     ignore_capse=ignore_capse,
                                     ignore_numbers=ignore_numbers) and intell != False:  # checks if a word from the wordlist is in the result
                            if progbar != False: progbar.stop()
                            if progbar != False: return ("Vigener", result, pw), progbar
                            return ("Vigener", result, pw)
                        if intell == False: returns.append(("Vigener", result, pw))  # saves the result

        if fast == False:
            # Dictonary attack

            pwlist = self.__pw_dic.get("vigener")  # gets the passwords from the standard list
            if addpwlist != None:  # if given adds new ones
                pwlist.extend(addpwlist)
            for pw in pwlist:
                if progbar != False: progbar.update()  # updates progresbar
                if self.check_pw(pw, self.__alphabet):  # checks if the password can be used for decryption
                    result = self.__vigener.decrypt(text, pw, alphabet=self.__alphabet,
                                                  remain=remain)  # decrypts with the given password
                    if self.find(result, self.__intelligence, split, ignore_punctuation=ignore_punctuation,
                                 ignore_capse=ignore_capse,
                                 ignore_numbers=ignore_numbers) and intell != False:  # checks if a word from the wordlist is in the result
                        if progbar != False: progbar.stop()
                        if progbar != False: return ("Vigener", result, pw), progbar
                        return ("Vigener", result)
                    if intell == False: returns.append(("Vigener", result, pw))  # saves the result

            # Analays
            an = Analys(self.__alphabet)

            if self.__add_frequency is not False:
                an.add_frequency(self.__add_frequency)

            an.change_max_length(max_length)
            keys = an.get_keys(text, language)  # Returns dict with the keys for every length
            Key_list = an.key_dict_to_key_list(keys)

            for key in Key_list:
                result = self.__vigener.decrypt(text, key, alphabet=self.__alphabet, remain=remain)

                if self.find(result, self.__intelligence, split, ignore_punctuation=ignore_punctuation,
                             ignore_capse=ignore_capse,
                             ignore_numbers=ignore_numbers) and intell != False:  # checks if a word from the wordlist is in the result
                    if progbar != False: progbar.stop()
                    if progbar != False: return ("Vigener", result, key), progbar
                    return ("Vigener", result)
                if intell == False: returns.append(("Vigener", result, key))  # saves the result

            self.__generator.set_list([0])  # sets the pw generator to 0
            # Bruteforce
            if Bruteforce:
                for lenght in range(len(self.__alphabet) ** 10):  # checks for all possible pws from a lenght of 1 to 10
                    if progbar != False: progbar.update()
                    pw = self.__generator.convert()  # gets the pw in string
                    self.__generator.increase()  # increases to the next pw
                    result = self.__vigener.decrypt(text, pw, remain=remain)  # decrypts with the given password
                    if self.find(result, self.__intelligence, split, ignore_punctuation=ignore_punctuation,
                                 ignore_capse=ignore_capse,
                                 ignore_numbers=ignore_numbers) and intell != False:  # checks if a word from the wordlist is in the result
                        if progbar != False: progbar.stop()
                        if progbar != False: return ("Vigener", result, pw), progbar
                        return ("Vigener", result, pw)
                    if intell == False: returns.append(("Vigener", result, pw))  # saves the result

        if len(returns) == 0: returns.append("NO MATCHES")
        if progbar != False: return returns, progbar
        return returns
