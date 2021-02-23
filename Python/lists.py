def insert(list_details,tat,pos,val):
    list_details.insert(pos,val)
    return list_details

def print_details(list_details):
    print(list_details)

def remove_details(list_details,val):
    list_details.remove(val)
    return list_details

def append_deatils(list_details,val):
    list_details.append(val)
    return list_details

def sort_details(list_details):
    list_details.sort()
    return list_details

def pop_details(list_details):
    list_details.pop()
    return list_details

def reverse_details(list_details):
    list_details.reverse()
    return list_details







if __name__ == '__main__':
    N = int(input())
    main_list = []
    for i in range(0,N):
        s = input()
        s1 = s.split(" ")
        pos = 0
        val = 0
        stat = s1[0]
        #pos = s1[1]
        #val = s1[2]
        if(stat == "insert"):
            pos = int(s1[1])
            val = int(s1[2])
            main_list =  insert(main_list,stat,pos,val)
        elif(stat == "print"):
            print_details(main_list)
        elif(stat == "remove"):
            val = int(s1[1])
            main_list = remove_details(main_list,val)
        elif(stat == "append"):
            val = int(s1[1])
            main_list = append_deatils(main_list,val)

        elif(stat == "sort"):
            main_list = sort_details(main_list)

        elif(stat == "pop"):
            main_list = pop_details(main_list)

        elif(stat == "reverse"):
            main_list = reverse_details(main_list)
        else:
            pass
