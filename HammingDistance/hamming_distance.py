
def readFile():
    patternFile = open("dataset_2.txt", "r")

    file = patternFile.readlines()

    for index, line in enumerate(file):
        if index == 0:
            lineOne = line
        if index == 1:
            lineTwo = line

    result = [lineOne, lineTwo]
    return result

def hamdist():
    data = readFile()
    str1 = data[0]
    str2 = data[1]
    diffs = 0
    for ch1, ch2 in zip(str1, str2):
        if ch1 != ch2:
            diffs += 1

    print(diffs)
    return diffs


if __name__ ==  "__main__":
    hamdist()