c=0
k=0
n=1
while n!=0:
    n=int(input("Enter any number: "))
    if n%2==0:
        c=c+1
    else:
        k=0+1
print("The number of even numbers: ",c-1)
print("The number of odd numbers:  ",k)
