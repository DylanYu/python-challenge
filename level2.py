
def level2():
    with open('level2.txt') as f:
        dic = {}
        count = 0
        line = f.readline().rstrip()
        while line:
            for c in line:
                count += 1
                if c in dic:
                    dic[c] += 1
                else:
                    dic[c] = 1
            line = f.readline().rstrip()
        avg = count / len(dic)
        #return sorted(dic.items(), lambda x, y: cmp(x[1], y[1]))
        return ''.join([c for c in dic if dic[c] < avg])

print level2()
