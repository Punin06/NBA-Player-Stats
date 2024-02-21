import requests

class Tid:
    def __init__(self):
        self.nickname = [] #initializing list to later store nicknames of teams
        self.teamid = [] #initializing list to later store teamid of teams
        #self.nbaFranchise = [] #initializing list to later store the values of nbaFranchise key
        #of teams that can be used to check if team is an nba franchise
        self.teams = [] #initializing a list that will be used to store teams

    def get_team_id(self, lname):
        url = "https://api-nba-v1.p.rapidapi.com/teams"
        headers = {
	"X-RapidAPI-Key": "caceb7bb59mshd876c225d69680dp139934jsnd0bb9d630083",
	"X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
}
        response = requests.get(url, headers=headers)
        temp = response.json()
        self.teams = temp["response"] #stores all the teams data
        #goes through teams to find nba franchise teams, stores their names and id
        for i in range(len(self.teams)):
            if(self.teams[i]["nbaFranchise"]==True):
                self.nickname.append(self.teams[i]["nickname"])
                self.teamid.append (self.teams[i]["id"])
        id = 0
        #finds the team id and returns it
        for i in range(len(self.nickname)):
            #print(nickname[i])
            if(lname.lower() == self.nickname[i].lower()):
                id = self.teamid[i]
                break
            else:
                #team does not exists, id is set to -1
                id = -1
        return id
