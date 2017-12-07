#!/usr/bin/env false

import decomp_validate as dv


class Validator(object):
    def __init__(self):
        pass

    def validate(self, hypergraph, decomposition):
        pass

    def decomposition_type(self):
        return dv.decompositions.TreeDecomposition

    def graph_type(self):
        return dv.decompositions.TreeDecomposition.graph_type()
