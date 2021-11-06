# dnaPattern = "CGTTGCATGTCGCATGATGCATGAGAGCT"
# windowSize = 4
store = {}
result = []
store_r = []


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
    multiple_combinations = []
    final_result = []

    for i in range(len(dnaPattern) - int(windowSize) + 1):
        store_pattern = ""
        for j in range(int(windowSize)):
            store_pattern += dnaPattern[i + j]

        store_r.append(store_pattern)


    pc = ["A", "C", "G", "T"]
    for item in store_r:
        print(item)
        res = []
        for i in range(len(item)):
            for n in pc:
                s = list(item)
                s[i] = n
                r = "".join(s)
                if not r in res:
                    res.append(r)
        print(res)
        multiple_combinations.append(res)
        m_c = [item for sublist in multiple_combinations for item in sublist]
        print(m_c)
        print(len(m_c))

    #print(len(multiple_combinations))
    #print(multiple_occ)
    for im in m_c:
        if im in store:
            store[im] = store[im] + 1
        else:
            store[im] = 1

    print(store)
    maximum = (max(store, key=store.get))
    print("---")
    print(maximum + " " + str(store[maximum]))

    for key, value in store.items():
        if store[key] == store[maximum]:
            final_result.append(key)


    #print(store_r)
    print(final_result)


def check_store(param):
    return True if param in store else False


if __name__ == "__main__":
    check_word_frequency()
