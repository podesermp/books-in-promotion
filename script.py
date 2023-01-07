from datetime import datetime
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Making a GET request
url = 'https://www.amazon.com.br/gp/bestsellers/books'
header = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'Referer':'https://www.amazon.com/stores/page/0B6B05F4-EE4D-4696-A789-BB7152AB8DCE?ingress=0&visitId=9365015c-39f1-4f05-8ec9-61dfafb3a84a&channel=SB-gway&liveVideoDataUrl=https%3A%2F%2Famazonlive-portal.amazon.com%2Fv2&ref_=sb_w_i_ctcd_snkrs&productGridPageIndex=4'
}

r = requests.get(url, headers=header)

soup = BeautifulSoup(r.content, 'html.parser')
trinta_mais = []
cards = soup.select('div[id=gridItemRoot]')

for card in cards:
    
    price = "_cDEzb_p13n-sc-price_3mJ9Z" # span
    title_author = "_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y" # div
    class_link = "a-link-normal a-text-normal" # a
    link = "https://www.amazon.com.br"


    price = card.find('span', class_=price)
    price = price.text
    title_author = card.select(f"div[class={title_author}]")
    link += card.find('a', class_=class_link).get('href')

    title = title_author[0].text
    author = title_author[1].text
    trinta_mais.append({
        "title": title
        ,"author": author
        ,"price": price
        ,"link": link
    })

df_trinta_mais = pd.DataFrame(trinta_mais, columns=trinta_mais[0].keys())
day= datetime.today().strftime('%Y-%m-%d %Hh%M')
 
with pd.ExcelWriter(f"./Trinta_mais_amazon.xlsx") as writer:
    df_trinta_mais.to_excel(writer, sheet_name=f"30 mais - {day}", index = False)