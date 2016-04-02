import requests,os,bs4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def get_player_stats(playerName):
    
    
    base_url="http://www.espncricinfo.com"
    url="http://www.espncricinfo.com/ci/content/player/search.html?search="
    
    names=[]    
    
    names=playerName.split()
    
    # for i in names:
    #    print i
        
    playerName="+".join(names)

    # print playerName
    url=url+playerName
    #print url

    res=requests.get(url)
    res.raise_for_status()
    
    soup=bs4.BeautifulSoup(res.text,"lxml")
    
    playerStatLink=soup.select(".ColumnistSmry") 
    playerStatLink=playerStatLink[1]
    temp_url=playerStatLink.get('href')

    url=base_url+temp_url

    res=requests.get(url)

    soup=bs4.BeautifulSoup(res.text,"lxml")

    player_info=soup.select(".ciPlayerinformationtxt")

    player_stats={}   

    for item in player_info[0:len(player_info)]:
        b=item.find('b')
     
        if b.string=="Major teams":
            span=item.findAll('span')
            temp=""
            for it in span:
                 temp+=it.string+" "
        else:
            temp=item.find('span')
            temp=temp.string

     
        player_stats[b.string]=temp

  """  if 'Current age' in player_stats.keys():
        player_age=player_stats['Current age']
        print player_age
    if 'Major teams' in player_stats.keys():
        player_teams=player_stats['Major teams']
        print player_teams

    if 'Playing role' in player_stats.keys():
        player_role=player_stats['Playing role']
        print player_role
    if 'Batting style' in player_stats.keys():
        player_bat_style=player_stats['Batting style']
        print player_bat_style)

    if 'Bowling style' in player_stats.keys():
        player_bowl_style=player_stats['Bowling style']
        print(player_bowl_style)
    """

    return player_stats  

def live_score():

    url = "http://www.cricbuzz.com/cricket-match/live-scores"
    response = requests.get('http://www.cricbuzz.com/live-cricket-full-commentary/15803/wi-vs-ind-2nd-semi-final-icc-world-t20-2016')
    soup = BeautifulSoup(response.text,"lxml")
    response = requests.get('http://www.cricbuzz.com/live-scores')
    soup = BeautifulSoup(response.text,"lxml")
    team_mate = soup.findAll("div", {"class" : "cb-lv-main"})
    for i in team_mate:
        print (i.text)
        print "\n\n"        
   
if __name__=='__main__':     
    player_stats=get_player_stats("Virender Sehwag")
    live_score()
    
    
