def cube_finder(number):
    cube_dictionary = {}
    for i in range(1,number+1):
        cube_dictionary[i] = get_cube(i)
    return cube_dictionary

def get_cube(number):
    return number**3

print(cube_finder(3))