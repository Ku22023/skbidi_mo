def max_of_three(a,b):
    if a >= b:
        print(f"{a} is bigger than {b}")
    elif a <= b:
        print(f"{b} is bigger than {a}")

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
max_of_three(a,b)

