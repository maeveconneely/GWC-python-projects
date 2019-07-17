"""
Part three of twitter data projet
7/11/19
"""
import tweets1
from wordcloud import WordCloud
import matplotlib.pyplot as plt

filtered_words = ["RT", "https", "co", "and", "the", "about"]




def generate_wordcloud(tweets):
    str = ""
    for tweet in tweets:
        #get the text from the tweet
        tweet = tweet.AsDict()
        text = tweet["text"]

        # get rid of the RT and links that come with the text
        for i in filtered_words:
            if i in text:
                text = text[:text.find(i)] + text[text.find(i) + len(i):]

        str += text + " "


    #generate wordcloud
    wordcloud = WordCloud().generate(str)

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

def main():
    tweets = tweets1.search_tweets()
    generate_wordcloud(tweets)

main()
