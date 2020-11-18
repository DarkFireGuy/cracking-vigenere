from scripts import frequency_analysis as frq
from scripts import DFGTools
from scripts import vigenere as vgn
from scripts import friedman as frd
from scripts import kasiski as ksk

bee = open('bee.txt').read()
cipher_bee = open('bee_ciphered.txt').read()

cipher_bee = frd.Friedman(cipher_bee)
ioc = cipher_bee.all_ioc_grouped

print(ioc)
print(cipher_bee)
