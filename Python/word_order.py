"""def main():
    n = int(input())
    main_list = []
    f_list = []
    f = 1
    for i in range(0,n):
        s = input()

        if(i != 0):
            if(s in main_list):
                #print(s)
                temp = main_list.index(s)
                #print(temp)
                temp2 = f_list[temp]
                temp2 += 1
                #1print(temp2)
                #print(type(temp))
                #print(type(temp2))
                #print(f_list)
                f_list.pop(f_list[temp])
                f_list.insert(temp,temp2)

            else:
                main_list.append(s)
                f_list.append(f)
        else:
            main_list.append(s)
            f_list.append(f)
    total_len = len(f_list)
    freq = ""
    print(total_len)
    for i in f_list:
        if(len(f_list) == i):
            freq += str(i)
        else:
            freq +=str(i)
            freq += " "
    print(freq)



main()"""
from collections import OrderedDict
words = OrderedDict()

for _ in range(int(input())):
    word = input()
    words.setdefault(word, 0)
    words[word] += 1

print(len(words))
print(*words.values())
