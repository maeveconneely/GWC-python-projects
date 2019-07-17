"""
Twitter data project
7/10/19
"""

from twitter import *
import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from tkinter import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from wordcloud import WordCloud

# Seperated out config of plot to just do it once
def config_plot():
    fig, ax = plt.subplots()

    ax.set(xlabel='Polarity', ylabel='Number of Tweets',
           title='Graph One')
    return (fig, ax)

class matplotlibSwitchGraphs:
    def __init__(self, master, polarity, subjectivity):
        self.master = master
        self.polarity = polarity
        self.subjectivity = subjectivity
        self.bins = [-1, -.9, -.8, -.7, -.6, -.5, -.4, -.3, -.2, -.1, 0, .1, .2, .3, .4, .5, .6,
        .7, .8, .9, 1 ]

        self.frame = Frame(self.master)
        self.fig, self.ax = config_plot()
        self.graphIndex = 0
        self.canvas = FigureCanvasTkAgg(self.fig, self.master)
        self.config_window()
        self.draw_graph_one()
        self.frame.pack(expand=YES, fill=BOTH)

    def config_window(self):
        self.canvas.mpl_connect("key_press_event", self.on_key_press)
        toolbar = NavigationToolbar2Tk(self.canvas, self.master)
        toolbar.update()
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self.button = Button(self.master, text="Quit", command=self._quit)
        self.button.pack(side=BOTTOM)
        self.button_switch = Button(self.master, text="Switch Graphs",
        command=self.switch_graphs)
        self.button_switch.pack(side=BOTTOM)

    def draw_graph_one(self):
        self.ax.clear() # clear current axes
        self.ax.hist(self.polarity, bins=self.bins)
        self.ax.axis([-1, 1, 0, 75])



        self.ax.set(xlabel="Polarity", ylabel="Number of Tweets", title='Polarity')
        self.canvas.draw()

    def draw_graph_two(self):
        self.ax.clear()
        self.ax.hist(self.subjectivity, bins=self.bins)
        self.ax.axis([0, 1, 0, 75])
        self.ax.set(xlabel="Subjectivity", ylabel="Number of Tweets",
        title='Subjectivity')
        self.canvas.draw()

    def on_key_press(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, self.canvas, toolbar)

    def _quit(self):
        self.master.quit()  # stops mainloop

    def switch_graphs(self):
        # Need to call the correct draw, whether we're on graph one or two
        self.graphIndex = (self.graphIndex + 1 ) % 2
        if self.graphIndex == 0:
            self.draw_graph_one()
        else:
            self.draw_graph_two()


def search_tweets():
    with open("twitter_tokens.txt", "r") as file:
        contents = file.read()

    contents = json.loads(contents)

    dict = contents[0]

    api = Api(access_token_key=dict["ACCESS_TOKEN"], access_token_secret=dict["ACCESS_SECRET"],
    consumer_key=dict["CONSUMER_KEY"], consumer_secret=dict["CONSUMER_SECRET"])

    search = input("Enter keyword to seach: ")
    tweets = api.GetSearch(search, count=200)
    return tweets

def get_ps(tweets):
    polarity = []
    subjectivity = []
    for tweet in tweets:
        tweet = tweet.AsDict()
        tb = TextBlob(tweet["text"])
        polarity.append(round(tb.polarity, 1))
        subjectivity.append(round(tb.subjectivity, 1))

    polarity_average = 0
    subjectivity_average = 0
    index = 0
    for i in polarity:
        polarity_average += i
        subjectivity_average += subjectivity[index]
        index += 1

    print("average polarity:", polarity_average/len(polarity))
    print("average subjectivity:", subjectivity_average/len(subjectivity))
    return polarity, subjectivity




def main():
    tweets = search_tweets()
    polarity, subjectivity = get_ps(tweets)
    root = Tk()
    matplotlibSwitchGraphs(root, polarity, subjectivity)
    root.mainloop()


if __name__ == "__main__":
    main()
