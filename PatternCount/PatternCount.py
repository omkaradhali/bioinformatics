def readFile():
    patternFile = open("dataset_4.txt", "r")

    file = patternFile.readlines()

    for index, line in enumerate(file):        
        if index == 0:
            lineOne = line
        if index == 1:
            lineTwo = line

    result = [lineOne.strip("\n"), lineTwo.strip("\n")]
    return result

def count(longString, pattern):
    windowPatern = len(pattern)
    windowString = len(longString)
    finalCount = 0
    
    for i in range(windowString - windowPatern + 1):
        j = 0
        for j in range(windowPatern):
            if(longString[i+j] != pattern[j]):
                break

            if(j == windowPatern - 1):
                    finalCount += 1

    return finalCount 
    

def find_pattern():
    result = readFile()
    print(count(result[0], result[1]))

if __name__ == "__main__":
    find_pattern()
