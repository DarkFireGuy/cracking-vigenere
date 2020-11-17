from kasiski import *
import os.path
from tools import *

class Vigenere:

    def test(self, key):
        if ''.join(filter(str.isalpha, key)).upper() != self.key:
            return False
        return True

    def __init__(self, p, k):
        # Remove all non alphabetic characters and make them both upper case
        self.plain_original = p
        self.plain = ''.join(filter(str.isalpha, self.plain_original)).upper()
        # Additionally, make key same length as plaintext if key is longer
        self.key = ''.join(filter(str.isalpha, k)).upper()[0:len(self.plain)]
        self.cipher_original = encrypt(self.plain_original, self.key)
        self.cipher = ''.join(filter(str.isalpha, self.cipher_original)).upper()
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
    tmp = k.upper()
    k = ''
    n = 0
    for x in p:
        if str.isalpha(x):
            k += tmp[n % len(tmp)]
            n += 1
        else:
            k += x
    c = ''
    # For each character in the plain text calculate the corresponding ciphertext character
    for x in range(0, len(p)):
        if str.isalpha(p[x]):
            tmp = chr((ord(p[x].upper()) + ord(k[x])) % 26 + 65)
            if p[x].islower():
                c += tmp.lower()
            else:
                c += tmp.upper()
        else:
            c += p[x]
    return c


def decrypt(c, k):
    # Creating the key stream
    tmp = k.upper()
    k = ''
    n = 0
    for x in c:
        if str.isalpha(x):
            k += tmp[n % len(tmp)]
            n += 1
        else:
            k += x
    p = ''
    # For each character in the plain text calculate the corresponding ciphertext character
    for x in range(0, len(c)):
        if str.isalpha(c[x]):
            tmp = chr((ord(c[x].upper()) - ord(k[x])) % 26 + 65)
            if c[x].islower():
                p += tmp.lower()
            else:
                p += tmp.upper()
        else:
            p += c[x]
    return p


def fencrypt(fname, key):
    key = ''.join(filter(str.isalpha, key)).upper()
    oname = safe_fname("_ciphered".join(os.path.splitext(fname)))
    with open(fname, "r") as file, open(oname, "w") as output:
        output.write(encrypt(file.read(), key))
    return True


def fdecrypt(fname, key):
    key = ''.join(filter(str.isalpha, key)).upper()
    oname = safe_fname("_decrypted".join(os.path.splitext(fname)))
    with open(fname, "r") as file, open(oname, "w") as output:
        output.write(decrypt(file.read(), key))
    return True


