from SentimentAnalyze import analyze
from Summerizer import summerizer
from Social_Media_Scraper import scrape_for_board
from Social_Media_Scraper import scrape_investorhub_board
from Social_Media_Scraper import Calculate_Score


# text = "Apple (AAPL -1.22%) stock is in a funk. Late to the artificial intelligence game, Apple recently had to iPhone Google for assistance. The latest data on iPhone sales is disheartening -- shipments are down 37% year to date in China. With so much bad news, it's no surprise that Apple stock has lost more than $20 of its value since late January. And now here comes the worst news: Apple's stock price may not recover anytime soon.In fact, according to Maxim Group analyst Tom Forte, Apple stock could be dead money for a prolonged period.Is Apple stock a buy?Now it's worth pointing out: Even Forte isn't saying Apple stock is a sell -- he just doesn't think it's going to go up much anytime soon, setting a $178 price target over the next year, and so rates Apple hold.And why does he think that? As StreetInsider reports, Apple gets 18.9 of its revenue from China -- where its iPhone sales are cratering under government pressure to stop using the devices. And seeing as iPhone accounts for the majority of Apple's operating profit, that's a big drag on growth at Apple. While the company has had some success growing services revenue, the drag on hardware sales, as well as increased regulatory scrutiny of monopolies around the globe, could prevent Apple from growing its sales -- or its stock price -- much at all over the near term.Or the long term, either.Consider that most analysts see Apple's profits growing at only about 10% annually over the next five years. That's not a bad growth rate, exactly. But on a stock that costs more than 26 times earnings, it may not be fast enough to sustain the stock price. For a high-quality, high-profit-margin company like Apple, you might not expect to ever see a PEG ratio of exactly 1 -- but unless Apple can find a way to revive iPhone sales, a 2.5 PEG is probably too much to pay for Apple's stock.Should you invest $1,000 in Apple right now?Before you buy stock in Apple, consider this:The Motley Fool Stock Advisor analyst team just identified what they believe are the 10 best stocks for investors to buy now… and Apple wasn’t one of them. The 10 stocks that made the cut could produce monster returns in the coming years.Consider when Nvidia made this list on April 15, 2005... if you invested $1,000 at the time of our recommendation, you’d have $466,882!*Stock Advisor provides investors with an easy-to-follow blueprint for success, including guidance on building a portfolio, regular updates from analysts, and two new stock picks each month. The Stock Advisor service has more than quadrupled the return of S&P 500 since 2002*."
# small_Text = summerizer(text)
# sentiment_score = analyze(small_Text)
# print("Sentiment Score:", sentiment_score)

Top_Comments = scrape_investorhub_board("dogecoin")
Score = Calculate_Score(Top_Comments)
print(Score)



