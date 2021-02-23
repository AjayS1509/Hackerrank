def alpanumeric_contain(s):
    c4 = 0
    for i in range(0,len(s)):
        if(s[i].isalnum()):
            c4 += 1
        else:
            pass
    if(c4 != 0):
        return True
    else:
        return False

def alphabet_contain(s):
    c3 = 0
    for i in range(0,len(s)):
        if(s[i].isalpha()):
            c3 += 1
        else:
            pass
    if(c3 != 0):
        return True
    else:
        return False


def digit_contain(s):
    c2 = 0
    for i in range(0,len(s)):
        if(s[i].isdigit()):
            c2 += 1
        else:
            pass
    if(c2 != 0):
        return True
    else:
        return False

def lowercase_contain(s):
    c = 0
    for i in range(0,len(s)):
        if(s[i].islower()):
            c += 1
        else:
            pass
    if(c != 0):
        return True
    else:
        return False

def uppercase_contain(s):
    c1 = 0
    for i in range(0,len(s)):
        if(s[i].isupper()):
            c1 += 1
        else:
            pass
    if(c1 != 0):
        return True
    else:
        return False





if __name__ == '__main__':
    s = input()

    a1 = alpanumeric_contain(s)
    a2 = alphabet_contain(s)
    a3 = digit_contain(s)
    a4 = lowercase_contain(s)
    a5 = uppercase_contain(s)
    print(a1)
    print(a2)
    print(a3)
    print(a4)
    print(a5)
