import requests as r
import pandas as pd
from bs4 import BeautifulSoup



baseURL = "https://www.autodesk.com/autodesk-university/au-online?facet_product%5B0%5D=urn%3Aadsk.content%3Acontent%3A3324e2e0-c5c3-461d-b91a-f31517c7cb19&"
headers = {'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 10066.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
page = r.get(baseURL, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")

# Get last page index
lastPageTag = soup.find('li', class_="pager__item pager__item--last")
lastPageLink = lastPageTag.find('a', href=True).attrs['href']
lastPage = lastPageLink.split("page=",1)[1]

# Iterate over pages
pages = list(range(0,int(lastPage)+1))

class_titles = []
class_links = []

for page in pages:
    print("#####################################################")
    print("Page " + str(page))
    
    url = baseURL + "page=" + str(page)
    page_ = r.get(url, headers=headers)
    soup_ = BeautifulSoup(page_.content, "html.parser")
    
    classLinks = soup_.find_all('div', class_="result grid")

    for i,classLink in enumerate(classLinks):       
        link = classLink.find('a', href=True).attrs['href']
        link_ = "www.autodesk.com" + link

        classTitle = link.split("/autodesk-university/class/",1)[1].replace("-"," ")
        print("Class " + str(i) + ": " + classTitle)

        class_titles.append(classTitle)
        class_links.append(link_)
    

# Export to excel
df = pd.DataFrame({"Class Title": class_titles, "Class Links": class_links})
df.to_excel('AUCivil3DClasses.xlsx', sheet_name="sheet1", index=False)  



