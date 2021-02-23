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
    final = s1_n1
    for k in s2_n2:
        final.append(k)
    final_set = set(final)

    print(len(final_set))

main()
