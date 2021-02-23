def pop_details(list_details):
    list_details.pop()
    #print(list_details)
    return list_details

def remove_details(list_details,val):
    list_details.remove(val)
    return list_details


def discard_details(list_details,val):
    list_details.discard(val)
    return list_details


def main():
    n =  int(input())
    n_s_non_int = []
    mq = []
    main_list = []
    s = input()
    n_s_non_int = s.split(" ")
    for i in range(0,n):
        mq.append(int(n_s_non_int[i]))
    main_list = set(mq)

    #print(main_list)
    op_length = int(input())
    a = []
    le_s = []
    for k in range(0,op_length):
        le = input()
        a = le.split(" ")
        stat = a[0]
        val = 0
        if(stat == "pop"):
            main_list = pop_details(main_list)

        elif(stat =="remove"):
            val = int(a[1])
            if(val in main_list):
                main_list = remove_details(main_list,val)
            else:
                print('None')

        elif(stat == "discard"):
            val = int(a[1])
            main_list = discard_details(main_list,val)
        else:
            pass

    main_ans_sum = sum(main_list)
    print(main_ans_sum)

main()
