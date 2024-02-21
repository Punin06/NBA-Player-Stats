import requests
class Season:
    def __init__(self):
      self.max_season = 0
      self.min_season = 0
#function to get the response data 
    def get_data(self):
        url = "https://api-nba-v1.p.rapidapi.com/seasons"
        headers = {
	"X-RapidAPI-Key": "caceb7bb59mshd876c225d69680dp139934jsnd0bb9d630083",
	"X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers)
        data = response.json()
        return data
    
    #function to return max and min season    
    def get_seasons(self):
        data = Season().get_data()
        season = data["response"]
        self.max_season = max(season)
        self.min_season = min(season)
        return self.min_season, self.max_season

