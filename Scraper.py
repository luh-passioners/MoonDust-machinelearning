import requests
from bs4 import BeautifulSoup
import praw
import tweepy
import tracemalloc


import redditscraper
import redditscraper.posts

url = "https://www.reddit.com/r/redditdev/comments/14zhhsb/is_there_a_way_to_scrape_more_recent_reddit_data/"
topic = "reddit"
ratelimit = 10

redditscraper.posts.getComments(url, topic, 10)