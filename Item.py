import networkx as nx


class Item:

    def __init__(self, tradingtime=float("inf"), location=None, name=None):

        if type(tradingtime) is not float:
            raise TypeError("Error! Type of time must be float!")
        self.tradingtime = tradingtime
        self.location = location
        self.name = name

    def setPreference(self, preference):
        self.preference = preference

    def __repr__(self):
        return str(self.name)

class Algo:

    def __init__(self, items):

        self.items = items
        self.underrated_items = []

    def check_cycle(self, cycle):
        l = len(cycle)
        bad_items = []
        for cyc in cycle:
            if cyc[0].player.trust < l:
                bad_items.append(cyc[0])
        m = min([t.player.trust for t in bad_items]) if len(bad_items) else 0
        self.underrated_items.append(cyc[0])

        return [item for item in bad_items if item.trust == m]

    def exe(self, trust=False):

        cycles = []

        g = nx.DiGraph()
        g.add_nodes_from(self.items)

        while len(g.nodes):
            for item in list(g.nodes):
                g.add_node(item)
                while item.preference[0] not in g.nodes:
                    item.preference.pop(0)
                g.add_edge(item, item.preference[0])

            while(True):
                try:
                    cycle = nx.algorithms.cycles.find_cycle(g)
                    if trust is True:
                        bad_items = self.check_cycle(cycle)

                        g.remove_edges_from([(bad_item, bad_item.preference[0]) for bad_item in bad_items])
                        g.add_edges_from([(bad_item, bad_item.preference[1]) for bad_item in bad_items])
                        for bad_item in bad_items:
                            bad_item.preference.pop(0)

                        if len(bad_items):
                            continue

                    cycles.append(cycle)
                    remove = [e[0] for e in cycle]
                    g.remove_nodes_from(remove)
                except nx.exception.NetworkXNoCycle:
                    break


        return cycles


