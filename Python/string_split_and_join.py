def split_and_join(line):
    # write your code here
    s1 = []
    final_output = ""
    s1 = line.split(" ")
    for i in range(0,len(s1)):
        if(i != len(s1)-1):
            final_output += s1[i]
            final_output += "-"
        else:
            final_output += s1[i]
    return final_output
