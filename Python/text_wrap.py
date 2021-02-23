

def wrap(string, max_width):
    l = []
    c = 0
    k = 0
    m = max_width
    temp = ""
    final = ""
    h = len(string)//max_width
    for i in range(0,h):
        temp = string[k:m]
        k+= max_width
        m += max_width
        l.append(temp)

    if(len(string) %max_width != 0):
        o = len(string) // max_width
        f = (o*max_width)
        te = string[f:]
        l.append(te)
    for j in l:
        if(l[len(l)-1] != j):
            final += j+"\n"
        else:
            final += j
    return final
