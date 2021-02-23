
def main():
    n =  int(input())
    s = []
    for i in range(0,n):
        le = input()
        s.append(le)

    final_set = set(s)
    final_set_length = len(final_set)

    print(final_set_length)



main()
