eligible=0
for i in range(10):
    attendence=int(input("Enter attendence:"))
    if attendence==-1:
        break
    if attendence>=75:
        print("Eligible")
        eligible+=1
    else:
        print("Not Eligible")
print("Total Eligible Employees:",eligible)
        
