
def ngrams(c, n):
    output = {}
    for x in range(0, n):
        for y in range(x, int(len(c)/n)*n-n+1, n):
            gram = c[y:y+n]
            if gram in output:
                output[gram] += 1
            else:
                output[gram] = 1
        # Clean output (remove all single occurrences)
        for z in [key for key, val in output.items() if val == 1]:
            output.pop(z)
        # Sort output
        output = {k: v for k, v in sorted(output.items(), key=lambda item: item[1])}
    return output
