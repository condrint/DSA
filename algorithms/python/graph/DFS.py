# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 11:39:07 2017

@author: Trenton
"""

import graph

def DFS(graph, start, discovered = {start : None}):
    """ perform dfs on a graph, 
        where discovered maps vertices (keys) to 
        edges (values) they were discovered by """
        
        for edge in graph.inident_edges(start): #creates iterator of outgoing edges from start    
            vertex = edge.opposite(start)
            if vertex not in discovered:
                discovered[vertex] = edge
                DFS(graph, vertex, discovered)