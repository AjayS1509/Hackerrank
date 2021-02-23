# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
n = input()
n_s = []
n_s = n.split(" ")
n1 = n_s[0]
n2 = int(n_s[1])
l1 = list(permutations(n1,n2))
final = []
a =""
for i in l1:
    for g in i:
        a += g
    final.append(a)
    a =""
final_2 = sorted(final)
for k in final_2:
    print(k)
