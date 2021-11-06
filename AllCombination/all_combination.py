
def generate_combination_n(n_size):
    pc = ["A", "C", "G", "T"]
    result = []
    for i in range(len(pc) - 1):
        i = pc[i] + pc[i+1]
        if not i in result:
            result.append(i)
        print(i)


def main():
    ip = "AAGC"
    pc = ["A", "C", "G", "T"]
    result = []

    temp = generate_combination_n(2)
    for i in range(len(ip)):
        for n in pc:
            s = list(ip)
            s[i] = n
            r = "".join(s)
            if not r in result:
                result.append(r)
            #print("".join(s))
            #result.append("".join(s))


    print(result)

if __name__ == "__main__":
    main()
