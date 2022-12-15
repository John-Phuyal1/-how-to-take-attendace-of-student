import os
import csv
os.system('cls')
totalStudent= int(input("Enter the total number of student"))
list1=[]
for i in range(totalStudent):
    list1.append(input("Enter the name of {} student".format(i+1)))
attendance = {


}
def takeAttendance():
    for val in list1:
        userInput = input("Is {} present".format(val))
        while (userInput.upper() !='A' and userInput.upper()!='P'):
            userInput1 = input("Is {} present".format(val))
            userInput=userInput1
        attendance[val]=userInput
    print (attendance)


def writeTo_file():
    takeAttendance()
    file=open("Attendance.csv","w")
    coloum=["name",attendance]
    writer = csv.writer(file)
    #write colum header first
    writer.writerow(coloum)
    for key in attendance.keys():
        #make list such as [ name,attendance]
        writer.writerow([key,attendance[key]])
    file.close()
writeTo_file()        
