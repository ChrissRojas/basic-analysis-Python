"""
This functions takes a list as a paremter and calculates which
departments had more than 60% where people voted for good.
It then outputs a list of those departments.
"""
def displayExPerf(sList):
    highList = []
    total = 0
    total2 = 0
    for department in sList:
        good = int(department[1]) 
        fair = int(department[2]) 
        bad = int(department[3])
        total += good + fair + bad
        total2 += good
        highTotal = total2/total
        total = 0
        total2 = 0
        if highTotal >= 0.6:
            highList.append(department[0])
    print("Departments with high survey rates= ", highList)



"""
The function uses a list to calculate which departments had 50% or more customers
voted for fair or poor. It then returns a list of those departments 
"""
def displayPoorPerf(sList):
    poorList = []
    total = 0
    total2 = 0
    for department in sList:
        good = int(department[1]) 
        fair = int(department[2]) 
        bad = int(department[3])
        total += good + fair + bad
        total2 += fair + bad
        poorTotal = total2/total
        total = 0
        total2 = 0
        if poorTotal >= 0.5:
            poorList.append(department[0])
    print("Departments with low survey rates= ", poorList)
    



"""
The functions takes a list as a parameter.
Calculates the weighted average of each department, value is rounded.
Then the average is compared to the lowest current average.
Returns the lowest average.
"""
def displayLowest(sList):
    lowest = 4
    total = 0
    total2 = 0
    lowestDepart = ""
    for department in sList:
        good = int(department[1]) * 3
        fair = int(department[2]) * 2
        bad = int(department[3])
        total += good + fair + bad
        total2 += int(department[1]) + int(department[2]) + int(department[3])
        average = round(total/total2,2)
        total = 0
        total2 = 0
        if average < lowest:
            lowest = average
            lowestDepart = department
    print("The department with lowest customer satisfaction rate is: ", lowestDepart[0])

"""
Takes a list as a parameter.
Calculates and compares the highest average
returns the department with the highest department 
"""
def displayHighest(sList):
    highest = 0
    total = 0
    total2 = 0
    highestDepart = ""
    for department in sList:
        good = int(department[1]) * 3
        fair = int(department[2]) * 2
        bad = int(department[3])
        total += good + fair + bad
        total2 += int(department[1]) + int(department[2]) + int(department[3])
        average = round(total/total2,2)
        total = 0
        total2 = 0
        if average > highest:
            highest = average
            highestDepart = department
    print("The department with highest customer satisfaction rate is: ", highestDepart[0])
 
"""
Takes an input and a list as a parameter.
Calculates the average of the given department.
prints out the average of that given department.
"""

def calAvgByDep(sList, department):
    found = False
    pos = 0
    total = 0
    total2= 0
    while pos < len(sList) and not found:
        if sList[pos][0] == department:
            found = True
            good = int(sList[pos][1])* 3
            fair = int(sList[pos][2])* 2
            bad = int(sList[pos][3])
            total += good + fair + bad
            total2 += int(sList[pos][1]) + int(sList[pos][2]) + int(sList[pos][3])
        pos += 1
    if found:
        print("The average of this department",round(total/total2,2))
    else:
        print("Department does not exist")

"""
Takes an input and a list as a parameter.
Sums up the total of the given department.
prints out the total of that given department.
"""

def calTotalByDep(sList,department):
    found = False
    pos = 0
    total = 0
    while pos < len(sList) and not found:
        if sList[pos][0] == department:
            found = True
            good = int(sList[pos][1])
            fair = int(sList[pos][2])
            bad = int(sList[pos][3])
            total += good + bad + fair
        pos += 1
    if found:
        print("The amount of people who have answered the survey for this department is: ",total) 
    else:
        print("Department does not exist")

"""
takes a list as a parameter and calculates the whole weighted average
and returns the average
"""
def calcAvg(sList):
    number = calcTotal(sList)
    total2 = 0
    for i in range(len(sList)):
        good = int(sList[i][1]) * 3
        fair = int(sList[i][2]) * 2
        bad = int(sList[i][3])
        total2 += good + fair + bad
    average = total2 / number
    return average 

"""
Takes a list and sums up the whole total.
returns that total
"""
def calcTotal(sList):
    total = 0
    for i in range(len(sList)):
        total += int(sList[i][1])
        total += int(sList[i][2])
        total += int(sList[i][3])
    return total
                
"""
Reads the file and returns each line in that file
"""
def displayData():
    surveyFile = open("survey.txt","r")
    survey = surveyFile.read()
    surveyFile.close()
    return survey


"""
Reads the file and inputs each line in the list.
returns that list.
"""
def readData():
    surveyFile = open("survey.txt", "r")
    surveyList = []
    for line in surveyFile:
        surveys = line.split()
        surveyList.append(surveys)
    surveyFile.close()
    return surveyList


"""
Displays the menu
"""
def menu():
    print("\nOption 1: display menu",
          "\nOption 2: display All survey information",
          "\nOption 3: Given department's total survey participants and average",
          "\nOption 4: Display the department with the highest average customer satisfaction",
          "\nOption 5: Display the department with the lowest average customer satisfaction",
          "\nOption 6: Displays the departments for which 50% or more customers voted fair or poor",
          "\nOption 7: Displays the departments for which 60% or more customers voted good",
          "\nOption 8: Displays the number of customers who used the customer satisfaction device and total average of the responses",
          "\nOption 0: Quit")

"""
This prompts the user for a choice and performs the function that is assigned
to that choice. It will keep asking until the user enters 0, which stops the
program from running.
"""
theSurveyList = readData()
menu()
loop = 1
while loop != 0:
    choice = int(input("Please enter a choice: "))
    if choice == 1:
        menu()
    elif choice == 2:
        print(displayData())
    elif choice == 3:
        department = input("Please enter a department: ")
        calTotalByDep(theSurveyList, department)
        calAvgByDep(theSurveyList, department)
    elif choice == 4:
        displayHighest(theSurveyList)
    elif choice == 5:
        displayLowest(theSurveyList)
    elif choice == 6:
        displayPoorPerf(theSurveyList)
    elif choice == 7:
        displayExPerf(theSurveyList)
    elif choice == 8:
        print("The total amount of people who used the devices and partook in the survey:",calcTotal(theSurveyList))
        print("The total weighted average of this survey",calcAvg(theSurveyList))
    elif choice == 0:
        loop = 0
        print("Bye")
    else:
        print("invalid choice")
            
          
          









