def rem_duplicate(t):
    t_list = list(t) # convert tuple to list
    return tuple(list(dict.fromkeys(t_list)))

print(rem_duplicate((1,1,1,2,3,4,5,6,6,6,6,4,0,0,0)))

# Output: (1, 2, 3, 4, 5, 6, 0)
