# -*- coding: utf-8 -*-
"""
contains the classes graph, vertex, and edge

"""


class Vertex:
    """ For use in graph data structure below """
    def __init__(self, x):
        self._element = x
        
    def getelement(self):
        return self._element
    
    def __hash__(self): #needed to allow for use in a dictionary/set
        return hash(id(self))

class Edge:
    """ For use in graph data structure below """
    def __init__(self, u, v, x):
        self._start = u
        self._end = v
        self._element = x
        
    def endpoints(self):
        return (self._origin, self._destination)
    
    def opposite(self, v): #Will return origin if v is not associated with this edge
        return self._destination if v is self._origin else self.origin 
    
    def element(self):
        return self._element
    
    def __hash__(self): #needed to allow for use in a dictionary/set
        return hash((self._origin, self._destination))
    
class Graph:
    """ For use with Edge and Vertex classes """
    
    def __init(self, directed = False):
        """ outgoing and incoming are dictionaries of dictionaries """
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing
        
    def is_directed(self):
        """ True if the graph is directed, otherwise false """
        return self._incoming is not self._outgoing
    
    def vertex_count(self):
        return len(self.__outgoing)
    
    def vertices(self):
        return self._outgoing.keys()
    
    def edge_count(self):
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total if self.is_directed() else total // 2 
    
    def edges(self):
        result = set()
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())
        return result
    
    def get_edge(self, u, v):
        return self._outgoing[u].get(v)
    
    def degree(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])
    
    def incident_edges(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge
    
    def insert_vertex(self, x = None):
        v = self.Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}
        return v
    
    def insert_edge(self, u, v, x=None):
        e = self.Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[u][v] = e
         