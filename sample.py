def num_print(a, b):
    if (a > 0 and a <= b):
        print("The counting is : ", a)
        inc = a+1
        num_print(inc, b)

num = float(input("Enter the starting number : "))
y = float(input("Enter the ending number : "))
num_print(num, y)
