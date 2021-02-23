def average(array):
    # your code goes here
    change_int = []
    for j in range(0,len(arr)):
        change_int.append(int(arr[j]))
    final_set = set(change_int)
    total_sum = sum(final_set)

    final_result = total_sum/len(final_set)
    return  final_result
