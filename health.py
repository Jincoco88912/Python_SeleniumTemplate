# %%
from datetime import datetime
import requests
from bs4 import BeautifulSoup

url = "https://1966.gov.tw/LTC/lp-6440-207-1-60.html"

# %%
resp = requests.get(url)
# print(resp.text)
soup = BeautifulSoup(resp.text, 'html.parser')
soup  =soup.find_all(class_="num")
# print(soup)
rows = [s.find_parent("li") for s in soup]
print(rows)
results=[]

# %%
for i in rows:
    title = i.find("a").get("title")
    link = i.find("a").get("href")
    time = i.find("time").text
    print(f"{title=} {link=} {time=}")
    results.append({"title":title,"link":link,"time":time})

# %%
print(results)
#連接資料庫
from sqlalchemy import create_engine,text
engine = create_engine("mssql+pyodbc://sa:project%40111@140.137.61.139:1433/healthcare?driver=SQL+Server+Native+Client+11.0")

#放資料進資料庫
with engine.connect() as conn:
    for i in results:
       result = conn.execute(text("INSERT INTO news (title, www, newsupdate) VALUES (:title, :www , :newsupdate)"),
        {"title": i['title'], "www": i['link'],"newsupdate":i['time']})
print('success to db')