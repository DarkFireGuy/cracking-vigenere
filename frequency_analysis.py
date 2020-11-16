import matplotlib.pyplot as plt
import string
import numpy as np
#Alpha: in this case, only uppercase
#Alpha-numerical: in this case, only numbers and uppercase
#All ASCII: in this case, only numbers, uppercase, and symbols

char_set = [string.ascii_uppercase, string.digits + string.ascii_uppercase, string.digits + string.ascii_uppercase + string.punctuation]
selection = 0
while selection not in [1,2,3]:
    selection = int(input("Frequency Analysis\nPlease choose from the following character sets:\n1) Alpha (Uppercase Only)\n2) Alpha-numerical (Uppercase and numbers only)\n3) All Ascii (Uppercase, numbers, and symbols only)\nPlease enter the number of your selection: "))

x = dict.fromkeys(list(char_set[selection-1]),  0)

fname = input("Enter the name of the file to be analyzed (include extension): ")
with open(fname) as file:
    for line in file:
        for char in line:
            if char in x:
                x[char] += 1
g = ''
while g.upper() not in ['YES', 'Y', 'N', 'NO']:
    g = input("Would you like the results to be sorted? (Y/N): ")
if g.upper() in ['YES', 'Y']:
    x = {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
    g = " (Sorted)"
else:
    g = ''
keys = x.keys()
vals = x.values()

# Makes the final graph larger
plt.figure(figsize=(12,9), dpi=300)

# Creates all the bars
plt.bar(keys, np.divide(list(vals), sum(vals)), label="File: " + fname + g)

# Adds a label above each bar for the value of the bar
for i in range(len(vals)):
    plt.annotate(str(round(np.divide(list(vals), sum(vals))[i]*100, 2)), xy=(list(keys)[i],np.divide(list(vals), sum(vals))[i]), fontsize=12, horizontalalignment='center')

# ticks = sorted((np(range(0, 10, 1)/10)).append(max(vals)/sum(vals)))
ticks = [x / 100 for x in range(0,100,5)]
ticks.append(max(vals)/sum(vals))
ticks = sorted(ticks)

plt.ylim(0, ticks[ticks.index(max(vals)/sum(vals)) + 1])
plt.ylabel('Proportion')
plt.xlabel('Character')
plt.xticks(list(keys))
plt.legend(bbox_to_anchor=(1, 1), loc="upper right", borderaxespad=0.)

plt.show()