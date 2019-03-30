import requests
from bs4 import BeautifulSoup

request = requests.get('https://taes-k.github.io')
html = request.text
newHtml = BeautifulSoup(html, 'html.parser')

subject = newHtml.select(
    'body > div > div.side-bar > div > nav > ul > li > a'
)

for title in subject :
    print(title.text)