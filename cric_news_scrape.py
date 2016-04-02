import requests,os,bs4

address = "172.31.1.6"
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

class cric_news:
 def news(self):
    base_url='http://www.cricbuzz.com/cricket-news/latest-news'
    res=requests.get(base_url,stream=True,proxies=proxyDict)

    soup = bs4.BeautifulSoup(res.text,"lxml")
    news = soup.select(".cb-col-33 a")
    news_dict={}
    for all_news in news:
        if str(all_news.get("title"))!="More Photos" and str(all_news.get("title"))!="None":
            news_dict[all_news.get("title")]=base_url+all_news.get("href")
    return news_dict
tt=cric_news()
tt.news()
