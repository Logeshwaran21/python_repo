def string_formatting(k):
    de,oc,he,bi=[[str(i) for i in range(1, k + 1)],[oct(i)[2:] for i in range(1, k + 1)],[hex(i)[2:] for i in range(1, k + 1)],[bin(i)[2:] for i in range(1, k + 1)]]
    res=""
    for i in range(k):
        res += de[i] + "\t\t" + oc[i] + "\t\t" + he[i].upper() + "\t\t" + bi[i] + "\n"
    return res