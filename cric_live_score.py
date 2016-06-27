import requests,os,bs4
from flask import Flask,jsonify

app=Flask(__name__) 
class Cricket:
 def live_scor(self):
  live_score=[]
  url="http://www.cricbuzz.com/live-scores"

  res=requests.get(url)
  soup=bs4.BeautifulSoup(res.text,"lxml")
 
  live = soup.findAll("div",{"class" : "cb-lv-main"})

  i=int()
  for i in range(len(live)):
    Headline=str()
    try:
      Headline=live[i].find('div',attrs={'class':'text-bold'}).text
    except:
      Headline=live_score[i-1]['Headline']  

    match_title=live[i].find('a',attrs={'class' : 'text-hvr-underline'}).text
 
    match_link="http://www.cricbuzz.com"+live[i].find('a').get('href')
    name_of_the_match_in_the_series=live[i].findAll('div',attrs={'class' : 'text-gray'})[0].text

    match_venue=live[i].findAll('div',attrs={'class' : 'text-gray'})[1].text

    match_timestamp=live[i].find('span',attrs={'class' : 'schedule-date'}).get('timestamp')

    tmp=live[i].findAll('div',attrs={'class' : 'cb-lv-scrs-col'})
    tmp2=tmp[:-1]
    tmp2=tmp2[0].findAll('span',attrs={'class' : 'text-bold'})
    #print(tmp[0].text)
    #string = string.replace(u'\xa0', u' ')
    match_score=tmp[0].text
    match_score = match_score.replace(u'\xa0',' ')
    #print(len(tmp2))
   
    #print(match_score)
    match_status=tmp[-1].text
    live_dict={}
    live_dict['Headline']=str(Headline)
    live_dict['match_title']=str(match_title)
    live_dict['match_link']=str(match_link)
    live_dict['name_of_the_match_in_the_series']=str(name_of_the_match_in_the_series)
    live_dict['match_venue']=str(match_venue)
    live_dict['match_timestamp']=str(match_timestamp)
    live_dict['match_score']=match_score
    live_dict['match_status']=str(match_status)
  # print(live_dict)
    live_score.append(live_dict)
    
  final_res=jsonify(result=live_score)
  return final_res    


if __name__=='__main__':
  cric=Cricket()
  app.add_url_rule('/',view_func=cric.live_scor)
  port = int(os.environ.get("PORT", 5001))
  app.run(host='0.0.0.0', port=port,debug=True)

