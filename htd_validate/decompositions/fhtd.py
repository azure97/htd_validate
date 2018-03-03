import logging
from cStringIO import StringIO

import networkx as nx
from htd_validate.decompositions import GeneralizedHypertreeDecomposition, TreeDecomposition
from htd_validate.utils import Hypergraph, HypergraphPrimalView


class FractionalHypertreeDecomposition(GeneralizedHypertreeDecomposition):
    _problem_string = 'fhtd'
    _data_type = float

    @staticmethod
    def decomposition_type():
        pass

    @staticmethod
    def from_ordering(hypergraph, ordering=None, weights=None):
        if ordering is None:
            ordering = sorted(hypergraph.nodes())
        if len(ordering) == 1:
            tree = nx.DiGraph()
            tree.add_node(1)
            chi = {1: ordering[0]}
            return FractionalHypertreeDecomposition(hypergraph=hypergraph, plot_if_td_invalid=True, tree=tree, bags=chi,
                                                    hyperedge_function=weights)

        logging.debug("Ordering: %s" % ordering)

        pgraph_view = HypergraphPrimalView(hypergraph=hypergraph)
        pgraph_decomp = TreeDecomposition.from_ordering(graph=pgraph_view, ordering=ordering)
        fhtd = FractionalHypertreeDecomposition(hypergraph=hypergraph, plot_if_td_invalid=True, tree=pgraph_decomp.T,
                                                bags=pgraph_decomp.bags, hyperedge_function=weights)
        logging.info("==== Computed Fhtd: ====")
        logging.info("Fhtd: edges=%s ; bags=%s; weights=%s" % (fhtd.T.edges(), fhtd.chi, fhtd.hyperedge_function))
        return fhtd

    # @staticmethod
    # def _reader(decomp, line):
    #    if line[0] == 'w':
    #        decomp.hyperedge_function[int(line[1])][int(line[2])] = float(line[3])
    #        return True
    #    return False

    @staticmethod
    def graph_type():
        return Hypergraph.__name__

    def __init__(self, hypergraph=None, plot_if_td_invalid=False, tree=None, bags=None, hyperedge_function=None):
        super(FractionalHypertreeDecomposition, self).__init__(hypergraph=hypergraph,
                                                               plot_if_td_invalid=plot_if_td_invalid, tree=tree,
                                                               bags=bags, hyperedge_function=hyperedge_function)
        self.plot_if_td_invalid = plot_if_td_invalid
        logging.debug('edges = %s' % self.tree.edges())

    def __len__(self):
        return len(self.bags)

    # TODO: reading allow floats as well insteat of just integers
    # TODO: technically the same as ghtd, but we skip the integer check
    def validate(self, graph):
        self.hypergraph = graph
        if self.edges_covered() and self.is_connected() and self.edge_function_holds() and \
                self.edge_function_holds():
            return True
        else:
            logging.error('ERROR in Tree Decomposition.')
            return False

    def __str__(self):
        string = StringIO()
        self.write(string)
        return string.getvalue()
