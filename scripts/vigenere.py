from scripts import kasiski, DFGTools
import os.path


class Vigenere:

    def test(self, key):
        return ''.join(filter(str.isalpha, key)).upper() == self.key

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
            tmp = kasiski.ngrams(self.cipher, x)
            if tmp:
                self.ngrams[x] = tmp

    def __str__(self):
        # Change this to something better
        return ("The plaintext \"%s\" was encrypted using the keyword \"%s\" to create the cipher text \"%s\"" %
                (self.plain, self.key, self.cipher))


def _v_enc_dec(inp, key, i):
    key = ''.join(filter(str.isalpha, key)).upper()
    # Creating the key stream (match plain's punctuation)
    tmp = key.upper()
    key = ''
    n = 0
    for x in inp:
        if str.isalpha(x):
            key += tmp[n % len(tmp)]
            n += 1
        else:
            key += x
    out = ''
    # Create output
    for x in range(0, len(inp)):
        # Only modify letters
        if str.isalpha(inp[x]):
            tmp = chr((ord(inp[x].upper()) + ord(key[x]) * i) % 26 + 65)
            # Make output match input's case
            if inp[x].islower():
                out += tmp.lower()
            else:
                out += tmp.upper()
        # Append any non letter without modification
        else:
            out += inp[x]
    return out


def encrypt(plain, key):
    # USAGE:
    # Plain: I like poo . poo. <3
    # Key: mElO
    # KeyStream: M ELOM ELO . MEL. <3
    # Cipher: U ptyq tzc . bsz. <3

    return _v_enc_dec(plain, key, 1)


def decrypt(cipher, key):
    # USAGE:
    # Cipher: U ptyq tzc . bsz. <3
    # Key: mElO
    # KeyStream: M ELOM ELO . MEL. <3
    # Plain: I like poo . poo. <3
    return _v_enc_dec(cipher, key, -1)


def fencrypt(fname, key):
    key = ''.join(filter(str.isalpha, key)).upper()
    oname = DFGTools.safe_fname("_ciphered".join(os.path.splitext(fname)))
    with open(fname, "r") as file, open(oname, "w") as output:
        output.write(encrypt(file.read(), key))
    return True


def fdecrypt(fname, key):
    key = ''.join(filter(str.isalpha, key)).upper()
    oname = DFGTools.safe_fname("_decrypted".join(os.path.splitext(fname)))
    with open(fname, "r") as file, open(oname, "w") as output:
        output.write(decrypt(file.read(), key))
    return True


def stylize(inp, length):
    inp = ''.join(filter(str.isalpha, inp)).upper()
    return ' '.join(inp[i:i + length] for i in range(0, len(inp), length))
