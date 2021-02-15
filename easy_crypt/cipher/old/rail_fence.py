def encrypt(text:str, shift: int):
    '''

    :param text: The text that is supposed to be encrypted(type: **str**)
    :param shift: How many rails should be used (type: **int**)
    :return: returns the encrypted text (type: **str**)
    '''
    if shift > len(text) or shift <= 1:
        raise ValueError("The shift is to big or to small")

    updated_text = []
    for value, letter in enumerate(text):
        s = value % (shift * 2 - 2)
        if s >= shift:
            s = (shift * 2 - 2) - s
        try:
            t = updated_text[s]
        except:
            updated_text.append(letter)
        else:
            t += letter
            updated_text[s] = t

    complet_text = ''
    for v, element in enumerate(updated_text):
        complet_text += element
        # print(v,element)
    return complet_text


def decrypt(text:str, shift: int):
    '''

    :param text: The text that is supposed to be decrypted(type: **str**)
    :param shift: How many rails should be used (type: **int**)
    :return: returns the decrypted text (type: **str**)
    '''
    if shift > len(text) or shift <= 1:
        raise ValueError("The shift is to big or to small")

    def get_rails(text, shift):  # Returns list with the amount on letters on a rail
        rails = []
        for v in range(len(text)):
            s = v % (shift * 2 - 2)
            if s >= shift:
                s = (shift * 2 - 2) - s
            try:
                amount = rails[s]
            except:
                rails.append(0)
            else:
                amount += 1
                rails[s] = amount
        return rails

    def split_text(text, rails):  # splits the text into rails
        clist = []
        for p in rails:
            clist.append(text[:p + 1])
            text = text[p + 1:]
        return clist

    if shift > len(text) or shift <= 1:
        raise ValueError("The shift is to big or to small")

    def reverse_rail(clist, rails): #Reverse the cipher
        all = ''
        row = 0
        way = 'up'
        positions = []
        for _ in range(len(rails)):
            positions.append(0)
        for p in range(len(text)):
            part = clist[row]
            all += part[positions[row]]
            positions[row] = int(positions[row]) + 1
            if row >= len(clist) - 1:
                row -= 1
                way = 'down'
            elif row <= 0:
                row += 1
                way = 'up'
            elif way == 'up':
                row += 1
            elif way == 'down':
                row -= 1
        return all

    rails = get_rails(text, shift)
    clist = split_text(text, rails)
    return reverse_rail(clist, rails)


