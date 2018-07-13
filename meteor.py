import os
import praw
from selenium import webdriver

os.system('cls')
reddit = praw.Reddit('bot1')

class Meteorigon(object):

    def __init__(self):
        self.sub_storage = [] 
        self.driver = None

    # search for articles containing key words
    def search_titles(self):    	
        count = 0
        user_sub = input("Which subreddit? ")
        user_article = input("Name of article? ")
        subreddit = reddit.subreddit(user_sub)

        for submission in subreddit.hot(limit=3):
            if(user_article in submission.title.lower()):
                count+=1
                print(count,": ", submission.title)
                print("Comments: ", submission.num_comments)
                print("Score: ", submission.score)
                print("URL: ", submission.url)
                print("Comments: ", submission.permalink)
                print("")
               	self.sub_storage.insert(count-1, submission.permalink)
        print(count, " articles found")
        print("")

    # return links
    def get_links(self):
        return(self.sub_storage)

    # open link in browser
    def open_link(self, i):
        print(self.sub_storage[i])
        print("")
        temp_url = "http://www.reddit.com" + self.sub_storage[i]
        driver = webdriver.Firefox()
        driver = driver.get(temp_url)
