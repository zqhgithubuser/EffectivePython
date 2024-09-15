from collections import defaultdict


class Visits:

    def __init__(self):
        self.data = defaultdict(set)

    def add(self, country, city):
        self.data[country].add(city)


visits = Visits()
visits.add("England", "Bath")
visits.add("England", "London")
print(visits.data)
