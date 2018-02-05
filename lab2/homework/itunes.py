from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.apple.com/itunes/charts/songs/"
data = urlopen(url).read()
html_content = data.decode("utf-8")

soup = BeautifulSoup(html_content, "html.parser")
div_list = soup.find_all("div", "section-content")
ul = div_list[1].find("ul")
li_list = ul.find_all("li")

song_list = []
for li in li_list:
    a3 = li.h3.a
    a4 = li.h4.a
    song_name = a3.string
    artist = a4.string
    songs ={
        "Song's name": song_name,
        "Artist": artist
    }
    song_list.append(songs)

import pyexcel
pyexcel.save_as(records=song_list, dest_file_name="itunes.xlsx")
