# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
n1 = input()
n2 = input()
n1_s = [str(i) for i in n1.split(" ")]
n2_s = [str(j) for j in n2.split(" ")]
n1_i1 = []
n2_i2 = []
for k in n1_s:
    n1_i1.append(int(k))
for k in n2_s:
    n2_i2.append(int(k))
l1 = list(product(n1_i1,n2_i2))
final = ""
for i in l1:
    final += str(i)
    final += " "
print(final)
