num = int(input("Enter number to check :"))

if num>50:
    print("number is greater than 50")
    if num%2==0:
        print("And it is even too")
    else:
        print("And it is odd too")

else:
    print("Number is less than 50")