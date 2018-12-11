a = [1,1,4,4,6,7,8,9,3,5,4,6,7,8,1,9]

def set_noDuplicate(list1):
    return list(set(list1))

print(set_noDuplicate(a))




def loop_noDuplicate(list2):
    list2 = []
    for elements in a:
        if elements not in list2:
            list2.append(elements)
    return list2

print(loop_noDuplicate(a))

