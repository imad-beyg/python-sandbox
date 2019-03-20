def square_list(list_numbers):
    square_list = []
    for list_number in list_numbers:
        square_list.append(calculate_sqaure(list_number))
    return square_list

def calculate_sqaure(x):
    return x*x

list_numbers = list(range(1,11))
print(square_list(list_numbers))

