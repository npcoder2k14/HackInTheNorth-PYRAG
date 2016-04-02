import requests
import bs4
import datetime
import json

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

class Barclay(object):

    def get_news_headlines(self, get_club_news=False, type_return='string'):
        """
        Parameters
        ----------
        get_club_news : Bool, default to False
                        If true , returns news about clubs too.

        type_return : String, to specify the return type
                      Defaults to `string`
        Returns
        -------
        String : A collection of news headlines and links
        """
        url = "http://www.premierleague.com/en-gb.html"
        res = requests.get(url,stream=True,proxies=proxyDict)
        soup = bs4.BeautifulSoup(res.text,'lxml')
        all_updated = False
        news_headline = []
        news_list = soup.select('.newsfeaturetitle')
        for i in range(len(news_list)):
            news_headline.append(str(news_list[i].text))
        news_url = []
        urls = soup.select('.newsfeature a')
        for i in urls:
            news_url.append("http://www.premierleague.com/"+i.get('href'))
        if get_club_news is True:
            news_list = soup.select('.feed li a')
            for i in range(len(news_list)):
                    news_headline.append(str(news_list[i].text))
            urls = soup.select('.feed li a')
            for i in urls:
                    news_url.append(i.get('href'))
        return_dict = {}
        for i, name in enumerate(news_headline):
            return_dict[name] = news_url[i]

        if type_return == 'dict':
            return return_dict

    def next3Fixtures(self, type_return='string'):
        now = datetime.datetime.now()
        url = "http://www.premierleague.com/en-gb/matchday/league-table.html?season=2015-2016&month=" +\
                months[now.month] + "&timelineView=date&toDate=1451433599999&tableView=NEXT_3_FIXTURES"
        team_names = soup(template = '.next3FixturesTable')
        for i in range(len(team_names)):
            team_names[i] = str(team_names[i].text)

        next_3_fixtures = soup.select('.club-row .col-fixture')
        for i in range(len(next_3_fixtures)):
            next_3_fixtures[i] = str(next_3_fixtures[i].text)

        return_dict = {}
        for i in range(len(team_names)):
            return_dict[team_names[i]] = next_3_fixtures[i]

        if type_return == 'dict':
            return return_dict

    def pointsTable(self, type_return='string'):
        url = 'http://www.premierleague.com/en-gb/matchday/league-table.html'

        res = requests.get(url, stream=True, proxies=proxyDict)
        soup = bs4.BeautifulSoup(res.text,'lxml')

        team_name = soup(template = '.leagueTable-Club')
        for i in range(len(team_name)):
            team_name[i] = str(team_name[i].text)

        matches_played = soup(template = '.leagueTable-P')
        for i in range(len(matches_played)):
            matches_played[i] = str(matches_played[i].text)

        matches_won = soup(template = '.leagueTable-W')
        for i in range(len(matches_won)):
            matches_won[i] = str(matches_won[i].text)

        matches_drew = soup(template = '.leagueTable-D')
        for i in range(len(matches_drew)):
            matches_drew[i] = str(matches_drew[i].text)

        matches_lost = soup(template = '.leagueTable-L')
        for i in range(len(matches_lost)):
            matches_lost[i] = str(matches_lost[i].text)

        goals_difference = soup(template = '.leagueTable-GD')
        for i in range(len(goals_difference)):
            goals_difference[i] = str(goals_difference[i].text)

        points = soup(template = '.leagueTable-Pts')
        for i in range(len(points)):
            points[i] = str(points[i].text)

        return_dict = {}
        for i in range (len(team_name)):
            return_dict[team_name[i]] = [matches_played[i], matches_won[i], matches_drew[i], matches_lost[i], goals_difference[i], points[i]]

        if type_return == 'dict':
            return return_dict

    def topScorers(self, type_return='string'):
        url = "http://www.premierleague.com/en-gb.html"

        res = requests.get(url, stream=True, proxies=proxyDict)
        soup = bs4.BeautifulSoup(res.text,'lxml')

        top_scorers = soup.select('.statsranking-topscorers .statsranking-table .statsranking-name a')
        for i in range(len(top_scorers)):
            top_scorers[i] = str(top_scorers[i].text)

        top_scorers_goals = []
        top_scorers_temp = soup.select('.statsranking-topscorers .statsranking-table tbody tr td')

        for i in range(2, len(top_scorers_temp), 3):
            top_scorers_goals.append(str(top_scorers_temp[i].text))

        return_dict = {}
        for i in range(len(top_scorers)):
            return_dict[top_scorers[i]] = top_scorers_goals[i]

        if type_return == 'dict':
            return return_dict

    def Fixtures(self, return_type='string'):
        url = "http://www.premierleague.com/en-gb/matchday/matches.html?paramClubId=ALL&paramComp_8=true&view=.dateSeason"

        res = requests.get(url, stream=True, proxies=proxyDict)
        soup = bs4.BeautifulSoup(res.text,'lxml')

        fixtures_time = soup.select('.time')
        for i in range(len(fixtures_time)):
            fixtures_time[i] = str(fixtures_time[i].text)

        fixtures_clubs = soup.select('.clubs a')
        for i in range(len(fixtures_clubs)):
            fixtures_clubs[i] = str(fixtures_clubs[i].text)

        fixtures_location = soup.select('.location a')
        for i in range(len(fixtures_location)):
            fixtures_location[i] = str(fixtures_location[i].text)

        return [fixtures_clubs, fixtures_time, fixtures_location]

    def Results(self, type_return='string'):
        url = "http://www.premierleague.com/en-gb.html"

        res = requests.get(url, stream=True, proxies=proxyDict)
        soup = bs4.BeautifulSoup(res.text,'lxml')

        results_time = soup.select('.megamenu-date span')
        for i in range(len(results_time)):
            results_time[i] = str(results_time[i].text)

        results_time = results_time[0:20]
        results_time.reverse()

        results_clubs = soup.select('.megamenu-matchName span')
        for i in range(len(results_clubs)):
            results_clubs[i] = str(results_clubs[i].text)
        results_clubs = results_clubs[0:60]

        results_clubs_temp = []
        for i in range(20):
            j = i*3
            results_clubs_temp.append([results_clubs[j], results_clubs[j+1], results_clubs[j+2]])
        results_clubs = results_clubs_temp
        results_clubs.reverse()

        results_location = soup.select('.megamenu-venue')
        for i in range(len(results_location)):
            results_location[i] = str(results_location[i].text)
        results_location = results_location[0:20]
        results_location.reverse()

        return [results_time, results_clubs, results_location]

if __name__ == '__main__':
    obj = Barclay()
    print(obj.get_news_headlines(type_return='dict'))
    print(obj.pointsTable('dict'))
    print(obj.topScorers('dict'))
    print(obj.Fixtures())
    print(obj.Results())
