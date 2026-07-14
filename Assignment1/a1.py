
# Implement news subscription model using best practices learnt here, where a Subscriber can Subscriber
# to news/updates on in a mobile app, as soon as a new update is published(new object created),
# all Subscriberd Subscribers should get notification message.
# a1

from abc import ABC, abstractmethod
from enum import Enum


class Subscriber(ABC):
    def __init__(self, name):
        self._name = name
        self.News: list[NewsArticle] = []

    def update(self, news: NewsArticle):
        self.News.append(news)

    def Inbox(self):
        print(f"Inbox of {self._name} ({self.type()} Subscriber)")
        for index, news in enumerate(self.News):
            print(index+1, ".")
            news.print()

    @abstractmethod
    def type(self):
        pass

    @abstractmethod
    def canReceive(self, category: NewsCategory):
        pass

class PremiumListener(Subscriber):
    def type(self):
        return NewsCategory.PremiumListener
    def canReceive(self, category: NewsCategory):
        return True

class SimpleListener(Subscriber):
    def type(self):
        return NewsCategory.SimpleListener
    def canReceive(self, category: NewsCategory):
        return self.type() == category

class NewsCategory(Enum):
    SimpleListener = "Simple"
    PremiumListener = "Premium"

class NewsArticle:
    def __init__(self, title, author, text, category: NewsCategory = NewsCategory.SimpleListener):
        self.title = title
        self.author = author
        self.category = category
        self.text = text

    def print(self):
        print(f"  Title:    {self.title}")
        print(f"  Author:   {self.author}")
        print(f"  Category: {self.category.value}")
        print(f"  Content:  {self.text}\n")

class NewsStation:
    def __init__(self):
        self._listeners: list[Subscriber] = []

    def Subscribe(self, listener: Subscriber):
        if listener not in self._listeners:
            self._listeners.append(listener)

    def unSubscribe(self, listener: Subscriber):
        if listener in self._listeners:
            self._listeners.remove(listener)

    def notify(self, news: NewsArticle):
        for listener in self._listeners:
            if listener.canReceive(news.category):
                listener.update(news)

    def PublishNews(self, title, author, text, category: NewsCategory = NewsCategory.SimpleListener):
        news = NewsArticle(title, author, text, category)
        self.notify(news)

if __name__ == "__main__":
    news_station = NewsStation()
    l1 = SimpleListener("Ali")
    l2 = PremiumListener("Omer")

    news_station.Subscribe(l1)
    news_station.Subscribe(l2)

    news_station.PublishNews("Death of Democracy", "Asma Jahangir", "lorem Ipsum", NewsCategory.PremiumListener)
    news_station.PublishNews("Death of Politics", "Omer Jahangir", "lorem Ipsum")
    news_station.PublishNews("Death of Nationalism", "Asma Jahangir", "lorem Ipsum")
    news_station.PublishNews("Partition of Pakistan", "Ali", "lorem Ipsum")
    news_station.PublishNews("Death of Democracy", "Jahangir", "lorem Ipsum", NewsCategory.PremiumListener)

    print("\n\n\nInbox of L1")
    l1.Inbox()
    print("\n\n\nInbox of L2")
    l2.Inbox()

    news_station.unSubscribe(l1)
    news_station.PublishNews("Partition of Pakistan 2", "Ali", "lorem Ipsum")
    news_station.PublishNews("Death of Democracy 2", "Jahangir", "lorem Ipsum", NewsCategory.PremiumListener)


    print("\n\n\nInbox of L1")
    l1.Inbox()
    print("\n\n\nInbox of L2")
    l2.Inbox()

