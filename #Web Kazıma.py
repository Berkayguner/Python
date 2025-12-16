#Web Kazıma.py 
import requests 
from bs4 import BeautifulSoup 

url= "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
    "Accept-Language":"tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
    "Referer":"https://www.google.com/",
    "Connection":"keep-alive"

}   

response=requests.get(url,headers=headers)
soup=BeautifulSoup(response.text,"html.parser")

table=soup.find_all("table")[0]
titles=table.find_all("th")
table_titles=[item.text.strip() for item in titles]

for item in table_titles:
    print(item, end=" ")
print("\n----------------------------------------------") 

rows=table.find_all("tr")
for row in rows[1:]:
    my_row =row.find_all("td")
    table_rows=[item.text.strip() for item in my_row] 
    for item in table_rows:
        print(item,end="  ")
    print("\n")