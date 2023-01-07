import requests
from bs4 import BeautifulSoup

def livros_monitorados(lista_livros:list):
    for livro in lista_livros:
        titulo, preco = consulta(livro)
        print(titulo, preco)

def consulta(title:str):
    site_amazon = 'https://www.amazon.com.br/s?k='
    new_title = title.replace(" ", "+")
    url = site_amazon+new_title+"&i=stripbooks"
    # print(url)
    header = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Referer':'https://www.amazon.com/stores/page/0B6B05F4-EE4D-4696-A789-BB7152AB8DCE?ingress=0&visitId=9365015c-39f1-4f05-8ec9-61dfafb3a84a&channel=SB-gway&liveVideoDataUrl=https%3A%2F%2Famazonlive-portal.amazon.com%2Fv2&ref_=sb_w_i_ctcd_snkrs&productGridPageIndex=4'
    }

    r = requests.get(url, headers=header)
    soup = BeautifulSoup(r.content, 'html.parser')

    first = soup.find(
        'div',
        class_='s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16'
    )

    title = first.find('span', class_='a-size-medium a-color-base a-text-normal').text
    price = first.find('span', class_='a-offscreen').text

    return (title, price)

livros_monitorados([
    'princesa das cinzas'
    , 'pequeno príncipe'
    , 'divergente'
    , 'a arte da guerra'
    , 'a biblioteca da meia noite'
])
