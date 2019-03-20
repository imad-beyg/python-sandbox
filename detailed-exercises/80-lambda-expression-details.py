#normal
def is_even(a):
    return a%2 == 0

#lambda
is_lambda_even = lambda a : a%2==0


#normal
def last_char(string):
    return string[-1]

#lambda
get_last_char = lambda string : string[-1]


#testing values
print(is_even(4))
print(is_lambda_even(6))     

print(last_char("Imad"))
print(get_last_char("Beyg"))



#if else in lambda expressions

func = lambda a : True if len(a) > 5 else False
print(func("Imad Beyg"))