def readFile():
    patternFile = open("dataset_4.txt", "r")

    file = patternFile.readlines()

    for index, line in enumerate(file):
        if index == 0:
            lineOne = line
        if index == 1:
            lineTwo = line
        if index == 2:
            lineThree = line

    result = [lineOne, lineTwo, lineThree]
    return result

def match_pat_with_skew():
    result = readFile()
    pat = result[0]
    genome = result[1]
    ham = result[2]
    indx = []
    di = {}

    start = 0

    for i in range(len(genome) - len(pat) + 1):
        diff = 0
        for k in range(len(pat) - 1):
            #print(genome[i+k] + " - " + pat[k])
            if genome[i + k] != pat[k]:
                diff += 1

        di[i] = diff


    for i in di.keys():
        if int(di[i]) == int(ham) or int(di[i]) <= int(ham):
            indx.append(i)

    res_str = ''

    for val in indx:
        res_str += str(val) + "  "

    print(res_str)
    print(len(indx))

if __name__ == "__main__":
    match_pat_with_skew()
