import requests
from bs4 import BeautifulSoup

Headers = {'User-Agent' : 'Mozilla/5.0 (Window NT 10.0 : Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) chrome / 128.0.0.0 Sarari/537.36'}
Url = "https://www.melon.com/new/index.htm"
Req = requests.get(Url,headers = Headers)
Html = Req.text
Soup = BeautifulSoup(Html,'html.parser')
NewList50 = Soup.select('td > div')

for Memo in NewList50:
    Rank = Memo.select_one('span.rank')

    if Rank is not None:
        print(Rank.text, end = '. ')

    Title = Memo.select_one('div > div.ellipsis.rank01 > span > a')
    Album = Memo.select_one('div > div.ellipsis.rank03 > a')
    if Title is not None:
        artist = Memo.select_one('div.ellipsis.rank02 > a').text

        print(artist, ',', Title.text, ',', Album)