import requests

class Pid:
    def __init__(self, team_id, szn):
        self.list = [] #initializing list 
        self.team_id = str(team_id) # this is to set the team id 
        self.szn = str(szn) #this is to set the nba season
        self.fname = [] #initializing list to later store first name of players
        self.lname = [] #initializing list to later store last name of players
        self.temp_fname = ""
        self.temp_lname = ""
        self.pid = 0   
        
    def get_player_id(self, player_name):
        url = "https://api-nba-v1.p.rapidapi.com/players"
        querystring = {"team":self.team_id,"season":self.szn}
        headers = {
	"X-RapidAPI-Key": "caceb7bb59mshd876c225d69680dp139934jsnd0bb9d630083",
	"X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
}
        response = requests.get(url, headers=headers, params=querystring)
        result = (response.json())
        ids =  (result["response"]) #this stores all the response data

        #Storing the players first name and last name
        temp_name = player_name.split() #placeholder to store the splitted player name
        if(len(temp_name)>1):
            self.temp_fname = temp_name[0] #placeholder to store the first name of the player
            self.temp_lname = temp_name[1] #placeholder to store the last name of the player
        else:
            self.pid = -1
            return self.pid

        #Storing all the player ids, first names and last names from a given team
        for c in range (len(ids)):
            self.list.append(ids[c]["id"])#storing all player ids for the given team
            self.fname.append(ids[c]["firstname"]) #storing first name of all players of given team
            self.lname.append(ids[c]["lastname"]) #storing last name of all players of given team

        #Returns the player id after going through player names
        for i in range (len(self.list)):
            #checks if player is found and then exits loop
            if (self.fname[i].lower() == self.temp_fname.lower() and self.lname[i].lower() == self.temp_lname.lower()):
                self.pid = self.list[i] # stores the pid of the given name
                break
            else:
                #player doesn't exist, id is set to -1
                self.pid = -1
        return self.pid
        
