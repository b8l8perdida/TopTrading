import Item
import unittest
import Player
import math
import numpy
from pyvis.network import Network as pyvNetwork


class AlgoTestCases(unittest.TestCase):

    def setUp(self):

        n = 10
        items = []

        players = [Player.Player(trust=max(math.sqrt(i), 6)) for i in range(n)]

        for nr, player in enumerate(players):
            item = Item.Item(name=nr)
            items.append(item)
            player.addItem(item)

        for player in players:
            preference = numpy.random.permutation(n)

            player.items[0].setPreference([players[k].items[0] for k in preference])

        self.items = items
        self.algo = Item.Algo(self.items)

    def testAlgorithmWorking(self):

        cycles = self.algo.exe()
        cycles = sum([cyc for cyc in cycles], [])
        self.assertEqual(len(cycles), len(self.items))

    def testAlgorithmTrustWorking(self):

        cycles = self.algo.exe(trust=True)

        m = min([len(cyc) for cyc in cycles])

        self.assertEqual(m, 1)

    def testPrintCycles(self):

        cycles = self.algo.exe()
        G = pyvNetwork(bgcolor="#222222", font_color="white", height="1000px",
                       width="100%", notebook=False, directed=True)

        for c in cycles:
            for e in c:
                if str(e[0]) not in G.nodes:
                    G.add_node(str(e[0]))
                if str(e[1]) not in G.nodes:
                    G.add_node(str(e[1]))
                G.add_edge(str(e[0]), str(e[1]))
        G.repulsion(spring_length=45, damping=0.5,
                    node_distance=245, spring_strength=0.00)
        G.show("example.html")
