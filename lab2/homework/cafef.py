from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
data = urlopen(url).read()
html_content = data.decode("utf-8")

soup = BeautifulSoup(html_content, "html.parser")
div = soup.find("div", style="overflow:hidden;width:100%;border-bottom:solid 1px #cecece;")
table = div.find("table")
tr_list = table.find_all("tr", {"class": ["r_item", "r_item_a"]})

from collections import OrderedDict

bctc_list = []
for tr in tr_list:
    td_list = tr.find_all("td")
    chi_tieu = td_list[0].string
    quy_4_16 = td_list[1].string
    quy_1_17 = td_list[2].string
    quy_2_17 = td_list[3].string
    quy_3_17 = td_list[4].string
    bctc = {
        "Chỉ tiêu": chi_tieu,
        "Quý 4-2016": quy_4_16,
        "Quý 1-2017": quy_1_17,
        "Quý 2-2017": quy_2_17,
        "Quý 3-2017": quy_3_17
    }
    bctc1 = OrderedDict(bctc.items())
    bctc_list.append(bctc1)

pyexcel.save_as(records=bctc_list, dest_file_name="cafef.xlsx")
