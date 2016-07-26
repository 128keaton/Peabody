#!/bin/python
import subprocess, re, csv
bcmd="./get-names.sh"
cleanNames = []


result = subprocess.check_output(bcmd, shell=True)
uncleanNames = result.split("\n")
notGoodNames = ['2nd@go-eagles.org', 'kk@go-eagles.org', 'missioncontrol@go-eagles.org']
for name in uncleanNames:
        results = re.findall('^[\w\.]+@go-eagles.org', name)
        for item in results:
                if item not in cleanNames and item not in notGoodNames:
                    cleanNames.append(item)
cleanNames.sort()
with open("output.csv", "wb") as f:
	writer = csv.writer(f)
	writer.writerows(cleanNames)
	

for email in cleanNames:
    studentFullName = email.replace('@go-eagles.org', '')
    studentLastInitial = studentFullName[-1:]
    studentFullName = studentFullName[:-1]
    studentFullName = studentFullName.title()
    studentLastInitial = studentLastInitial.upper()
    studentFullName = studentFullName + " " + studentLastInitial + "."
	
    print("Student email: " + email + ". Student name: " + studentFullName)
	