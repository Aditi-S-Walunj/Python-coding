marks=[]
for i in range(1,6):
    mark=int(input("Enter marks of five subjects:"))
    marks.append(mark)
total=sum(marks)
average=total/5
percentage=float(total/500.0)*100.0
while True:
    print("\n1.Calculate Result")
    print("2.Display Grade")
    print("3.Display Status")
    print("4.Performance Summary")
    print("5.Exit")
    choice=int(input("Enter choice:"))
    if choice==1:
        print("---------------------")
        print("Result")
        print("Total Marks:",total)
        print("Percentage:",percentage,"%")
    elif choice==2:
        print("---------------------")
        if percentage>=80 and percentage<=100:
            print("Grade=A")
        elif percentage>=60 and percentage<80:
            print("Grade=B")
        elif  percentage>=35 and percentage<60:
            print("Grade=C")
        else:
            print("Grade=F")
    elif choice==3:
        print("---------------------")
        if percentage>=35:
            print("Status=Pass")
        else:
            print("Status=Fail")
    elif choice==4:
        print("-----Performance Summary-----")
        print("Result")
        print("Total Marks:",total)
        print("Percentage:",percentage,"%")
        if percentage>=80 and percentage<=100:
            print("Grade=A")
        elif percentage>=60 and percentage<80:
            print("Grade=B")
        elif  percentage>=35 and percentage<60:
            print("Grade=C")
        else:
            print("Grade=F")
            if percentage>=35:
                print("Status=Pass")
            else:
                print("Status=Fail")
    elif choice==5:
        print("---------------------")
        print("Exit")
        break
    else:
        print("Invalid choice")
            

