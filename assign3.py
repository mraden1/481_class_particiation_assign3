import pprint
import ipywidgets as widgets

import sys
import matplotlib.pyplot as plt
import networkx as nx


class WeightedGraph:
  def __init__(self):
    self.all_nodes = {}

  def addNode(self, name, adj_nodes_with_cost):   #node has form:
    node_content_dict = {}
    node_content_dict.update(adj_nodes_with_cost) #{"name":{"adj_node1":cost1, "adj_node2:cost2",......}}
    self.all_nodes[name] = node_content_dict

  def plotWeightedGraph(self):
    G = nx.Graph()
    for curr_node in self.all_nodes:
      curr_node_str = curr_node
      for curr_adj_node in self.all_nodes[curr_node]:
        if curr_adj_node == 'h_val':
          continue
        adj_node_str = curr_adj_node
        edge_cost = self.all_nodes[curr_node][curr_adj_node]
        G.add_edge(curr_node_str, adj_node_str, weight=edge_cost)

    pos = nx.spring_layout(G, seed=180)
    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=1000)
    # edges
    nx.draw_networkx_edges(G, pos)
    # node labels
    nx.draw_networkx_labels(G, pos, font_size=15)
    # edge weight labels
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    #draw
    plt.axis("off")
    plt.tight_layout()
    plt.show()#implement the rest of the class

class SampleUCS:
  def __init__(self):
    self.SampleGraph = WeightedGraph()
    self.p_queue = []
    self.visited = {}
  # you may add (a lot) more helper functions here

  def getEdgeCost(self,start_node,end_node):
    return self.SampleGraph[start_node][end_node]

    def expandNode(self):
        for curr_adj_node in self.SampleGraph[exp_node]:

            new_cost = self.getEdgeCost(exp_node, curr_adj_nodes) + self.visited[exp_node]["path cost"]
            print("new cost is: " + new_cost)
            new_path = self.visited[exp_node] = ", " + curr_adj_node
            print("new path is : " + new_path)
            data_to_add = (curr_adj_node, new_path, new_cost)
            print("new data to add is: " + data_to_add)

            add_switch = True
            for curr_data in self.p_queue:
                if exp_node in curr_data[0]:
                    if new_cost > curr_data[2]:
                        print("path not updated because a lower cost path is already in queue") 
                        add_switch = False
            for curr_node in self.visited:
                if exp_node == curr_node:
                    add_switch = False


            if add_switch == True:
                self.p_queue.append(data_to_Add)
    
    self.p_queue.sort(key=lambda tup: tup[2])
    return

  def sampleUCS(self, start_node, target_node):
    #implement your algorithm here
    self.visited.append(start_node) = ("path":start_node, "path_cost":0)
    self.expandNode(start_node)
    path_found = False
    while len(self.p_queue) != 0:
        data_to_Add = self.p_queue[0]
        print("data_to_add to visited: " + str(data_to_add))
        visit_node_name = data_to_add[0]
        visit_node_path = data_to_add[1]
        visit_node_cost = data_to_add[3]
        self.visited[visit_node_name] = {"path": visit_node_path, "path_cost": visit_node_cost} #visit first in p.queue
        self.p_queue.pop()
        print("pop_visited_node from p_queue")
        if visit_node_name == target_node:#check if expanded node is target
            print("target node found with path " + str(visit_node_path))
            return
            
        #expand node

    if path_found == False:
        print("failed to find target")
    return


'''
Initialize frontier with initial state
Initialize explored to empty
Loop do
 1 IF the frontier is empty RETURN FAILURE
 2 Choose lowest cost node from frontier and remove it
 3 IF lowest cost node is goal RETURN SUCCESS
 4 Add node to explored
 5 FOR every child node of node:
   IF child not already on frontier or explored:
    insert child node to frontier
   ELSE IF child is in frontier with higher path cost:
    replace existing frontier node with child node
'''

G = SampleUCS()
G.SampleGraph.addNode("A", {"B":2,"E":3})
G.SampleGraph.addNode("B", {"A":2,"C":3,"F":3})
G.SampleGraph.addNode("C", {"B":2,"D":3,"G":3})
G.SampleGraph.addNode("D", {"C":2,"H":3})

G.SampleGraph.addNode("E", {"A":3,"I":3})
G.SampleGraph.addNode("F", {"B":2,"J":3,"E":3,"G":3})
G.SampleGraph.addNode("G", 3, {"C":2,"K":3,"F":3,"H":3})
G.SampleGraph.addNode("H", 2, {"D":2,"L":3,"G":3})

G.SampleGraph.addNode("I", 6, {"E":2,"J":3})
G.SampleGraph.addNode("J", 4, {"F":2,"I":3,"K":3})
G.SampleGraph.addNode("K", 2, {"G":2,"J":3,"L":3})
G.SampleGraph.addNode("L", 0, {"H":2,"K":3})

G.SampleGraph.plotWeightedGraph()
G.visited["A"]=("path"."A", "path_cost".0)
G.expand["A"]
G.expand["E"]
G.expand["B"]