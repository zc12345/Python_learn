# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 21:16:11 2019

@author: zc12345
@contact: 18292885866@163.com

@description:
    
@ref: https://blog.csdn.net/qq_36793545/article/details/84844867
"""
import networkx as nx
import numpy as np 
import matplotlib.pyplot as plt

def relu(x):
    return (abs(x)+x)/2

def gcn_layer(A_hat, D_hat, X, W):
    return relu(D_hat**-1 * A_hat * X * W)

def plot_graph(G, weight_name=None):
    '''
    G: a networkx G
    weight_name: name of the attribute for plotting edge weights (if G is weighted)
    '''
    plt.figure()
    pos = nx.spring_layout(G)
    edges = G.edges()
    weights = None
    
    if weight_name:
        weights = [int(G[u][v][weight_name]) for u,v in edges]
        labels = nx.get_edge_attributes(G,weight_name)
        nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
        nx.draw_networkx(G, pos, edges=edges, width=weights);
    else:
        nodelist1 = []
        nodelist2 = []
        for i in range (34):
            if G.nodes[i]['club'] == 'Mr. Hi':
                nodelist1.append(i)
            else:
                nodelist2.append(i)
#        nx.draw_networkx(G, pos, edges=edges)
        nx.draw_networkx_nodes(G, pos, nodelist=nodelist1, node_size=300, node_color='r',alpha = 0.8)
        nx.draw_networkx_nodes(G, pos, nodelist=nodelist2, node_size=300, node_color='b',alpha = 0.8)
        nx.draw_networkx_edges(G, pos, edgelist=edges,alpha =0.4)

def plot_output(G, output):
#    plt.scatter(np.array(output)[:,0],np.array(output)[:,1])
    for i in range (G.number_of_nodes()):
        if G.nodes[i]['club'] == 'Mr. Hi':
            plt.scatter(np.array(output)[i,0],np.array(output)[i,1] ,label=str(i),color='b',alpha=0.5, s=250)
            plt.text(np.array(output)[i,0],np.array(output)[i,1] ,i, horizontalalignment='center',verticalalignment='center', fontdict={'color':'black'})
        else:
            plt.scatter(np.array(output)[i,0],np.array(output)[i,1] ,label=str(i) ,color='r',alpha=0.5, s=250)
            plt.text(np.array(output)[i,0],np.array(output)[i,1] ,i, horizontalalignment='center',verticalalignment='center', fontdict={'color':'black'})

def main():
    zkc = nx.karate_club_graph()
#    plot_graph(zkc)
    order = sorted(list(zkc.nodes()))
    A = nx.to_numpy_matrix(zkc, nodelist=order)
    I = np.eye(zkc.number_of_nodes())
    A_hat = A + I
    D_hat = np.array(np.sum(A_hat, axis=0))[0]
    D_hat = np.matrix(np.diag(D_hat))
    W_1 = np.random.normal(loc=0, scale=1, size=(zkc.number_of_nodes(), 4))
    W_2 = np.random.normal(loc=0, size=(W_1.shape[1], 2))
    H_1 = gcn_layer(A_hat, D_hat, I, W_1)
    H_2 = gcn_layer(A_hat, D_hat, H_1, W_2)
    output = H_2
#    plot_output(zkc, output)
#    feature_representations = {node: np.array(output)[node] for node in zkc.nodes()}
#    print(feature_representations)

    
if __name__ == '__main__':
    main()
