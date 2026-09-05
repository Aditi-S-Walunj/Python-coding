marks=[]
for i in range(1,6):
    mark=int(input("Enter marks of five subjects:"))
    marks.append(mark)
total=sum(marks)
average=total/5
percentage=float(total/500.0)*100.0
print("---------------------")
print("Total Marks:",total)
print("Average Marks:",average)
print("Percentage:",percentage,"%")
print("Highest Marks:",max(marks))
print("Lowest Marks:",min(marks))
