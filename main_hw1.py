my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

sorted_list = my_list[::]  # copy original list
sorted_list.sort()  # sort function to sort the list
pare = sorted_list[1::2]  # index 0 = 1, index 1 = 2. Even numbers every 2nd step starting from 1
impare = sorted_list[0::2]  # index 0 = 1, Odd numbers every 2nd step starting from 0
descendent = sorted_list.copy()  # copy sorted list
descendent.reverse()  # reverse function to reverse the list
descended_with_slices = sorted_list[-1::-1]  # copy from last element to first of the sorted list
multiples_of_three = sorted_list[2::3]


print('Original list: ' + str(my_list))
print(f'Sorted list (Ascending): {sorted_list}')
print('Sorted list (Descending): {}'.format(descendent))
print(f'Descending using slices: {descended_with_slices}')
txt = 'Even numbers'
print('{1}: {0}'.format(pare, txt))
print('{text}: {the_list}'.format(text='Odd numbers', the_list=impare))
print(f'Mutltiples of 3: {multiples_of_three}')
print(f'Original remained the same: {my_list}')
