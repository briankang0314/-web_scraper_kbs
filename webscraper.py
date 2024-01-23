# /path/to/your/scraping_script.py
import requests
from bs4 import BeautifulSoup

def scrape_temple_names(base_url, total_pages):
    temple_names = []

    for page in range(1, total_pages + 1):
        url = f"{base_url}&page={page}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Replace 'your_element_selector' with the actual selector needed to find temple names
        temples = soup.select('your_element_selector')
        for temple in temples:
            temple_names.append(temple.text.strip())

    return temple_names

def main():
    BASE_URL = 'http://jogyebuddhism.or.kr/bbs/board.php?bo_table=yuljong_sachal'
    TOTAL_PAGES = 52

    temples = scrape_temple_names(BASE_URL, TOTAL_PAGES)
    for name in temples:
        print(name)

if __name__ == "__main__":
    main()
