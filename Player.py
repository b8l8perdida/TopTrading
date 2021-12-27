import Item
import Constants

class Player:

    def __init__(self, user="Grace", pwd="Judy", profile="Grace", items=None, trust=6):

        self.user = user
        self.pwd = pwd
        self.profile = profile
        self.items = items if items is not None else []
        self.trust = trust

    def incrementTrust(self):

        self.trust = self.trust + 1

    def decrementTrust(self):

        self.trust = max(Constants.MIN_TRUST, self.trust - 1)

    def addItem(self, item):

        self.items.append(item)
        item.player = self


class Profile:

    def __init__(self):
        pass