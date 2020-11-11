class Vigenere:

    def __init__(self, p, k):
        # Remove all non alphabetic characters and make them both upper case
        self.plain = ''.join(filter(str.isalpha, p)).upper()
        # Additionally, make key same length as plaintext if key is longer
        self.key = ''.join(filter(str.isalpha, k)).upper()[0:len(self.plain)]
        self.cipher = encrypt(self.plain, self.key)

    def __str__(self):
        return("The plaintext \"%s\" was encrypted using the keyword \"%s\" to create the cipher text \"%s\"" % (self.plain, self.key, self.cipher))


def encrypt(p, k):
    k = k.upper() * int(len(p) / len(k)) + k[0:len(p) % len(k)]
    c = ''; p=p.upper()
    for x in range(0, len(p)):
        c += chr((ord(p[x]) + ord(k[x])) % 26 + 65)
    return(c)

def decypt(c, k):
    k = k.upper() * int(len(c) / len(k)) + k[0:len(c) % len(k)]
    p = ''; c=c.upper()
    for x in range(0, len(c)):
        p += chr((ord(c[x]) - ord(k[x])) % 26 + 65)
    return(p)

