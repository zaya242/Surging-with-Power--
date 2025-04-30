a = int(input("Enter the number : "))
if a & (a-1) == 0:
    if a == 1:
        print("It is a power of 4")
        exit()
    elif a % 10 == 4 or a % 10 == 6:
        print("It is a power of 4")
    else:
        print("It is not a power of 4")

else:
    print("It is not a power of 4")               