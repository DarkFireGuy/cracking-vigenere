import glob
import os.path


# Sorts a dictionary in ascending order based on values
def sort_dict(dictionary: dict):
    output = {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1])}
    return output


# Given a file name will return a name that does not conflict with an existing file

def safe_fname(fname):
    fname, fext = os.path.splitext(fname)
    tmp_name = fname + fext
    n = 1
    while does_it_exist(tmp_name):

        tmp_name = fname + "(" + str(n) + ")" + fext
        n += 1
    return tmp_name


def does_it_exist(name):
    return os.path.isdir(name) or os.path.isfile(name)
