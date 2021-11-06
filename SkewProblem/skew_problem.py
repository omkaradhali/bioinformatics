#genome = "CCGGCCGG"

def readFile():
    patternFile = open("dataset_3.txt", "r")

    file = patternFile.readlines()

    for index, line in enumerate(file):
        if index == 0:
            lineOne = line

    result = lineOne
    return result

def main():
    genome = readFile()
    print(genome)
    c_r = []
    sum = 0
    result = []
    for i in genome:
        if i == "C":
            sum = sum - 1
        if i == "G":
            sum = sum + 1
        c_r.append(sum)

    #print(min(c_r))

    print(min(c_r))

    min_value = min(c_r)
    for index, i in enumerate(c_r):
        if i == min_value:
            result.append(index+1)

    res_str = ""
    for val in result:
        res_str += str(val) + " "

    print(res_str)
    #print([i for i, x in enumerate(c_r) if x == min(c_r)])

if __name__ == "__main__":
    main()