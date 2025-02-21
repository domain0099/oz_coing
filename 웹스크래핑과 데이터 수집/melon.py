
import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"}

url = "https://www.melon.com/chart/index.htm"
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

lst50 = soup.select(".lst50") # list형태
lst100 = soup.select(".lst100") # list형태
#soup.select(".lst50, .lst100")

lst_all = lst50 + lst100

for rank, i in enumerate(lst_all, 1):
    title = i.select_one(".ellipsis.rank01 a").text
    singer = i.select_one(".checkEllipsis").text
    album = i.select_one(".ellipsis.rank03 a").text

    print(f"[순위] : {rank}")
    print(f"[제목] : {title}")
    print(f"[가수] : {singer}")
    print(f"[앨범] : {album}")
    print()

