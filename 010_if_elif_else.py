y=int(input("Give me a year: "))
if    y<1582:
    print("Not within Gergorian Calendar")
elif     y%4:
    print("Common Year")
elif    y%100:
     print("leap year")
elif y%400:
    print("Common Year")
else:
    print("leap year")
