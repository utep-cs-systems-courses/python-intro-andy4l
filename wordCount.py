import sys  # cmd args
import string

# arguments passed while executing program in shell
ffname = sys.argv[1]
oname = sys.argv[2]


def fileReader(filename, outputfile):
    f = open(filename, "r")
    o = open(outputfile, "w")
    w = dict()
    for line in f:
        # remove special characters that are integrated in words
        line = line.strip()
        line = line.replace('-', " ")
        line = line.replace("'", " ")
        # split words into list
        words = line.split()

        for word in words:
            # eliminate punctuation in each word
            word = word.translate(str.maketrans('', '', string.punctuation))
            word = word.lower()
            if word in w:
                w[word] = w[word] + 1
            else:
                w[word] = 1

    #   sorted used to sort keys in dictionary
    #   write dictionary output key by key to output file
    for key in sorted(w.keys()):
        o.write(key + " " + str(w[key]) + "\n")
    f.close()
    o.close()


def main():
    fileReader(ffname, oname)


main()
