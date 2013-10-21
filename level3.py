
def level3():
    with open('level3.txt') as f:
        line = f.readline().rstrip()
        result = []
        while line:
            line = list(line)
            for i in range(3, len(line)-3):
                if line[i].islower() and \
                    str(line[i-3: i]).isupper() and \
                    str(line[i+1: i+4]).isupper() and\
                    line[i-4].islower() and line[i+4].islower():
                    result.append(line[i])
            line = f.readline().rstrip()
        return result

print ''.join(level3())
