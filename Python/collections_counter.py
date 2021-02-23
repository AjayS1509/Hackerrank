# Enter your code here. Read input from STDIN. Print output to STDOUT
def remove_details(s1_s,val):
    s1_s.remove(val)
    return s1_s


def main():
    n = int(input())
    s = input()
    s1 = []
    total = 0
    s1 = s.split(" ")
    s1_s = []
    for i in s1:
        s1_s.append(int(i))

    #print(s1_s)
    cust = int(input())
    for i in range(0,cust):
        d1 =[]
        d = input()
        d1 = d.split(" ")
        if(int(d1[0]) in s1_s):
            s1_s = remove_details(s1_s,int(d1[0]))
            total += int(d1[1])
        else:
            pass

    print(total)
main()
