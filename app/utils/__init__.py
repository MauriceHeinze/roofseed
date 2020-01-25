import requests


class Tree


class Trees:
    def __init__(self, url="https://trees.codefor.de/api/"):
        self.url = url
        return

    def bound_box(self, co1, co2):
        """
        Gives trees in bound box with co1 and co2 as coordiantes of bounding box
        co1, co2 should be provided as tuples and be (x, y) and (x, y)
        """
        url = self.url + "trees/"
        params = {"in_bbox": [co1[0], co1[1], co2[0], co2[1]]}
        return self.parse(requests.get(url, params=params))

    def parse(self, response):
        """Parses Api responses to usable tree objects"""

    def find_near


    def find_trees(self, mode):
        trees = requests.get(url, params={""})
        return trees
