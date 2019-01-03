import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
from sklearn.metrics.pairwise import pairwise_distances
from networkx.drawing.nx_agraph import graphviz_layout
from __future__ import division
import collections
from networkx.algorithms.richclub import rich_club_coefficient
import seaborn as sns
import random

# No new packages

def Hist_degree(G, Type):
    e1 = []
    e2 = []
    for e in G.edges():
        e1.append(e[0])
        e2.append(e[1])
    random.shuffle(e2) 
    random_graph= nx.DiGraph()
    random_graph.add_edges_from([(e1[i],e2[i]) for i in range(len(e1))])
    if Type == 'out':
        out_list =[]
        out_list_r = []
        for elmt in G.out_degree:
            out_list.append(elmt[1])
            
        for relmt in random_graph.out_degree : 
            out_list_r.append(relmt[1])
        x1 = pd.Series(out_list)
        x2 = pd.Series(out_list_r)
        ax = sns.distplot(x1, kde=False)   
        ax = sns.distplot(x2, kde=False, color='grey')   
  
        
    if Type == 'in':
        in_list =[]
        in_list_r = []
        for elmt in G.in_degree:
            in_list.append(elmt[1])
        for relmt in random_graph.in_degree : 
            in_list_r.append(relmt[1])
        x1 = pd.Series(in_list)
        x2 = pd.Series(in_list_r)
        ax = sns.distplot(x1, kde=False)   
        ax = sns.distplot(x2, kde=False, color='grey')   
        
    if Type == 'both':
        random_graph.to_undirected()
        both_list =[]
        both_list_r =[]
        for elmt in nx.degree(G):
            both_list.append(elmt[1])
        for relmt in random_graph.degree : 
            both_list_r.append(relmt[1])
        x1 = pd.Series(both_list)
        x2 = pd.Series(both_list_r)
        ax = sns.distplot(x1, kde=False)   
        ax = sns.distplot(x2, kde=False, color='grey')  
        
Hist_degree(G4, 'both')
    