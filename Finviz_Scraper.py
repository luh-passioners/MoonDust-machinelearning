import ssl
from urllib.request import Request, urlopen
from SentimentAnalyze import analyze 
from Summerizer import summerizer
from keys import CLAUDE_API_KEY
from bs4 import BeautifulSoup
from IBD50_Tickers import get_tickers
from newspaper import Article


"""Scrapes news data from finviz.com"""
class NewsScraper:

    def __init__(self, tickers):
        self.tickers = tickers
        self.news_data = {}
        self.context = ssl._create_unverified_context()
        self.user_agent = {'user-agent': 'my-app'}


    """Scrapes news data for each ticker"""
    def scrape_news(self):
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

"""Parses scraped news data"""
class NewsParser:

    def __init__(self, news_data):
        self.news_data = news_data

    def parse_news_links(self):
        sorted_news_data = []
        ticker_links = {}
        for ticker, news_data in self.news_data.items():
            unique_links = set()  # Store unique links to avoid duplicates
            for row in news_data.findAll('tr'):
                if len(unique_links) > 4:
                    break
                if row.a:
                    title = row.a.text.strip()
                    link = row.a["href"]
                else:
                    title = "No headline found"
                #if link not in unique_links:  # Check for unique link before adding
                unique_links.add(link)
                sorted_news_data.append([ticker, title, link])
                    #news_links.append(link)
            ticker_links[ticker] = unique_links
        return sorted_news_data, ticker_links


"""Filters out unwanted elements from text extraction"""
def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    return True

"""Extracts visible text from HTML content"""
def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(string=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.strip() for t in visible_texts)


"""Fetches news content and performs sentiment analysis"""
def analyze_news(ticker_links):
    text = set()
    content_string = []
    for ticker in ticker_links:
        for link in ticker_links[ticker]:
            
            try:
                article = Article(link)
                article.download()
                article.parse()
                content_string.append(article.text)
                text.add(link)
                ticker_link = link
                html = Request(url=ticker_link, headers={'user-agent': 'my-app'})
                """"
                response = urlopen(html, context=ssl._create_unverified_context())
                content = response.read()
                content = text_from_html(content)
                content_string.append(content)
                """
            except Exception as e:
                print("Error fetching data for ticker", ticker)
                print(e)

        sum = 0
        count = 0
        for val in content_string:
            count += 1 
            sum += analyze(summerizer(val))
        
        print(ticker, sum/count)


tickers = get_tickers()

scraper = NewsScraper(tickers)
scraper.scrape_news()

parser = NewsParser(scraper.news_data)
sorted_news_data, ticker_links = parser.parse_news_links()

analyze_news(ticker_links)  