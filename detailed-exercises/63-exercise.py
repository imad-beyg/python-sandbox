# define a function that take list of strings 
# list containing reverse of every string
 
# NOTE - USE LIST COMPREHENSION because we already did this exercise 
# using normal method
 
# example 
# l = ['abc', 'tuv', 'xyz']
# reverse_string(l) ----> ['bac', 'vut', 'zyx']

def reverse_string(names):
    reverse_list = []
    for name in names:
        reverse_list.append(name[::-1])
    return reverse_list


def reverse_string_list_comprehension(names):
    reverse_list = [name[::-1] for name in names]
    return reverse_list


l = ['imad','beyg','sundas','zia']
print(reverse_string(l))
print(reverse_string_list_comprehension(l))