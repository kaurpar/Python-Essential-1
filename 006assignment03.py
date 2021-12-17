hr1=int(input("Give me the start time hour:"))
min1=int(input("Give me the start time minute:"))
dt=int(input("Give me the duration in minutes:"))
ft=hr1*60+min1+dt
hr2=ft//60
min2=ft-hr2*60
print("The finish time is=",hr2,":" ,min2)
