import requests
import bs4
import datetime

address = "172.31.1.4"
port = "8080"
user = "HITN051"
password = "666729757"

http_proxy  = "http://" + user + ":" + password + "@" + address + ":" + port
https_proxy = "http://" + user + ":" + password + "@" + address + ":" + port
ftp_proxy   = "http://" + user + ":" + password + "@" + address + ":" + port   
proxyDict = { 
              "http"  : http_proxy, 
              "https" : https_proxy, 
              "ftp"   : ftp_proxy
            }

months = {
              1  :  "JANUARY",
              2  :  "FEBRUARY",
              3  :  "MARCH",
              4  :  "APRIL",
              5  :  "MAY",
              6  :  "JUNE", 
              7  :  "JULY",
              8  :  "AUGUST",
              9  :  "SEPTEMBER",
              10 :  "OCTOBER",
              11 :  "NOVEMBER",
              12 :  "DECEMBER"
}



class barclay_news:
    
    def __init__(self):
        self.url = "http://www.premierleague.com/en-gb.html"
        
        self.res = requests.get(self.url,stream=True,proxies=proxyDict)
        self.soup = bs4.BeautifulSoup(self.res.text,'lxml')
        
        self.all_updated = False

    def get_news_headlines(self):
            news_headline = []
            news_list = self.soup.select('.newsfeaturetitle')
            for i in range(len(news_list)):
                    news_headline.append(str(news_list[i].text))
            return news_headline
    
    def get_news_headlines_url(self):
            news_url = []
            urls = self.soup.select('.newsfeature a')
            for i in urls:
                    news_url.append("http://www.premierleague.com/"+i.get('href'))
            return news_url
            
    def get_club_news(self):
            news_headline = []
            news_list = self.soup.select('.feed li a')
            for i in range(len(news_list)):
                    news_headline.append(str(news_list[i].text))
            return news_headline
    
    def get_club_news_url(self):
            news_url = []
            urls = self.soup.select('.feed li a')
            for i in urls:
                    news_url.append(i.get('href'))
            return news_url
            
    def update_all(self):
        self.news_headlines = self.get_news_headlines()
        self.news_headlines_url = self.get_news_headlines_url()
        self.club_news = self.get_club_news()
        self.club_news_url = self.get_club_news_url()
        
        self.all_updated = True
            
    def news(self):
        if not self.all_updated:
            self.update_all()
            
        return [self.news_headlines, self.news_headlines_url]

#test = barclay_news()
#print (test.news())

class barclay_next3Fixtures:

    def __init__(self):
        now = datetime.datetime.now()
        self.url = "http://www.premierleague.com/en-gb/matchday/league-table.html?season=2015-2016&month=" + months[now.month] + "&timelineView=date&toDate=1451433599999&tableView=NEXT_3_FIXTURES"
        
        self.res = requests.get(self.url, stream=True, proxies=proxyDict)
        self.soup = bs4.BeautifulSoup(self.res.text,'lxml')

        self.all_updated = False

    def get_team_names(self):
        team_names = self.soup(template = '.next3FixturesTable')

        for i in range(len(team_names)):
            team_names[i] = str(team_names[i].text)

        return team_names

    def get_next_3_fixtures(self):
        self.next_3_fixtures = self.soup.select('.club-row .col-fixture')

        for i in range(len(self.next_3_fixtures)):
            self.next_3_fixtures[i] = str(self.next_3_fixtures[i].text)

        return self.next_3_fixtures
        
    def update_all(self):
        self.team_names = self.get_team_names()
        self.next_3_fixtures = self.get_next_3_fixtures()
        
        self.update_all = True

    def fixtures(self):
        if not self.all_updated:
            self.update_all()
            
        fixtures = []
        for i in range(20):
            j = i*3
            fixtures.append([self.next_3_fixtures[j], self.next_3_fixtures[j+1], self.next_3_fixtures[j+2]])
            
        return fixtures
        
    def fixtures_of(self, team):
        if not self.all_updated:
            self.update_all()
            
        position = self.team_names.index(team)
        fixtures = [self.next_3_fixtures[3*position], self.next_3_fixtures[3*position+1], self.next_3_fixtures[3*position+2]]
        
        return fixtures

#test = barclay_next3Fixtures()
#print (test.fixtures_of('Arsenal'))

class barclay_pointsTable:
    
    def __init__(self):
        self.url = 'http://www.premierleague.com/en-gb/matchday/league-table.html'
        #res = requests.get(url)
        self.res = requests.get(self.url, stream=True, proxies=proxyDict)
        self.soup = bs4.BeautifulSoup(self.res.text,'lxml')
        
        self.all_updated = False

    def get_team_names(self):
        team_name = self.soup(template = '.leagueTable-Club')
    
        for i in range(len(team_name)):
            team_name[i] = str(team_name[i].text)
    
        return team_name
    
    def get_matches_played(self):
        matches_played = self.soup(template = '.leagueTable-P')
    
        for i in range(len(matches_played)):
            matches_played[i] = str(matches_played[i].text)
    
        return matches_played
    
    def get_matches_won(self):
        matches_won = self.soup(template = '.leagueTable-W')
    
        for i in range(len(matches_won)):
            matches_won[i] = str(matches_won[i].text)
    
        return matches_won
    
    def get_matches_drew(self):
        matches_drew = self.soup(template = '.leagueTable-D')
    
        for i in range(len(matches_drew)):
            matches_drew[i] = str(matches_drew[i].text)
    
        return matches_drew
    
    def get_matches_lost(self):
        matches_lost = self.soup(template = '.leagueTable-L')
    
        for i in range(len(matches_lost)):
            matches_lost[i] = str(matches_lost[i].text)
    
        return matches_lost
    
    def get_goals_for(self):
        goals_for = self.soup(template = '.leagueTable-GF')
    
        for i in range(len(goals_for)):
            goals_for[i] = str(goals_for[i].text)
    
        return goals_for
    
    def get_goals_against(self):
        goals_against = self.soup(template = '.leagueTable-GA')
    
        for i in range(len(goals_against)):
            goals_against[i] = str(goals_against[i].text)
    
        return goals_against
    
    def get_goals_difference(self):
        goals_difference = self.soup(template = '.leagueTable-GD')
    
        for i in range(len(goals_difference)):
            goals_difference[i] = str(goals_difference[i].text)
    
        return goals_difference
    
    def get_points(self):
        points = self.soup(template = '.leagueTable-Pts')
    
        for i in range(len(points)):
            points[i] = str(points[i].text)
    
        return points
        
    def update_all(self):
        self.team_names = self.get_team_names()
        self.points = self.get_points()
        self.matches_played = self.get_matches_played()
        self.matches_won = self.get_matches_won()
        self.matches_drew = self.get_matches_drew()
        self.matches_lost = self.get_matches_lost()
        self.goals_for = self.get_goals_for()
        self.goals_against = self.get_goals_against()
        self.goal_difference = self.get_goals_difference()
        
    def table(self):
        if not self.all_updated:
            self.update_all()
            
        all_data = [self.team_names, self.points, self.matches_played, self.matches_won, self.matches_drew, self.matches_lost, self.goals_for, self.goals_against, self.goal_difference]
        
        return all_data

#test = barclay_pointsTable()
#print (test.table())

class barclay_topScorers:
    
    def __init__(self):
        self.url = "http://www.premierleague.com/en-gb.html"
       
        self.res = requests.get(self.url, stream=True, proxies=proxyDict)
        self.soup = bs4.BeautifulSoup(self.res.text,'lxml')
        
        self.all_updated = False

    def get_top_scorers(self):
        top_scorers = self.soup.select('.statsranking-topscorers .statsranking-table .statsranking-name a')
    
        for i in range(len(top_scorers)):
            top_scorers[i] = str(top_scorers[i].text)
    
        return top_scorers
    
    def get_top_goals(self):
        top_scorers = []
        top_scorers_temp = self.soup.select('.statsranking-topscorers .statsranking-table tbody tr td')
    
        for i in range(2, len(top_scorers_temp), 3):
            top_scorers.append(str(top_scorers_temp[i].text))
    
        return top_scorers
    
    def update_all(self):
        self.scorers = self.get_top_scorers()
        self.goals = self.get_top_goals()
        self.all_updated = True  
        
    def top_scorers_goals(self,num=10):
        if not self.all_updated:
            self.update_all()
        
        if num > 10:
            num = 10

        return [self.scorers, self.goals]
           

#print (barclay_topScorers().top_scorers_goals())

class barclay_Fixtures:
    
    def __init__(self):
        self.url = "http://www.premierleague.com/en-gb/matchday/matches.html?paramClubId=ALL&paramComp_8=true&view=.dateSeason"
        
        self.res = requests.get(self.url, stream=True, proxies=proxyDict)
        self.soup = bs4.BeautifulSoup(self.res.text,'lxml')
        
        self.all_updated = False
        
    def get_fixtures_time(self):
        fixtures_time = self.soup.select('.time')
    
        for i in range(len(fixtures_time)):
            fixtures_time[i] = str(fixtures_time[i].text)
    
        return fixtures_time
    
    def get_fixtures_clubs(self):
        fixtures_clubs = self.soup.select('.clubs a')
    
        for i in range(len(fixtures_clubs)):
            fixtures_clubs[i] = str(fixtures_clubs[i].text)
    
        return fixtures_clubs
    
    def get_fixtures_location(self):
        fixtures_location = self.soup.select('.location a')
    
        for i in range(len(fixtures_location)):
            fixtures_location[i] = str(fixtures_location[i].text)
    
        return fixtures_location

    def update_all(self):
        self.fixtures_time = self.get_fixtures_time()
        self.fixtures_clubs = self.get_fixtures_clubs()
        self.fixtures_location = self.get_fixtures_location()
        
        self.all_updated = True
        
    def fixtures(self):
        if not self.all_updated:
            self.update_all()

        return [self.fixtures_time, self.fixtures_clubs, self.fixtures_location]

#print (barclay_Fixtures().fixtures())

class barclay_Results:
    
    def __init__(self):
        self.url = "http://www.premierleague.com/en-gb.html"
        
        self.res = requests.get(self.url, stream=True, proxies=proxyDict)
        self.soup = bs4.BeautifulSoup(self.res.text,'lxml')
        
        self.all_updated = False
        
    def get_results_time(self):
        results_time = self.soup.select('.megamenu-date span')
    
        for i in range(len(results_time)):
            results_time[i] = str(results_time[i].text)
            
        results_time = results_time[0:20]
        results_time.reverse()
    
        return results_time
    
    def get_results_clubs(self):
        results_clubs = self.soup.select('.megamenu-matchName span')
    
        for i in range(len(results_clubs)):
            results_clubs[i] = str(results_clubs[i].text)
            
        results_clubs = results_clubs[0:60]
        
        results_clubs_temp = []
        for i in range(20):
            j = i*3
            results_clubs_temp.append([results_clubs[j], results_clubs[j+1], results_clubs[j+2]])
        
        results_clubs = results_clubs_temp
        results_clubs.reverse()
    
        return results_clubs
    
    def get_results_location(self):
        results_location = self.soup.select('.megamenu-venue')
    
        for i in range(len(results_location)):
            results_location[i] = str(results_location[i].text)
            
        results_location = results_location[0:20]
        results_location.reverse()
    
        return results_location

    def update_all(self):
        self.results_time = self.get_results_time()
        self.results_clubs = self.get_results_clubs()
        self.results_location = self.get_results_location()
        
        self.all_updated = True
        
    def results(self):
        if not self.all_updated:
            self.update_all()

        return [self.results_time, self.results_clubs, self.results_location]

test = barclay_Results()
print (test.results())
