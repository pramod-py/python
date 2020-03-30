#Code by @pyadda
import requests
from bs4 import BeautifulSoup
res=requests.get("https://www.worldometers.info/coronavirus/")
soup=BeautifulSoup(res.content,"html.parser")
all_div=soup.find_all('div',{'class':'maincounter-number'})
update= soup.find_all('div', {'style':'font-size:13px; color:#999; text-align:center'})[0].get_text()
print(update)
total_Cases=soup.find_all('div',{'class':'maincounter-number'})[0].get_text()
print("Total Corona Virus Cases",total_Cases)
total_death=soup.find_all('div',{'class':'maincounter-number'})[1].get_text()
print("Total Death Cases",total_death)
recovered=soup.find_all('div',{'class':'maincounter-number'})[2].get_text()
print("Total recoverd Cases",recovered)
