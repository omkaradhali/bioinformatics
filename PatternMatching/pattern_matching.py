""" Need to make this readable through command line """

pat = "AA"
genome = "AAACATAGGATCAAC"


def pattern_matching(pattern, genome_string):
    pat_length = len(pattern)
    genome_length = len(genome_string)
    result = []

    for i in range(genome_length - pat_length + 1):
        count = 0
        for k in range(pat_length):
            if genome_string[i + k] == pattern[k]:
                count += 1

        if count == pat_length:
            result.append(i)

    print(result)
    return result

if __name__ == "__main__":
    print("hello there")
    result = pattern_matching(pat, genome)
    st = ""
    for i in result:
        st += str(i) + " "
    print(st)
