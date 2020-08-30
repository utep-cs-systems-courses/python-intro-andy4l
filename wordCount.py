import sys  # cmd args
import string

ffname = sys.argv[1]
oname = sys.argv[2]


def sortDict(words):
    words = sorted(words.keys(), key=lambda x: x.lower())
    return words


def fileReader(filename, outputfile):
    f = open(filename, "r")
    o = open(outputfile, "w")
    w = dict()
    for line in f:
        line = line.strip()

        words = line.split(" ")
        # print(words)

        for word in words:
            word = word.translate(str.maketrans('', '', string.punctuation))
            if word in w:
                w[word] = w[word] + 1
            # if word in punc:
            #   words = words.
            else:
                w[word] = 1

    #   iterate and sort alphabetically through dictionary
    #   write dictionary output key by key to output file
    #sortedWords = sortDict(words)
    for key in sorted(w.keys()):
    #for key in sortedWords:
        o.write(key + " " + str(w[key]) + "\n")
        print(key, " ", w[key])
    f.close()
    o.close()


def main():
    fileReader(ffname, oname)


main()
