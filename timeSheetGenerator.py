month = 2
startDate = 23
year = 2015
count = 0
week = ["mon","tue","wed","thr","fri"]
day = 0
 
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    monthEndDate = 31
else:
    monthEndDate = 30
   
if month == 2:
    monthEndDate = 28
 
while count < 10:
    date = str(month) + "_" + str(startDate) + "_" + str(year)
    output = "TAG POS=1 TYPE=SELECT FORM=NAME:form1 ATTR=NAME:timeInHour1" + date + " CONTENT=%08:30\nTAG POS=1 TYPE=SELECT FORM=NAME:form1 ATTR=NAME:timeInAMPM1" + date + " CONTENT=%AM\nTAG POS=1 TYPE=SELECT FORM=NAME:form1 ATTR=NAME:timeOutHour1" + date + " CONTENT=%12:30\nTAG POS=1 TYPE=SELECT FORM=NAME:form1 ATTR=NAME:timeOutAMPM1" + date + " CONTENT=%PM\nTAG POS=1 TYPE=SELECT FORM=NAME:form1 ATTR=NAME:timeInHour2" + date + " CONTENT=%12:30\nTAG POS=1 TYPE=SELECT FORM=NAME:form1 ATTR=NAME:timeInAMPM2" + date + " CONTENT=%PM\nTAG POS=1 TYPE=SELECT FORM=NAME:form1 ATTR=NAME:timeOutHour2" + date + " CONTENT=%01:00\nTAG POS=1 TYPE=SELECT FORM=NAME:form1 ATTR=NAME:timeOutAMPM2" + date + " CONTENT=%PM\nTAG POS=1 TYPE=SELECT FORM=NAME:form1 ATTR=NAME:svcName2" + date + " CONTENT=%1_0_1972\nTAG POS=1 TYPE=SELECT FORM=NAME:form1 ATTR=NAME:svcName1" + date + " CONTENT=%0_0_1974\nTAG POS=1 TYPE=SELECT FORM=NAME:form1 ATTR=NAME:timeInHour3" + date + " CONTENT=%01:00\nTAG POS=1 TYPE=SELECT FORM=NAME:form1 ATTR=NAME:timeInAMPM3" + date + " CONTENT=%PM\nTAG POS=1 TYPE=SELECT FORM=NAME:form1 ATTR=NAME:timeOutHour3" + date + " CONTENT=%05:00\nTAG POS=1 TYPE=SELECT FORM=NAME:form1 ATTR=NAME:timeOutAMPM3" + date + " CONTENT=%PM\nTAG POS=1 TYPE=SELECT FORM=NAME:form1 ATTR=NAME:svcName3" + date + " CONTENT=%0_0_1974"
 
    if week[day] == "fri":
        startDate +=3
        day = -1
    else:
        startDate += 1
 
    if startDate > monthEndDate:
        startDate = startDate - monthEndDate
        month +=1
 
    print(output)
    day += 1
    count += 1
