from freq_analysis import freqs
import string


def ioc(fname, normalize: bool = False):
    frq = list(freqs(string.ascii_uppercase, fname).values())
    n = sum(frq)
    for x in range(0, len(frq)):
        frq[x] = frq[x] * (frq[x] - 1)
    frq = sum(frq)
    if normalize:
        return frq*26 / (n*(n-1))
    else:
        return frq / (n*(n-1))