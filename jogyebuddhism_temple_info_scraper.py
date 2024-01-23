import requests
from bs4 import BeautifulSoup
import csv

def scrape_temple_info(base_url, total_pages):
    temple_info = []

    for page in range(1, total_pages + 1):
        url = f"{base_url}&page={page}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        for td in soup.find_all('td', style=lambda value: value and 'word-break:break-all;' in value):
            name_tag = td.find('span')
            name = name_tag.get_text(strip=True) if name_tag else 'No Name'
            
            location_parts = td.find_all('td', align='left')
            location = ''
            if location_parts:
                for part in location_parts:
                    if '소재지 :' in part.get_text():
                        location = part.get_text(strip=True).replace('소재지 :', '').replace('<br>', '').strip()

            temple_info.append({'Name': name, 'Location': location})

    return temple_info

def write_to_csv(data, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Name', 'Location'])
        writer.writeheader()
        for temple in data:
            writer.writerow(temple)

def main():
    BASE_URL = 'http://jogyebuddhism.or.kr/bbs/board.php?bo_table=yuljong_sachal'
    TOTAL_PAGES = 52

    temples = scrape_temple_info(BASE_URL, TOTAL_PAGES)
    csv_filename = 'temples.csv'
    write_to_csv(temples, csv_filename)
    print(f"Data successfully saved to {csv_filename}")

if __name__ == "__main__":
    main()
