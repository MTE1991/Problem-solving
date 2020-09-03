def valid_element(elements):
    removed = 0
    new_list = []
    for i in elements:
        if i not in new_list:
            new_list.append(i)
        elif i in new_list:
            repeat_count = new_list.count(i)
            if repeat_count < 2:
                new_list.append(i)
            else:    
                removed = i
    print(new_list)
    print('Removed:', removed)

valid_element([1, 2, 3, 3, 3, 3, 4, 5, 8, 8])

'''
Output:
[1, 2, 3, 3, 4, 5, 8, 8]
Removed: 3
'''
