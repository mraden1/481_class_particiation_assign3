#implement the rest of the class
# @title
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
    plt.show()
class SampleUCS:
  def __init__(self):
    self.SampleGraph = WeightedGraph()
    self.p_queue = []  # store as (node_name, path, cost)
    self.visited = {}  # store as {node_name: {path:, cost:,}}

  # you may add (a lot) more helper functions here

  def getEdgeCost(self,start_node,end_node):
    if end_node not in self.SampleGraph.all_nodes[start_node]:
      print("edge does not exist!")
      return -1
    return self.SampleGraph.all_nodes[start_node][end_node]

  def expandNode(self,exp_node):
    for curr_adj_node in self.SampleGraph.all_nodes[exp_node]:  #loop through p_que and visited to check if exist

      new_cost = self.getEdgeCost(exp_node,curr_adj_node) + self.visited[exp_node]["path_cost"] # new cost is curr path_cost + edge cost
      print("new cost is: "+ str(new_cost))
      new_path = self.visited[exp_node]["path"] + ", " + curr_adj_node
      print("new path is: "+ str(new_path))
      data_to_add = (curr_adj_node, new_path, new_cost)
      print("new data to add is:" + str(data_to_add))

      add_switch = True
      for curr_data in self.p_queue: # if in p_queue, check if has a lower cost than existing path
        if curr_adj_node == curr_data[0]:
          print("node "+ curr_data[0] +" visited before with cost " +str(curr_data[2])+" is expanded")
          if new_cost > curr_data[2]: # do not add if new cost is higher
            print("path not updated bc a lower cost path is already in queue")
            add_switch = False
      for curr_node in self.visited:
        if curr_node == curr_adj_node: # if already in visited, do not add
          print("path not added bc already visited")
          add_switch = False

      if add_switch == True:  # if not exist, add to p_que
        print("### append node "+ str(curr_adj_node) +" to p_queue ###")
        self.p_queue.append(data_to_add)

    self.p_queue.sort(key=lambda tup: tup[2])   # sort p_que by path cost after adding all data into p_queue
    return

  def sampleUCS(self, start_node, target_node):
    #implement your algorithm here
    print("start with start node: " + str(start_node))
    self.visited[start_node]={"path":start_node,"path_cost":0}
    self.expandNode(start_node)
    path_found = False
    while len(self.p_queue) != 0:
      data_to_add = self.p_queue[0]
      visit_node_name = data_to_add[0]
      print("=========================")
      print("expanding node "+ str(data_to_add[0]))
      print("data to add to visited: " + str(data_to_add))
      visit_node_path = data_to_add[1]
      visit_node_cost = data_to_add[2]
      self.visited[visit_node_name] = {"path": visit_node_path, "path_cost": visit_node_cost}   # visit 1st in p_queue
      data_holder = self.p_queue.pop(0)
      print("pop visited node " +str(data_holder)+ " from p_queue")
      print("current p_queue content: "+str(self.p_queue))
      if visit_node_name == target_node:  # if the node visited is target
        print("target node found with path " + str(visit_node_path))
        return
      self.expandNode(visit_node_name)  # expand node
    # if reaching here, node is not found, print failure and end program
    if path_found == False:
      print("Fail to find target!")
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

import pprint
import ipywidgets as widgets

G = SampleUCS()
G.SampleGraph.addNode("A", {"B":2,"E":3})
G.SampleGraph.addNode("B", {"A":2,"C":3,"F":3})
G.SampleGraph.addNode("C", {"B":2,"D":3,"G":3})
G.SampleGraph.addNode("D", {"C":2,"H":3})

G.SampleGraph.addNode("E", {"A":3,"I":3})
G.SampleGraph.addNode("F", {"B":2,"J":3,"E":3,"G":3})
G.SampleGraph.addNode("G", {"C":2,"K":3,"F":3,"H":3})
G.SampleGraph.addNode("H", {"D":2,"L":3,"G":3})

G.SampleGraph.addNode("I", {"E":2,"J":3})
G.SampleGraph.addNode("J", {"F":2,"I":3,"K":3})
G.SampleGraph.addNode("K", {"G":2,"J":3,"L":3})
G.SampleGraph.addNode("L", {"H":2,"K":3})

pprint.pprint(G.SampleGraph.all_nodes)
print(G.getEdgeCost('A','B'))
print(G.getEdgeCost('A','E'))
print(G.getEdgeCost('K','J'))

G.SampleGraph.plotWeightedGraph()
G.sampleUCS("A","L")

"""


G.visited["A"]={"path":"A","path_cost":0}
G.expandNode("A")
print(str(G.p_queue))
print(str(G.visited))

G.visited["B"]={"path":"A, B","path_cost":2}
G.expandNode("B")
print(str(G.p_queue))
print(str(G.visited))
'''
print(str(G.p_queue))
G.expandNode("C")
print(str(G.p_queue))
'''
"""