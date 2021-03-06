import requests


class TreeException(Exception):
    """Exception reserved for Trees API Bind"""


class Tree:
    def __init__(self, id, x, y, **kwargs):
        self.id = id
        self.x = x
        self.y = y
        for key, val in kwargs.items():
            self.__setattr__(key, val)  # properries support

    def description(self):
        return f"<p>{self.species_german.title()} {self.location_number}<hr> \
                Planted in {self.year_of_planting }<br>{self.address }<p>"



class TreeGroup:
    def __init__(self, trees, count=0, raw_type="", next=None, previous=None):
        self.trees = trees
        self.count = count
        self.raw_type = raw_type
        self.next = next
        self.previous = previous

    def add_tree(self, tree):
        """Convience method for self.trees.append(tree)"""
        self.trees.append(tree)

    def pop_tree(self, index):
        """Convience method for self.trees.pop(tree)"""
        self.trees.pop(index)

    def add_next(self):
        if self.next is None:
            raise TreeException("No next available")
        else:
            next = Trees.parse(requests.get(self.next))
            self.next = next.next
            print(next.next)
            [self.trees.append(tree)
             for tree in next.trees]

    def remove_tree(self, tree):
        """Convience method for self.trees.remove(tree)"""
        self.trees.remove(tree)

    def jsonify(self):
        return [[tree.x, tree.y, tree.description()] for tree in self.trees]


class Trees:
    def __init__(self, url="https://trees.codefor.de/api/trees"):
        self.url = url
        return

    def bound_box(self, co1, co2):
        """
        Gives trees in bound box with co1 and co2 as coordiantes of bounding box
        co1, co2 should be provided as tuples and be (x, y) and (x, y)
        """
        params = {"in_bbox": [co1[0], co1[1], co2[0], co2[1]]}
        return self.parse(requests.get(self.url, params=params))

    @staticmethod
    def parse(response):
        """Parses Api responses to usable tree objects"""
        if not response.status_code == 200:
            raise TreeException(f"API respond with unexpected \
                                  {response.status_code} response")
        else:
            data = response.json()
        group = TreeGroup([], count=data["count"], raw_type=data["type"],
                          next=data["next"], previous=data["previous"])
        [group.add_tree(Tree(entry["id"], entry["geometry"]["coordinates"][0],
         entry["geometry"]["coordinates"][1], **entry["properties"]))
         for entry in data["features"]]
        return group

    def find_nearby(self, long, lat, pages=1):
        params = {"in_bbox": [long+1, lat+1, long-1, lat-1]}
        if pages == 1:
            return self.parse(requests.get(self.url, params=params))
        else:
            group = self.parse(requests.get(self.url, params=params))
            [group.add_next() for i in range(pages-1)]
            return group

    def find_bezirk(self, bezirk):
        params = {"bezirk": bezirk}
        return self.parse(requests.get(self.url, params=params))

    def find_trees(self, mode):
        trees = requests.get(self.url, params={""})
        return trees
