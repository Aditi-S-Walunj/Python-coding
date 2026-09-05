marks=[]
for i in range(1,6):
    mark=int(input("Enter marks of five subjects:"))
    marks.append(mark)
total=sum(marks)
average=total/5
percentage=float(total/500.0)*100.0
print("Percentage:",percentage,"%")
if percentage>=80 and percentage<=100:
    print("Grade=A & Status=Pass")
elif percentage>=60 and percentage<80:
    print("Grade=B & Status=Pass")
elif  percentage>=35 and percentage<60:
    print("Grade=C & Status=Pass")
else:
    print("Grade=F & Status=Fail")
                 
            
        
        
