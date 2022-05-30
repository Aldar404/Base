import requests
from bs4 import BeautifulSoup


r = requests.get("https://randstuff.ru/saying/")
soup = BeautifulSoup(r.text, 'html.parser')
wisdom = soup.find('div', id="saying")
result = wisdom.get_text(strip=True)


