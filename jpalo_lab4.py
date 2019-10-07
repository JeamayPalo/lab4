
#Problem 1 - TuitionIncrease

amount = 8000
count = 1
while(count<=5):
    amount += amount*0.03
    if(count == 1):
        print("In",count,"year, the tuition will be $",end="")
    else:
        print("In", count, "years, the tuition will be $",end="")
    print(amount)
    count += 1

#Problem 2 - Factorial

n = int(input("Enter a nonnegative integer:"))
while n<0:
     n = int(input("Enter a nonnegative integer:"))
factorial = 1
for i in range(1,n+1):
     factorial = factorial * i
print(factorial)

#Problem 3 - Triangle Pattern

n = int(input("Enter number of lines for pattern: "))
for i in range(n):
    print("#", end='')
    for j in range(i):
        print("#",end='')
    print("#")