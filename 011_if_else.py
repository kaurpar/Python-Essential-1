x=float(input("Enter your income: "))
if x<855528:
    tax=(0.18*x)-556.2
    if tax<0:
        tax = 0
        print("this is your", tax, "amount to be paid")
else:
            tax=14839+(0.32*(x-85528))
            print("this is your", tax, "amount to be paid")
        
        

    


