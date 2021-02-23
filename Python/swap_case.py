def swap_case(s):
    final =""
    for i in s:
        if(i.isupper()):
            final += i.lower()
        elif(i.islower()):
            final += i.upper()
        else:
            final += i


    return final
