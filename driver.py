import os
import praw

os.system('cls')
reddit = praw.Reddit('bot1')

class Meteorigon(object):

    # search for a particular article within a subreddit
    def search_titles(self): 
        count = 0
        user_sub = input("Which subreddit? ")
        user_article = input("Name of article? ")
        subreddit = reddit.subreddit(user_sub)

        for submission in subreddit.hot(limit=20):
            if(user_article in submission.title.lower()):
                count+=1
                print(count,": ", submission.title)
                print("Comments: ", submission.num_comments)
                print("Score: ", submission.score)
                print("URL: ", submission.url)
                print("Comments: ", submission.permalink)
                print("")

        print(count, " articles found")