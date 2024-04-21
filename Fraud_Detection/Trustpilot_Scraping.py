import requests
from bs4 import BeautifulSoup
import json
import re


def Scrape_Score(company):
    url_Start = "https://www.trustpilot.com/search?query="
    url = url_Start + company
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers = headers)

    if response.status_code == 200:
        # Parse the HTML with Beautiful Soup
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find all comments with the specified tag
        trustscore_element = soup.find('span', class_='styles_desktop__U5iWw')

        if trustscore_element:
            # Access the content or attributes of the element
            
            parent_text = trustscore_element.parent.text.strip()


            pattern = r"\d+\.\d+"

            match = re.search(pattern, parent_text)
            trustscore = match.group()
            print(trustscore)
        else:
            print("TrustScore element not found")


