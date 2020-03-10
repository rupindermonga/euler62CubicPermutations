'''


The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.

'''
def CubicPermutations(x,y):
    # in our case: x is cube and y is the number of permutations (5)
    i = 2
    break_point = 0
    while True:
        new_list = []
        final_count = 0
        
        while True:
            if len(str(i**x)) == len(str((i-1)**x)) or i == break_point:
                new_list.append(i**x)
            elif len(new_list)<y:
                break_point = i
                break
            else:
                for j in range(len(new_list)):
                    count = 0
                    final_number = new_list[j]
                    final_list = []
                    str_to_check = str(final_number)
                    list_to_check = list(str_to_check)
                    list_to_check.sort()
                    for k in range(len(new_list)):
                        new_str = str(new_list[k])
                        new_list_to = list(new_str)
                        new_list_to.sort()
                        if list_to_check == new_list_to:
                            count += 1
                            final_list.append(new_list[k])
                            if count > y:
                                break
                    if count == y:
                        final_count = count
                        break
            if final_count == y:
                break
            else:
                i += 1
        if final_count == y:
            break        
    return final_list

final = CubicPermutations(3,5)
print(final)