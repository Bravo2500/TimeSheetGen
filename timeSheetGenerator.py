#Version 1.4 script now automatically edits the imacro script.

month = 4  
startDate = 6 
year = 2015 
count = 0 
week = ["mon","tue","wed","thr","fri"] 
day = 0 
outputList = [] 

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    monthEndDate = 31
else:
    monthEndDate = 30
   
if month == 2:
    monthEndDate = 28
 
while count < 10:
    date = str(month) + "_" + str(startDate) + "_" + str(year)
    outputList.append("TAG POS=1 TYPE=INPUT:TEXT FORM=ID:form1 ATTR=NAME:timeInHour1" + date + " CONTENT=8:30\nTAG POS=1 TYPE=INPUT:RADIO FORM=ID:form1 ATTR=NAME:timeInAMPM1" + date + " \nTAG POS=1 TYPE=INPUT:TEXT FORM=ID:form1 ATTR=NAME:timeOutHour1" + date + " CONTENT=12:30\nTAG POS=2 TYPE=INPUT:RADIO FORM=ID:form1 ATTR=NAME:timeOutAMPM1" + date + " \nTAG POS=1 TYPE=SELECT FORM=ID:form1 ATTR=NAME:svcName1" + date + "  CONTENT=%0_0_1974\nTAG POS=1 TYPE=INPUT:TEXT FORM=ID:form1 ATTR=NAME:timeInHour2" + date + "  CONTENT=12:30\nTAG POS=2 TYPE=INPUT:RADIO FORM=ID:form1 ATTR=NAME:timeInAMPM2" + date + " \nTAG POS=1 TYPE=INPUT:TEXT FORM=ID:form1 ATTR=NAME:timeOutHour2" + date + "  CONTENT=1:00\nTAG POS=2 TYPE=INPUT:RADIO FORM=ID:form1 ATTR=NAME:timeOutAMPM2" + date + " \nTAG POS=1 TYPE=SELECT FORM=ID:form1 ATTR=NAME:svcName2" + date + "  CONTENT=%1_0_1972\nTAG POS=1 TYPE=INPUT:TEXT FORM=ID:form1 ATTR=NAME:timeInHour3" + date + "  CONTENT=1:00\nTAG POS=2 TYPE=INPUT:RADIO FORM=ID:form1 ATTR=NAME:timeInAMPM3" + date + " \nTAG POS=1 TYPE=INPUT:TEXT FORM=ID:form1 ATTR=NAME:timeOutHour3" + date + "  CONTENT=5:00\nTAG POS=2 TYPE=INPUT:RADIO FORM=ID:form1 ATTR=NAME:timeOutAMPM3" + date + " \nTAG POS=1 TYPE=SELECT FORM=ID:form1 ATTR=NAME:svcName3" + date + "  CONTENT=%0_0_1974\n")
 
    if week[day] == "fri": 
        startDate +=3
        day = -1
    else:
        startDate += 1 
 
    if startDate > monthEndDate:
        startDate = startDate - monthEndDate
        month +=1
        
    day += 1
    count += 1

file = open("#Current.iim","w")
file.writelines(outputList)
file.close()
