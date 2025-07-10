import requests
from bs4 import BeautifulSoup

def Analyzer(url):
    reponse = requests.get(url)
    soup = BeautifulSoup(reponse.text,"html.parser")

    title = soup.title.string if soup.title else "No title"
    meta_desc = soup.find('meta', attrs={'name':'description'})
    meta_desc = meta_desc["content"] if meta_desc else "No Meta_desc"

    h1_tags = [h.get_text(strip=True) for h in soup.find_all('h1')]
    images = soup.find_all('img')
    missing_alt = sum(1 for img in images if not img.find('alt'))

    return title, h1_tags,images, missing_alt
    # print(f"Title: {title}")
    # print(f"Meta Description: {meta_desc}")
    # print(f"H1 Tags: {h1_tags}")
    # print(f"images:{images}")
    # print(f"Images without alt: {missing_alt}/{len(images)}")

# Url = input("Enter URL:  ")
# Analyzer(Url)