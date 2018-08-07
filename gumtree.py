import requests
from bs4 import BeautifulSoup

class Search:
    def __init__(self, category="all", query="", location="", min_price="", max_price=""):
        self.category = category
        self.query = query
        self.location = location
        self.min_price = min_price
        self.max_price = max_price
        self.do_search()
        
    def do_search(self):
        """ Completes a Gumtree search. """
        request = requests.get("http://www.gumtree.com/search?q=%s&search_location=%s&category=%s&min_price=%s&max_price=%s" % (self.query, self.location, self.category, self.min_price, self.max_price))

        if request.status_code == 200:
            items = []
            links = []
            self.items = []
            self.links = []
            soup = BeautifulSoup(request.text, "html.parser")
            for item in soup.find_all("h2", {"class":"listing-title"}):
                items.append(item.text)
            for link in soup.find_all("a", {"class":"listing-link"}, href=True):
                links.append(link["href"])
            print("Found {} items.".format(len(items)))
            for x in range(len(links)):
                if str(links[x]) != "":
                    self.links.append("http://www.gumtree.com{}".format(str(links[x])))
                    tmp = str(items[x])
                    tmp = tmp.replace("\n", "", tmp.count("\n"))
                    self.items.append(tmp)
        else:
            print("Error {}".format(request.status_code))
