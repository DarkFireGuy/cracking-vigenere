from scripts import frequency_analysis as freqs, DFGTools
import string
import pathlib
from statistics import mean


class Friedman:

    def __init__(self, text):

        self.text = DFGTools.only_alpha(text)
        self.ioc = ioc(self.text)
        self.all_ioc_grouped = all_ioc(self.text, 2, 25)
        self.all_ioc = {}
        self.print_message_grouped = ''
        self.print_message = ''
        for x in self.all_ioc_grouped:
            self.print_message_grouped += "Key Length %d:\n" % x
            self.all_ioc[x] = mean(self.all_ioc_grouped[x].values())
            self.print_message += "Key Length %d: %.5f\n" % (x, self.all_ioc[x])
            for y in self.all_ioc_grouped[x]:
                self.print_message_grouped += "Group %d: %.5f\n" % (y, self.all_ioc_grouped[x][y])

    def __str__(self):
        return self.print_message


def ioc(text, normalize: bool = False):
    frq = list(freqs.freqs(string.ascii_uppercase, text).values())
    n = sum(frq)
    for x in range(0, len(frq)):
        frq[x] = frq[x] * (frq[x] - 1)
    frq = sum(frq)
    if normalize:
        return frq * 26 / (n * (n - 1))
    else:
        return frq / (n * (n - 1))


def all_ioc(text, min_length, max_length):
    text = DFGTools.only_alpha(text)
    output = {}
    # Dictionary with key as length
    for i in range(min_length, max_length + 1):
        # Dictionary with key as for group numbes
        output_ = {}
        split = splitter(text, i)
        for j in range(1, i + 1):
            output_[j] = ioc(split[j])
        output[i] = output_
    return output


def file_splitter(file_location, length):
    if length < 2:
        return False

    permissions = 0o755
    file = pathlib.Path(file_location)
    content = DFGTools.only_alpha(file.read_text())
    fname = file.stem
    fext = file.suffix
    p = pathlib.Path.cwd().joinpath(fname + '_splits', fname + "_n" + str(length))
    p.mkdir(mode=permissions, parents=True, exist_ok=True)

    # inside fname_length create files fname_1.txt, fname_2.txt, ... fname_length.txt
    for n in range(0, length):
        tmp_p = p.joinpath(fname + "_" + str(n + 1) + fext)
        tmp = ''
        for x in range(n, len(content), length):
            tmp += content[x]
        tmp_p.write_text(tmp)


def splitter(text, length):
    text = DFGTools.only_alpha(text)
    output = dict((k, '') for k in range(1, length + 1))
    for n in range(0, length):
        for x in range(n, len(text), length):
            output[n + 1] += text[x]
    return output
