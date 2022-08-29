from sre_constants import INFO
from bs4 import BeautifulSoup
from csv import writer
import requests

#webpage used to scrape data from
url="https://www.pararius.com/apartments/amsterdam"
page=requests.get(url)
soup =BeautifulSoup(page.content,"html.parser")
#retrieve all sections with class listing-item-search
lists=soup.find_all("section",class_="listing-search-item")
#create file and loop through sections to populate rows
with open('housing.csv','w',encoding='utf8',newline='') as f:
    thewriter=writer(f)
    header=['Title','Location','Price','Area']
    thewriter.writerow(header)
    for list in lists:
        title=list.find('a',class_='listing-search-item__link--title').text.replace('\n','').strip()
        location=list.find('div',class_='listing-search-item__sub-title').text.replace('\n','').strip()
        price=list.find('div',class_='listing-search-item__price').text.replace('\n','').strip()
        area=list.find('li',class_='illustrated-features__item--surface-area').text.replace('\n','').strip()
        info=[title,location,price,area]
        thewriter.writerow(info)