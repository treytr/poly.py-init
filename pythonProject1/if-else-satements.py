marks=int(input("Enter your marks scored"))

if marks>=80 and marks<= 100:
    print("You have scored an A")
elif marks>=60 and marks<= 79:
    print("You have scored a C")
elif marks>=40 and marks<=59:
    print("You have scored a D")
elif marks >= 0 and marks<=39:
    print("You have FAILED in life")
else:
    print("invalid marks value")