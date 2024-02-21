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
        #ids =  (x) #this stores all the players for that team
        #print(ids)
        

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
            #print(list)
        """

        print(temp_fname.lower()=="Luka".lower())
        print(temp_lname.lower()=="Doncic".lower())
        """

        
        #print (len(self.list)) #works
        count = 0 

        #Returns the player id after going through player names
        for i in range (len(self.list)):
            #print(self.fname[i]) #works
            #print(self.list) works
            #print (self.fname[i]) works
            #print(self.temp_fname)# works
            #print((self.fname[i].lower() == self.temp_fname.lower()),"\n") #works
            #Searches the players name, and returns the player id if player is found
            #print(self.list[i]) works
            #checks if player is found and then exits loop
            if (self.fname[i].lower() == self.temp_fname.lower() and self.lname[i].lower() == self.temp_lname.lower()):
                self.pid = self.list[i] # stores the pid of the given name
                break
            else:
                #player doesn't exist, id is set to -1
                self.pid = -1
                #pid = self.list[3] works
        return self.pid
        
#Testing if Pid works

"""
pid = Pid(17,2023)
print(pid.get_player_id("Lebron James"))
"""
                

#Works through input
#Response can't be looped, use sleep to loop it


#print(flag)


#Segregrate the search to first request team input from user, second player name, find id and begin visualization
#Create this as classes import or create obj use functions to return values
#42 players prop in an nba rooster

"""
    ch = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13',
      '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25',
      '26', '27', '28', '29', '30']
    tid = Tid()
    c = tid.get_team_id()
    
    querystring = {"team":"1","season":"2021"}
    headers = {
	"X-RapidAPI-Key": "caceb7bb59mshd876c225d69680dp139934jsnd0bb9d630083",
	"X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
}
    response = requests.get(url, headers=headers, params=querystring)
    result = (response.json())
    x =  (result["response"])
    ids =  (x[:-1])
    list = []
    flag = 0
    def get_player_id():
        for c in range (len(ids)):
            list.append(ids[c]["id"])
    #flag += 1
            #print(list)
            return(list)
"""
