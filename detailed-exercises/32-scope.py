x = 4 #global variable

def func():
    global x
    x = 7
    return 7

print(x)
print(func())
print(x)
