import re
import matplotlib.pyplot as plt

def sortDict(letter_count):
    return(dict(sorted(letter_count.items())))


def getLetterCount(filename):
    letter_count = {} # dictionary to store letter count

    with open(filename) as file:
        for word in file:
            for s in word.lower(): 
                if re.match('[a-z]', s): # ensure we only match letters
                    if s in letter_count:
                        letter_count[s] += 1
                    else:
                        letter_count[s] = 1

    print(letter_count) 
    return(letter_count)


def createHistogram(letter_count):
    plt.bar(letter_count.keys(), letter_count.values())
    plt.show()

def main():
    filename = "/usr/share/dict/words" # /path/to/file
    try:
        letter_count = getLetterCount(filename) # count number of letters in file
        sorted_letter_count = sortDict(letter_count) # sort the dictionary
        createHistogram(sorted_letter_count) # produce visual histogram
    except:
        print("There was an error processing the file")
    

if __name__ == "__main__":
    main()