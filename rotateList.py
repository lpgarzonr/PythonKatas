def rotate(my_list, num_rotations):
    counter = 1
    lastIdx = len(my_list)-1
    while counter <= num_rotations:
        tmp = my_list[0]
        my_list[0] = my_list[lastIdx]
        my_list[lastIdx] = tmp
        counter+=1
    return my_list
  
l = ['a', 'b', 'c', 'd', 'e', 'f']
print(rotate(l, 0))
print(rotate(l, 1))
print(rotate(l, 3))
print(rotate(l, 9))
