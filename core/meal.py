import requests
from bs4 import BeautifulSoup
from datetime import datetime
import shelve

now = datetime.now()
f = shelve.open("meal.db")

class Meal:
    def __init__(self):
        self.y = now.year
        self.m = now.month
        self.d = now.day
        self.meal = self.get_meal(self.y, self.m, self.d)
        self.update_meal()
        self.write_meal()

    def get_raw(self, y, m, d):
        """
        Gets raw meal HTML from http://hana.hs.kr/life/meal.asp
        """
        date = {"yy": y, "mm": m, "dd": d}
        r = requests.get("http://hana.hs.kr/life/meal.asp", params=date)
        r.encoding = "utf-8"
        return r.text

    def parse_meal(self, raw):
        """
        Parses raw meal HTML into a list
        """
        meals = []
        soup = BeautifulSoup(raw, "lxml")
        for e in soup.select_one(".today_meal").find_all("td"):
            meals.append(e.text)
        return meals

    def get_meal(self, y, m, d):
        """
        Uses get_raw() and parse_meal() to return meals.
        Defaults to current year, month, and day if not specified.
        """
        if y == None:
            y = now.year
        if m == None:
            m = now.month
        if d == None:
            d = now.day

        raw = self.get_raw(y, m, d)
        return self.parse_meal(raw)


    def update_meal(self):
        self.y = 2019
        self.m = 3
        self.d = 29
        self.meal = self.get_meal(self.y, self.m, self.d)
        print(self.meal)


    def write_meal(self):
        f["breakfast"] = self.meal[0]
        f["lunch"] = self.meal[1]
        f["dinner"] = self.meal[2]
        f["snack"] = self.meal[3]
        f.close()
