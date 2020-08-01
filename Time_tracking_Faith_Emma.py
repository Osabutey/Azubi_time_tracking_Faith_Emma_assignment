#!/usr/bin/python
from datetime import datetime
datearr=[] #create an array to store date
wage_per_hour = 5
client_name = input("Name of client: ")
task_name = input("What is the name of this task?: ")
started = input("When did "+task_name+" start? (YYYY-MM-DD HH:MM): ")
datearr.append(started)
end = input("When did "+task_name+" end? (YYYY-MM-DD HH:MM): ")
datearr.append(end)
print("Amazing, let us process your payroll now!")
format='%Y-%m-%d %H:%M'
try:
    startdate = datetime.strptime(datearr[0], format ) #convert string to datetime format
    #enddate = datetime.strptime(datearr[1], format)
    enddate= datetime.strptime(datearr[1], format )
    print ('So uhm ',startdate,'to ' , enddate," ")
    confirm = input("Did I get that right?Y/n: ")
    if confirm and confirm.lower()=="y":
        timediff = round(((enddate-startdate).total_seconds() / 3600), 2)
        wages = round((timediff * wage_per_hour), 2)
        print ('Okay it took ', timediff, 'hours so $5/hr for you comes to $'+str(wages))
    else:
        print("Aww snap. Please run me again and start from the top")
except Exception as e:
        print("Sorry but there was this issue with your entries!: "+e)




