
def level1(s):
    lst = list(s)
    for i in range(len(lst)):
        c = ord(lst[i])
        if c >= ord('a') and c <= ord('z'):
            new_c = c + 2
            if new_c > ord('z'):
                new_c = new_c - (ord('z') - ord('a')) - 1
            lst[i] = chr(new_c)
    return ''.join(lst)

s0 = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
s1 = 'map'
print level1(s0)
print level1(s1)
