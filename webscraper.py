from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import urllib.error
import requests
import urllib


def bbc():
    url = 'https://www.bbc.com/news'
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    word = input('What are you looking for?')
    for tag in soup.find_all('a', attrs={'class': 'gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor'}):
        if word in tag.text:
            x = tag.get('href')
            if x.startswith('https'):
                print(tag.text, '->', tag['href'])
            else:
                print(tag.text, '->'+'https://www.bbc.com'+tag.get('href'))
# so far i have created a webcrawler that goes on the first page of the bbc.com


def wordSearch():
    topic = input('What are you looking for ?')
    url_list = []
    for i in range(1, 11):
        dynamic_url = f'https://www.bbc.co.uk/search?q={topic}&page={i}'
        url_list.append(dynamic_url)
    headers = {"User-Agent": ""}
    for url in url_list:
        html = requests.get(url, headers=headers)
        if html.status_code == 200:
            soup = BeautifulSoup(html.text, 'html.parser')
            print(F'--- PAGE {url_list.index(url)+1} ---')
            for tag in soup.find_all('a', attrs={'class': 'ssrcss-1ynlzyd-PromoLink e1f5wbog0'}):
                date = soup.find(
                    'span', {'class': 'ssrcss-1if1g9v-MetadataText ecn1o5v1'}).get_text(strip=True)
                print(tag.text, '->', tag['href'], '->', date)
        else:
            print(f'Failed connection on page{url_list.index(url)+1} ..')


print(bbc())
