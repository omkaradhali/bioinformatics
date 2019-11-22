def readFile():
    patternFile = open("dataset_3.txt", "r")

    file = patternFile.readlines()

    for index, line in enumerate(file):        
        if index == 0:
            lineOne = line
        if index == 1:
            lineTwo = line

    result = [lineOne.strip("\n")]
    return result

def reverse_compliemnt_pattern():

    result = readFile()
    pat = result[0]
    output = []

    
    for i in pat:
        if( i == 'A'):
            output.append('T')
        if(i == "G"):
            output.append('C')
        if( i == "C"):
            output.append("G")
        if( i == "T"):
            output.append("A")
    print(''.join(output[::-1]).replace("\n",""))
    print(len(pat))
    print(len(''.join(output[::-1])))

if __name__ == "__main__":
    reverse_compliemnt_pattern()