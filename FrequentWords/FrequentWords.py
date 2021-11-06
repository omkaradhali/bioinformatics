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

    data = readFile()
    dnaPattern = data[0]
    windowSize = data[1]

    print(data[0])

    for i in range(len(dnaPattern) - int(windowSize) + 1):
        store_pattern = ""
        for j in range(int(windowSize)):
            store_pattern += dnaPattern[i+j]
        
        if check_store(store_pattern):
            store[store_pattern] = store[store_pattern] + 1
        else:
            store[store_pattern] = 1
    maximum = (max(store, key=store.get))
    
    for key, value in store.items():
        if(store[key] == store[maximum]):
            result.append(key)
        
    print(store)
    print(result)

def check_store(param):
    return True if param in store else False
    
if __name__ == "__main__":
    check_word_frequency()
    