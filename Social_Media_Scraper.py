import requests
from bs4 import BeautifulSoup
import json
import re
from SentimentAnalyze import analyze

def scrape_for_board(ticker):
        url_Start = "https://investorshub.advfn.com/v2/boards?query="
        url = url_Start + ticker
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        response = requests.get(url, headers = headers)
        if response.status_code == 200:
            data = json.loads(response.text)
            # Extract and print the "boardurl" values as strings
            try:
                first_boardurl = data[0]["boardurl"]
                return str(first_boardurl)
            except Exception as e:
                print(e)

        else:
            print(response, 'Failed to retrieve data from the website.')
            print(response.reason)


def scrape_investorhub_board(ticker): 
    board = scrape_for_board(ticker)
    url_Start = "https://investorshub.advfn.com/"
    url = url_Start + board
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers = headers)


    if response.status_code == 200:
        # Parse the HTML with Beautiful Soup
        html_content = response.content
        soup = BeautifulSoup(html_content, 'lxml')

        # Find all comments with the specified tag
        comments = soup.find_all('p', class_='mb-0')
        count = 0  # Track the number of comments added

        # Extract the text content of the first 10 comments
        comment_texts = []
        for comment in comments:
            if not re.search(r"https?://\S+", comment.get_text(strip=True)) and count < 20:
                comment_texts.append(comment.get_text(strip=True))  # Remove leading/trailing whitespace
                count += 1

        return Text_Cleaner(comment_texts)
    else:
        print(response, 'Failed to retrieve data from the website.')
        print(response.reason)



def Text_Cleaner(comment_texts):
    cleaned_text_list = []
    for text in comment_texts:
        # Remove special characters and punctuation
        clean_text = re.sub(r"[^\w\s]", "", text)
        # Remove URLs and HTML tags (optional, adjust regex if needed)
        clean_text = re.sub(r"(http\S+|\<.*?\>)", "", clean_text)
        # Convert all letters to lowercase (optional)
        clean_text = clean_text.lower()  # Optional for sentiment analysis

        cleaned_text_list.append(clean_text.strip())  # Remove leading/trailing whitespace

    return cleaned_text_list

def Calculate_Score(comment_texts):
    score = 0
    for text in comment_texts:
        Str_Text = str(text)
        score += analyze(Str_Text)
    return score / len(comment_texts)

