def createLeague():
    leagueFile = open("european leagues.csv", "r")
    lines = leagueFile.readlines()[2:]
    leagueList = []
    for line in lines:
        line = line.rstrip("\n")
        team = line.split(",")
        leagueList.append(team)
    leagueFile.close()
    for scores in leagueList:
        winScores = int(scores[2]) * 3
        drawScores = int(scores[3])
        totalScores = winScores + drawScores
        scores.append(totalScores)
    return leagueList

def getTeam(fList,team):
    found = False
    pos = 0
    while pos < len(fList) and not found:
        if fList[pos][0] == team:
            found = True
            teamName = fList[pos][0]
            matches = fList[pos][1]
            wins = fList[pos][2]
            draws = fList[pos][3]
            losses = fList[pos][4]
            score = fList[pos][5]
        pos += 1
    if found:
        print("Team:", teamName, " Matches:", matches, " Matches Won:", wins,
              " Matches drawn:", draws, " Matches lost:", losses, " Score:", score)
    else:
        print("Team does not exist")
        
def getWinner(fList):
    highest = 0
    loss = 100
    winner = ""
    for i in range(len(fList)):
        number = fList[i][5]
        losses = int(fList[i][4])
        if number > highest:
            highest = number
            loss = losses
            winner = fList[i][0]
        elif number == highest and losses < loss:
            loss = losses
            winner = fList[i][0]
    return winner

def updateScores(team1,team2,result1,result2,fList):
    updatedData =[]
    for scores in fList:
        newMatches = int(scores[1]) + 1
        newWins = int(scores[2]) + 1
        newDraws = int(scores[3]) + 1
        newLoss = int(scores[4]) + 1
        newWinScore = newWins * 3
        newDrawScore = newDraws * 1
        if result1 > result2 and scores[0] == team1:
            scores[1] = str(newMatches)
            scores[2] = str(newWins)
            scores[5] = newWinScore
            updatedData.append(scores)
        elif result1 > result2 and scores[0] == team2:
            scores[1] = str(newMatches)
            scores[4] = str(newLoss)
            updatedData.append(scores)
        elif result2 > result1 and scores[0] == team2:
            scores[1] = str(newMatches)
            scores[2] = str(newWins)
            scores[5] = newWinScore
            updatedData.append(scores) 
        elif result2 > result1 and scores[0] == team1:
            scores[1] = str(newMatches)
            scores[4] = str(newLoss)
            updatedData.append(scores)
        elif result1 == result2 and scores[0] == team1:
            scores[1] = str(newMatches)
            scores[3] = str(newDraws)
            scores[5] = newScore
            updatedData.append(scores)
        elif result2 == result1 and scores[0] == team2:
            scores[1] = str(newMatches)
            scores[3] = str(newDraws)
            scores[5] = newScore
            updatedData.append(scores)
    print(updatedData)
    return fList
 

fbteams = createLeague()

loop = 1
while loop != 0:
    print("\nOption 1: Get team information",
          "\nOption 2: Display the current winner",
          "\nOption 3: Update Information of the team",
          "\nOption 0: Quit\n")
    choice = int(input("Please enter a numbered choice: "))
    if choice == 1:
        teamChoice = input("Enter a team: ")
        getTeam(fbteams, teamChoice)
    elif choice == 2:
        print("The current winner is: ", getWinner(fbteams))
    elif choice == 3:
        team1Choice = input("Please enter 1st team's name: ")
        team2Choice = input("Please enter 2nd team's name: ")
        goalsTeam1 = int(input("Please enter the amount of goals the first team has scored: "))
        goalsTeam2 = int(input("Please enter the amount of goals the second team has scored: "))
        updateScores(team1Choice,team2Choice,goalsTeam1,goalsTeam2,fbteams)
        print("Data has been updated")
    elif choice == 0:
        print("BYE")
        loop =0
    else:
        print("Invalid Choice")

            
        

