from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_page = response.text

soup = BeautifulSoup(web_page,'html.parser')
article_tag = soup.find_all(name='h3',class_="title")
title_names = []
for item in article_tag :
    title = item.getText()
    title_names.append(title)
title_names = list(reversed(title_names))
print(title_names)
with open('movies.txt','a',encoding='utf8') as file :
    for movie in title_names :
        file.write(movie+"\n")
