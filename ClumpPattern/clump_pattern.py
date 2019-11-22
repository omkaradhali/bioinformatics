#dnaPattern = "CGTTGCATGTCGCATGATGCATGAGAGCT"
#windowSize = 4
store = {}
result = []

def readFile():
    patternFile = open("dataset_3.txt", "r")

    file = patternFile.readlines()

    for index, line in enumerate(file):        
        if index == 0:
            lineOne = line
        if index == 1:
            lineTwo = line

    result = [lineOne.strip("\n"), lineTwo.strip("\n")]
    return result

def check_word_frequency():

    result = []
    data = readFile()
    dnaPattern = data[0]
    windowSize = data[1].split(" ")
    print(windowSize)

    #dnaPattern = 
    l = []
    while dnaPattern:
        l.append(dnaPattern[:int(windowSize[1])])
        dnaPattern = dnaPattern[int(windowSize[1]):]

    windowLength = int(windowSize[1])

    for i in range(windowLength - int(windowSize[0]) + 1):
        if i == windowLength - 1:
            windowLength += windowLength
        
        
        store_pattern = ""
        for j in range(int(windowSize[0])):
            if(i + j < windowLength):
                store_pattern += dnaPattern[i+j]
        
        if check_store(store_pattern):
            store[store_pattern] = store[store_pattern] + 1
        else:
            store[store_pattern] = 1
        
#maximum = (max(store, key=store.get))

    for key, value in store.items():
        if(store[key] == int(windowSize[2])):
            result.append(key)
    result = list(dict.fromkeys(result))
        
    
    result_string = ""
    for item in result:
        result_string += item + " "
    #print(store)
    print(result_string)

def check_store(param):
    return True if param in store else False
    
if __name__ == "__main__":
    check_word_frequency()
    