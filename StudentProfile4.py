n=int(input("Enter number of students:"))
marks=[]
for i in range(n):
     marks.append(float(input(f"Enter marks of student:{i+1}")))
average=sum(marks)/n
print("---------------------")
print("Average Marks:",average)
print("Highest Marks:",max(marks))
print("Lowest Marks:",min(marks))
print("Pass",sum(m>=40 for m in marks))
print("Fail",sum(m<40 for m in marks))
