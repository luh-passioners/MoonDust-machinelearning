import ssl
from urllib.request import Request, urlopen
from SentimentAnalyze import analyze 
from bs4 import BeautifulSoup


class NewsScraper:
    """Scrapes news data from finviz.com"""

    def __init__(self, tickers):
        self.tickers = tickers
        self.news_data = {}
        self.context = ssl._create_unverified_context()
        self.user_agent = {'user-agent': 'my-app'}

    def scrape_news(self):
        """Scrapes news data for each ticker"""
        finviz_url = 'https://finviz.com/quote.ashx?t='
        for ticker in self.tickers:
            url = finviz_url + ticker
            req = Request(url=url, headers=self.user_agent)
            try:
                response = urlopen(req, context=self.context)
                content = response.read()
                html = BeautifulSoup(content, 'html.parser')
                individual_news_data = html.find(id='news-table')
                self.news_data[ticker] = individual_news_data
            except Exception as e:
                print("Error fetching data for ticker", ticker)
                print(e)


class NewsParser:
    """Parses scraped news data"""

    def __init__(self, news_data):
        self.news_data = news_data

    def parse_news_links(self):
        """Parses news links and headlines for each ticker"""
        sorted_news_data = []
        ticker_links = {}
        for ticker, news_data in self.news_data.items():
            news_links = []
            for row in news_data.findAll('tr'):
                if len(news_links) > 5:
                    break
                if row.a:
                    title = row.a.text.strip()
                    link = row.a["href"]
                else:
                    title = "No headline found"
                sorted_news_data.append([ticker, title, link])
                news_links.append(link)
            ticker_links[ticker] = news_links
        return sorted_news_data, ticker_links


def tag_visible(element):
    """Filters out unwanted elements from text extraction"""
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    return True


def text_from_html(body):
    """Extracts visible text from HTML content"""
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(string=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.strip() for t in visible_texts)


def analyze_news(ticker_links):
    """Fetches news content and performs sentiment analysis"""
    text = []
    for ticker in ticker_links:
        for link in ticker_links[ticker]:
            ticker_link = link
            html = Request(url=ticker_link, headers={'user-agent': 'my-app'})
            try:
                response = urlopen(html, context=ssl._create_unverified_context())
                content = response.read()
                content = text_from_html(content)
                text.append(content)
            except Exception as e:
                print("Error fetching data for ticker", ticker)
                print(e)
    for val in text:
        print(analyze(val))


# Usage
tickers = ['AMZN', 'AMD']
scraper = NewsScraper(tickers)
scraper.scrape_news()

parser = NewsParser(scraper.news_data)
sorted_news_data, ticker_links = parser.parse_news_links()

analyze_news(ticker_links)  