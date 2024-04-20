from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import ssl


def get_tickers():
    context = ssl._create_unverified_context()
    swing_trade_bot_url = 'https://swingtradebot.com/stocks-tagged-as/41811/as_charts?page='

    tickers = []

    for index in range(1, 4):
        url = swing_trade_bot_url + str(index)

        req = Request(url=url, headers={'user-agent': 'my-app'})

        response = urlopen(req, context=context)
        content = response.read()

        # Check status code
        status_code = response.getcode()

        if status_code == 200:  # Success
            html = BeautifulSoup(content, 'html.parser')
            for anchor in html.find_all('a', class_='text-decoration-underline', target='_blank', href=True):
                text = anchor.text.strip()
                if text:
                    ticker = text.split(" - ")[0].strip()
                    tickers.append(ticker)
        else:
            print(f"Error: Website returned status code {status_code}")


    return tickers

# Test usage
#extracted_tickers = get_tickers()

#if extracted_tickers:
#  print("Extracted tickers:")
#  for ticker in extracted_tickers:
#    print(ticker)
#else:
#  print("No tickers found.")