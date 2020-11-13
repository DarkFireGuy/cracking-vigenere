from kasiski import *


class Vigenere:

    def test(self, key):
        if ''.join(filter(str.isalpha, key)).upper() != self.key:
            return False
        return True

    def __init__(self, p, k):
        # Remove all non alphabetic characters and make them both upper case
        self.plain = ''.join(filter(str.isalpha, p)).upper()
        # Additionally, make key same length as plaintext if key is longer
        self.key = ''.join(filter(str.isalpha, k)).upper()[0:len(self.plain)]
        self.cipher = encrypt(self.plain, self.key)
        self.ngrams = {}
        # Adds dictionary entries for trigrams to 6-grams
        for x in range(3, 7):
            tmp = ngrams(self.cipher, x)
            if tmp:
                self.ngrams[x] = tmp

    def __str__(self):
        # Change this to something better
        return("The plaintext \"%s\" was encrypted using the keyword \"%s\" to create the cipher text \"%s\"" %
               (self.plain, self.key, self.cipher))


def encrypt(p, k):
    # Creating the key stream
    k = k.upper() * int(len(p) / len(k)) + k[0:len(p) % len(k)]
    c = ''
    p = p.upper()
    # For each character in the plain text calculate the corresponding ciphertext character
    for x in range(0, len(p)):
        c += chr((ord(p[x]) + ord(k[x])) % 26 + 65)
    return c


def decrypt(c, k):
    # Creating the key stream
    k = k.upper() * int(len(c) / len(k)) + k[0:len(c) % len(k)]
    p = ''
    c = c.upper()
    # For each character in the plain text calculate the corresponding ciphertext character
    for x in range(0, len(c)):
        p += chr((ord(c[x]) - ord(k[x])) % 26 + 65)
    return p
