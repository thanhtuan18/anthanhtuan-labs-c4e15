url = "http://dantri.com.vn"
output_file_name = "new.xlsx"

# 1. Download trang Web
from urllib.request import urlopen
from bs4 import BeautifulSoup

# # 1.1 Mo ket noi voi website
# conn = urlopen(url)
# # 1.2 Read
# data = conn.read()
# # 1.3 Decode
# html_content = data.decode("utf-8")

data = urlopen(url).read()
html_content = data.decode("utf-8")

# html_file = open("dantri.html", "wb")
# html_file.write(data)
# html_file.close()
# 2. Tach ra vung quan tam

# Create a Soup
soup = BeautifulSoup(html_content, "html.parser") # xml
# print(soup.prettify())
ul = soup.find("ul", "ul1 ulnew") # class id="" 1 soup
# print(ul.prettify())
li_list = ul.find_all("li") # [soup, soup, soup]
# for li in li_list:
#     # print(li.prettify())
#     print(li["href"], li["link"])
#     print("***********************")

# 3. Tach thong tin can thiet

news_list = []
for li in li_list:
    h4 = li.h4 # hoac h4 = li.find("h4")
    a = h4.a # hoac a = li.a hoac a = li.h4.a
    href = url + a["href"]
    title = a.string #a["title"]
    news = {
        "title": title,
        "link": href
    }
    news_list.append(news)

import pyexcel
pyexcel.save_as(records=news_list, dest_file_name="dantri.xlsx")
