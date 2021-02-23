

# Complete the solve function below.
def solve(s):
    l = []
    n_l = []
    l = s.split(" ")
    for i in l:
        t =""
        for j in range(0,len(i)):
            if( j == 0):
                t += i[j].upper()
            else:
                t += i[j]
        n_l.append(t)
    final = ""
    for k in range(0,len(n_l)):
        if(k != len(n_l)-1):
            final += n_l[k]
            final += " "
        else:
            final += n_l[k]
    return final
