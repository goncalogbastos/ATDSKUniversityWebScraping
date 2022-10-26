import requests as r
from bs4 import BeautifulSoup


URL = "https://www.autodesk.com/autodesk-university/au-online?facet_product%5B0%5D=urn%3Aadsk.content%3Acontent%3A3324e2e0-c5c3-461d-b91a-f31517c7cb19&page=1"
headers = {'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 10066.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
page = r.get(URL, headers=headers)


soup = BeautifulSoup(page.content, "html.parser")
classTitles = soup.find_all("div", class_="medium--down--hide")

print(classTitles)