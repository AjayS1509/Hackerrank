# Enter your code here. Read input from STDIN. Print output to STDOUT
def main():
    n1 = int(input())
    s = input()
    s1 = [str(i) for i in s.split(" ")]
    s1_n1 = []
    for j in s1:
        s1_n1.append(int(j))
    n2 = int(input())
    p = input()
    s2 = [str(i) for i in p.split(" ")]
    s2_n2 = []
    for j in s2:
        s2_n2.append(int(j))
    #print(s2_n2)
    final = []
    for i in s1_n1:
        for j in s2_n2:
            if(i == j):
                final.append(i)
            else:
                pass


    print(len(final))

main()
