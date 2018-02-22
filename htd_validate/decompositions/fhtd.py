import logging
from collections import defaultdict

from cStringIO import StringIO

from htd_validate.decompositions import Decomposition
from htd_validate.decompositions import GeneralizedHypertreeDecomposition
from htd_validate.utils import Hypergraph


class FractionalHypertreeDecomposition(GeneralizedHypertreeDecomposition):
    _problem_string = 'fhtd'
    _data_type = float

    @staticmethod
    def decomposition_type():
        pass

    #@staticmethod
    #def _reader(decomp, line):
    #    if line[0] == 'w':
    #        decomp.hyperedge_function[int(line[1])][int(line[2])] = float(line[3])
    #        return True
    #    return False

    @staticmethod
    def graph_type():
        return Hypergraph.__name__

    def __init__(self, plot_if_td_invalid=False):
        super(FractionalHypertreeDecomposition, self).__init__()
        self.hypergraph = Hypergraph()
        self.hyperedge_function = defaultdict(dict)

    def __len__(self):
        return len(self.bags)

    # TODO: reading allow floats as well insteat of just integers
    # TODO: technically the same as ghtd, but we skip the integer check
    def validate(self, graph):
        print self.edge_function_holds()
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
