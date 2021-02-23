# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

number = int(input())
odict = OrderedDict()
for i in range(number):
    list_of_item = input().split(' ')
    price = int(list_of_item[-1])
    item_name = " ".join(list_of_item[:-1])
    if odict.get(item_name):
        odict[item_name] += price
    else:
        odict[item_name] = price

for i,v in odict.items():
    print(i,v)
