from vigenere import *
# import kasiski as ksk
# import ioc_friedman as ioc
import freq_analysis as frq
from tools import *


fencrypt("bee.txt", "BEEMOVIEISAMEME")
frq.plot_alpha("bee_ciphered.txt", "bee_ciphered.png", False)