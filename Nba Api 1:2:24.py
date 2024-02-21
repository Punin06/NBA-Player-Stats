import requests
from matplotlib import pyplot as plt
from Tid import Tid
from Pid import Pid
from Season import Season

class Nba_api:
    def __init__(self):
        self.player_name = [] #initializing variable that will be used to store player name
        self.player_score = [] #initializing variable that will be used to store player stat
        self.pid = 0 #initializing variable to store player id
        self.tid = 0 #this one is to store team id
        self.season = 0 #to store the season to search for
        self.stat_line = "" #initializing stat line to decide what stat to display
        #creating max and min to store the max and min season
        self.max = 0
        self.min = 0
    
    def get_response(self):
        url = "https://api-nba-v1.p.rapidapi.com/players/statistics"
        querystring = {"id":str(self.pid),"season":str(self.season)}
        headers = {
	"X-RapidAPI-Key": "caceb7bb59mshd876c225d69680dp139934jsnd0bb9d630083",
	"X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
}
        response = requests.get(url, headers=headers, params=querystring)
        player_data = (response.json()) #Stores the player's data
        player_szn_data = player_data["response"] #Stores the player's season data
        return player_szn_data

#function to calculate season average number for the player.
    def get_player_stat(self, player_data, stat_line):
        #stores the returned player's season data
        player_szn_data = player_data
        player_game_data = player_szn_data
        #setting the stat line to search
        self.stat_line = stat_line
        
        #storing the player's name
        self.player_name.append(player_szn_data[0]["player"]["firstname"] + " " + player_szn_data[0]["player"]["lastname"])
        count = 0 #to count the number of games played
        sum  = 0 #to store the sum of the stat
        #loop to go through the players game and calc season average
        for v in range (len(player_game_data)):
            if(player_game_data[v][self.stat_line] == None):
                sum += 0
            else:
                #adding sum to later use to calc season average
                sum += int(player_game_data[v][self.stat_line])
                #count for number of games played
                count +=1
        #stores the player's season average
        self.player_score.append(sum/count)
        
#function to display the stats in the form of a bar chart
    def display_stat(self):        
     #prints the average for the szn
        bars = plt.bar(self.player_name, self.player_score, width = 0.5)
    #annotating all the bars
        for i, bar in enumerate(bars):
            plt.annotate(f'{round(self.player_score[i], 1)}', xy = ((bar.get_x() + bar.get_width()/2.0), self.player_score[i]), ha = "center", va = "bottom")

#function to call various other functions to get player id, team id and season.
    def call_functions(self):
        #variable to store last name of nba team
        lname = input("Enter last name of team ex: Celtics for Boston Celtics \n")
        #Creating object for class Tid
        tids =Tid()
        #calling the function to get team id and storing it
        self.tid = tids.get_team_id(lname) 
        
        #Validation to ensure the team name is found
        while self.tid == -1:
            lname = input("Please enter a valid last name of team ex: Celtics for Boston Celtics \n")
            self.tid = tids.get_team_id(lname)
            
        self.season = int(input("Enter a season: Ex: 2023 for the 2023 nba season \n"))

        #storing the max and min season values to find the range that can be searched
        self.min, self.max = Season().get_seasons()

        #input validation for seasons
        while (self.season < self.min) or (self.season > self.max):
            self.season = int(input(f"Please enter a season between {self.min} - {self.max}!\n"))

        #Creating object for class Pid
        pids = Pid(self.tid, self.season)
        name = input("Enter full player name, please exclude middle name! \n")
        #calling the function to get player id and storing it
        self.pid = pids.get_player_id(name)

        #Validation to ensure the player name is found
        while self.pid == -1:
            name = input("Please enter a valid full player name, please exclude middle name! Ex: Lebron James for Lebron James\n")
            self.pid = pids.get_player_id(name)
            
        
def main():
    api = Nba_api()
    #asking the number of players to search and storing it
    num = int(input("How many players do you want to search?\n "))
    
      #input validation for variable num
    while num < 1:
        num = int(input("Please enter a valid number of players to search?\n "))
        
    #asking the stat line to search for
    choice = int(input("Type 1 for points, 2 for rebounds, 3 for assists\n"))
    stat_line = ""
    
    #input validation for variable choice
    while choice < 1 or choice > 3:
        choice = int(input("Please type 1 for points, 2 for rebounds, 3 for assists!\n"))

    #conditionals to set stat line
    if choice == 1:
        #setting stat_line to search for points
        stat_line = "points"
    elif choice == 2:
        #setting stat_line to search for rebounds
        stat_line = "totReb"
    else:
        #setting stat_line to search for assists
        stat_line = "assists"
        
    #creating count to ensure all the players are searched
    count = 1
    
    while (num >= count):            
        api.call_functions()
        response = api.get_response()
        api.get_player_stat(response, stat_line)
        api.display_stat()
        #incrementing count
        count+=1

    #displaying the graph
    plt.show()
    
main()
    
"""
#make a function for this
querystring = {"id":str(pid),"season":str(season)} 

headers = {
	"X-RapidAPI-Key": "caceb7bb59mshd876c225d69680dp139934jsnd0bb9d630083",
	"X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

player_stats = (response.json()) #it's got buddy hields stats for the 2020 szn

c = player_stats["response"]


x = (c[:-1]) # stores 0 to n-1
"""




    #this is a list where the first index refers to the game,
    #it fetches the date for that game, so x[0] gets the data for the first game for that player in that szn


"""
Important keywords of stats
points
offReb
defReb
totReb
fgm
fga
ftm
fta
pos
min
assists
steals
turnovers
blocks
plusMinus
pFouls
ftp
"""

#Create a way to find players through user input and fetch stats,
#nba.com doesn't have the id, use rapidapi page for this api
#data visualizations for stats, allow comparison btw different players, start with smth basic, ex: pts
#This uses player id to find players
