import networkx as nx
import matplotlib.pyplot as plt

class WeightedGraphWithHeuristic:
  def __init__(self):
    self.all_nodes = {}
    self.start_end = []

  def addNode(self, name, adj_nodes_with_cost):
    node_content_dict = {}                #node has form:
    node_content_dict["h_val"]= self.calculateNearest(name)  #{"name":{"h_val":heuristic, "adj_node1":cost1, "adj_node2:cost2",......}}
    node_content_dict.update(adj_nodes_with_cost)
    self.all_nodes[name] = node_content_dict


  #creates a list that stores the start node, checkpoint nodes, and end node
  def addStartEnd(self, start, first_store, second_store, end):
    self.start_end.append(start)
    self.start_end.append(first_store)
    self.start_end.append(second_store)
    self.start_end.append(end)

  #calculates the nearest of the checkpoint nodes
  def calculateNearest(self, current_node):
    distance_to_first = self.calculateVertical(current_node, self.start_end[1]) + self.calculateHorizontal(current_node, self.start_end[1])
    distance_to_second = self.calculateVertical(current_node, self.start_end[2]) + self.calculateHorizontal(current_node, self.start_end[2])

    if (distance_to_first >= distance_to_second):
        return distance_to_second
    else:
        return distance_to_first

  #calculates the vertical distance between 2 nodes
  def calculateVertical(self, begin, finish):
    lis = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    begin = begin.replace(begin[0], "", 1)
    finish = finish.replace(finish[0], "", 1)

    return (lis.index(finish) - lis.index(begin))

  #calculates the horizontal distance between 2 nodes
  def calculateHorizontal(self, begin, finish):
    lis = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]

    return (lis.index(begin[0]) - lis.index(finish[0]))

  def getStartEnd(self):
    print(self.start_end + " has been returned")
    return self.start_end

  def plotWeightedGraphWithHeuristic(self):
    G = nx.Graph()
    for curr_node in self.all_nodes:
      curr_node_str = curr_node + "\nh:" + str(self.all_nodes[curr_node]['h_val'])
      for curr_adj_node in self.all_nodes[curr_node]:
        if curr_adj_node == 'h_val':
          continue
        adj_node_str = curr_adj_node + "\nh:" + str(self.all_nodes[curr_adj_node]['h_val'])
        edge_cost = self.all_nodes[curr_node][curr_adj_node]
        G.add_edge(curr_node_str, adj_node_str, weight=edge_cost)

    pos = nx.spring_layout(G, seed=180)
    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=500)
    # edges
    nx.draw_networkx_edges(G, pos)
    # node labels
    nx.draw_networkx_labels(G, pos, font_size=10)
    # edge weight labels
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    #draw
    plt.axis("off")
    plt.tight_layout()
    plt.show()


class SampleGreedyBestFirstSearch:
  def __init__(self):
    self.SampleGraph = SampleGraph()

  #  Algorithm:
  # set start node as current node
  # loop:
  #   get the adjacent node with lowest heuristic of current node
  #   move to that node
  def greedyBestFirstSearch(self1, start_node1, target_node):
    loop_count = 0
    print("Sample Greedy Best First Search Starts")
    print("===========================================")
    curr_node = start_node
    if start_node == target_node:
      print("start node is target node!")
      print("### Program Ends ###")
      return
    curr_path = []
    while loop_count <= 50:
      curr_path.append(curr_node)
      print("visiting curr node: " + curr_node)
      print("adding curr node to path.")
      print("curr path:"+str(curr_path))
      heuristic_dict = {}                 # get the node with lowest h_val using a dict
      curr_lowest_h_val = sys.maxsize            # and a lowest h_val recorder
      print("finding adj node with lowest heuristic")
      for curr_adj_node in self.all_nodes[curr_node]:   # loop through adj_nodes of curr_node
        if curr_adj_node == target_node:        # if target node found1, end and print path
          print("=======================================")
          print("<<<<<<<<<<<< Target found! >>>>>>>>>>>>")
          print("=======================================")
          curr_path.append(curr_adj_node)
          print("Path to target:" + str(curr_path))
          print("### Program Ends ###")
          return
        if curr_adj_node == 'h_val':          # ignore h_val kv pair in loop
          continue
        curr_h_val = self.all_nodes[curr_adj_node]['h_val']  # get h_val of curr_adj_node
        if curr_h_val in heuristic_dict:
          heuristic_dict[curr_h_val].append(curr_adj_node)     # add to list if exist
        else:
          heuristic_dict[curr_h_val] = [curr_adj_node]    # add h_val node name pair into dict if not exist
        if curr_h_val < curr_lowest_h_val:       # update lowest h_val if a lower is found
          curr_lowest_h_val = curr_h_val        # note: in case of draw1, the first will be selected
      print("curr adj nodes and heuristics"+str(heuristic_dict))
      next_node = heuristic_dict[curr_lowest_h_val][0]    # this is the node with lowest h_val
      curr_node = next_node                # move to next node
      print("selecting node "+ str(next_node))
      print("========= moving to next node =========")
      loop_count += 1



"""[start:K2, 1st_store: B9, 2nd_store:D9, end:K1]"""

G = WeightedGraphWithHeuristic()
G.addStartEnd("K2", "B9", "D9", "K1")

G.addNode("A1", {"A2":2,"B1":2})
G.addNode("A2", {"A1":2,"A3":1,"B2":2})
G.addNode("A3", {"A2":1,"A4":1,"B3":1})
G.addNode("A4", {"A3":1,"A5":2,"B4":2})
G.addNode("A5", {"A4":2,"A6":1,"B5":2})
G.addNode("A6", {"A5":1,"A7":1,"B6":1})
G.addNode("A7", {"A6":1,"A8":1,"B7": 100})
G.addNode("A8", {"A7":1,"A9":1,"B8":1})
G.addNode("A9", {"A8":1,"A10":2,"B9":2})
G.addNode("A10", {"A9":2,"A11":2,"B10":1})
G.addNode("A11", {"A10":2,"A12":2,"B11":1})
G.addNode("A12", {"A11":2,"B12":2})


G.addNode("B1", {"A1":2,"B2":2,"C1":2})
G.addNode("B2", {"A2":2,"B1":2,"B3":1,"C2":2})
G.addNode("B3", {"A3":1,"B2":1,"B4":1,"C3":1})
G.addNode("B4", {"A4":2,"B3":1,"B5":2,"C4":2})
G.addNode("B5", {"A5":2,"B4":2,"B6":1,"C5":2})
G.addNode("B6", {"A6":1,"B5":2,"B7": 100,"C6":1})
G.addNode("B7", {"A7": 100,"B6": 100,"B8": 100,"C7": 100})
G.addNode("B8", {"A8":1,"B7": 100,"B9":2,"C8":2})
G.addNode("B9", {"A9":2,"B8":2,"B10":1,"C9":1})
G.addNode("B10", {"A10":1,"B9":1,"B11":1,"C10":1})
G.addNode("B11", {"A11":1,"B10":1,"B12":1,"C11":1})
G.addNode("B12", {"A12":2,"B11":1,"C12":2})


G.addNode("C1", {"B1":2,"C2":2,"D1":2})
G.addNode("C2", {"B2":2,"C1":2,"C3":1,"D2":2})
G.addNode("C3", {"B3":1,"C2":1,"C4":1,"D3":1})
G.addNode("C4", {"B4":2,"C3":1,"C5":2,"D4":2})
G.addNode("C5", {"B5":2,"C4":2,"C6":1,"D5":2})
G.addNode("C6", {"B6":1,"C5":1,"C7": 100,"D6":1})
G.addNode("C7", {"B7": 100,"C6": 100,"C8": 100,"D7": 100})
G.addNode("C8", {"B8":2,"C7": 100,"C9":1,"D8":2})
G.addNode("C9", {"B9":1,"C8":1,"C10":1,"D9":1})
G.addNode("C10", {"B10":1,"C9":1,"C11":1,"D10":1})
G.addNode("C11", {"B11":1,"C10":1,"C12":1,"D11":1})
G.addNode("C12", {"B12":2,"C11":1,"D12":2})


G.addNode("D1", {"C1":2,"D2":2,"E1":1})
G.addNode("D2", {"C2":2,"D1":2,"D3":1,"E2":1})
G.addNode("D3", {"C3":1,"D2":1,"D4":1,"E3":1})
G.addNode("D4", {"C4":2,"D3":1,"D5":2,"E4":1})
G.addNode("D5", {"C5":2,"D4":2,"D6":1,"E5":1})
G.addNode("D6", {"C6":1,"D5":1,"D7": 100,"E6":1})
G.addNode("D7", {"C7": 100,"D6": 100,"D8": 100,"E7": 100})
G.addNode("D8", {"C8":2,"D7": 100,"D9":2,"E8":1})
G.addNode("D9", {"C9":1,"D8":2,"D10":2,"E9":1})
G.addNode("D10", {"C10":1,"D9":2,"D11":1,"E10":1})
G.addNode("D11", {"C11":1,"D10":1,"D12":1,"E11":1})
G.addNode("D12", {"C12":2,"D11":1,"E12":2})

G.addNode("E1", {"D1":1,"E2":1,"F1":1})
G.addNode("E2", {"D2":1,"E1":1,"E3":1,"F2":1})
G.addNode("E3", {"D3":1,"E2":1,"E4":1,"F3":1})
G.addNode("E4", {"D4":1,"E3":1,"E5":1,"F4":1})
G.addNode("E5", {"D5":1,"E4":1,"E6":1,"F5":1})
G.addNode("E6", {"D6":1,"E5":1,"E7": 100,"F6":2})
G.addNode("E7", {"D7": 100,"E6": 100,"E8": 100,"F7": 100})
G.addNode("E8", {"D8":1,"E7": 100,"E9":1,"F8":2})
G.addNode("E9", {"D9":1,"E8":1,"E10":1,"F9":1})
G.addNode("E10", {"D10":1,"E9":1,"E11":1,"F10":1})
G.addNode("E11", {"D11":1,"E10":1,"E12":1,"F11":1})
G.addNode("E12", {"D12":2,"E11":1,"F12":2})

G.addNode("F1", {"E1":1,"F2":1,"G1":1})
G.addNode("F2", {"E2":1,"F1":1,"F3":1,"G2":1})
G.addNode("F3", {"E3":1,"F2":1,"F4":1,"G3":1})
G.addNode("F4", {"E4":1,"F3":1,"F5":1,"G4":1})
G.addNode("F5", {"E5":1,"F4":1,"F6":1,"G5":1})
G.addNode("F6", {"E6":1,"F5":1,"F7":1,"G6":1})
G.addNode("F7", {"E7":1,"F6":1,"F8":1,"G7":1})
G.addNode("F8", {"E8":1,"F7":1,"F9":1,"G8":1})
G.addNode("F9", {"E9":1,"F8":1,"F10":1,"G9":1})
G.addNode("F10", {"E10":1,"F9":1,"F11":1,"G10":1})
G.addNode("F11", {"E11":1,"F10":1,"F12":1,"G11":1})
G.addNode("F12", {"E12":1,"F11":1,"G12":1})

G.addNode("G1", {"F1":1,"G2":1,"H1":1})
G.addNode("G2", {"F2":1,"G1":1,"G3":1,"H2":1})
G.addNode("G3", {"F3":1,"G2":1,"G4":1,"H3":1})
G.addNode("G4", {"F4":1,"G3":1,"G5":1,"H4":1})
G.addNode("G5", {"F5":1,"G4":1,"G6":1,"H5":1})
G.addNode("G6", {"F6":1,"G5":1,"G7":1,"H6":1})
G.addNode("G7", {"F7":1,"G6":1,"G8":1,"H7":1})
G.addNode("G8", {"F8":1,"G7":1,"G9":1,"H8":1})
G.addNode("G9", {"F9":1,"G8":1,"G10":1,"H9":1})
G.addNode("G10", {"F10":1,"G9":1,"G11":1,"H10":1})
G.addNode("G11", {"F11":1,"G10":1,"G12":1,"H11":1})
G.addNode("G12", {"F12":1,"G11":1,"H12":1})

G.addNode("H1", {"G1":1,"H2":1,"I1":1})
G.addNode("H2", {"G2":1,"H1":1,"H3":1,"I2":1})
G.addNode("H3", {"G3":1,"H2":1,"H4":1,"I3":1})
G.addNode("H4", {"G4":1,"H3":1,"H5":1,"I4":1})
G.addNode("H5", {"G5":1,"H4":1,"H6":1,"I5":1})
G.addNode("H6", {"G6":1,"H5":1,"H7":1,"I6":1})
G.addNode("H7", {"G7":1,"H6":1,"H8":1,"I7":1})
G.addNode("H8", {"G8":1,"H7":1,"H9":1,"I8":1})
G.addNode("H9", {"G9":1,"H8":1,"H10":1,"I9":1})
G.addNode("H10", {"G10":1,"H9":1,"H11":1,"I10":1})
G.addNode("H11", {"G11":1,"H10":1,"H12":1,"I11":1})
G.addNode("H12", {"G12":1,"H11":1,"I12":1})

G.addNode("I1", {"H1":1,"I2":1,"J1":1})
G.addNode("I2", {"H2":1,"I1":1,"I3":1,"J2":1})
G.addNode("I3", {"H3":1,"I2":1,"I4":1,"J3":1})
G.addNode("I4", {"H4":1,"I3":1,"I5":1,"J4":1})
G.addNode("I5", {"H5":1,"I4":1,"I6":1,"J5":1})
G.addNode("I6", {"H6":1,"I5":1,"I7":1,"J6":1})
G.addNode("I7", {"H7":1,"I6":1,"I8":1,"J7":1})
G.addNode("I8", {"H8":1,"I7":1,"I9":1,"J8":1})
G.addNode("I9", {"H9":1,"I8":1,"I10":1,"J9":1})
G.addNode("I10", {"H10":1,"I9":1,"I11":1,"J10":1})
G.addNode("I11", {"H11":1,"I10":1,"I12":1,"J11":1})
G.addNode("I12", {"H12":1,"I11":1,"J12":1})

G.addNode("J1", {"I1":1,"J2":1,"K1":1})
G.addNode("J2", {"I2":1,"J1":1,"J3":1,"K2":1})
G.addNode("J3", {"I3":1,"J2":1,"J4":1,"K3":1})
G.addNode("J4", {"I4":1,"J3":1,"J5":1,"K4":1})
G.addNode("J5", {"I5":1,"J4":1,"J6":1,"K5":1})
G.addNode("J6", {"I6":1,"J5":1,"J7":1,"K6":1})
G.addNode("J7", {"I7":1,"J6":1,"J8":1,"K7":1})
G.addNode("J8", {"I8":1,"J7":1,"J9":1,"K8":1})
G.addNode("J9", {"I9":1,"J8":1,"J10":1,"K9":1})
G.addNode("J10", {"I10":1,"J9":1,"J11":1,"K10":1})
G.addNode("J11", {"I11":1,"J10":1,"J12":1,"K11":1})
G.addNode("J12", {"I12":1,"J11":1,"K12":1})

G.addNode("K1", {"J1":1,"K2":1,"L1":1})
G.addNode("K2", {"J2":1,"K1":1,"K3":1,"L2":1})
G.addNode("K3", {"J3":1,"K2":1,"K4":1,"L3":1})
G.addNode("K4", {"J4":1,"K3":1,"K5":1,"L4":1})
G.addNode("K5", {"J5":1,"K4":1,"K6":1,"L5":1})
G.addNode("K6", {"J6":1,"K5":1,"K7":1,"L6":1})
G.addNode("K7", {"J7":1,"K6":1,"K8":1,"L7":1})
G.addNode("K8", {"J8":1,"K7":1,"K9":1,"L8":1})
G.addNode("K9", {"J9":1,"K8":1,"K10":1,"L9":1})
G.addNode("K10", {"J10":1,"K9":1,"K11":1,"L10":1})
G.addNode("K11", {"J11":1,"K10":1,"K12":1,"L11":1})
G.addNode("K12", {"J12":1,"K11":1,"L12":1})

G.addNode("L1", {"K1":1,"L2":1})
G.addNode("L2", {"K2":1,"L1":1,"L3":1})
G.addNode("L3", {"K3":1,"L2":1,"L4":1})
G.addNode("L4", {"K4":1,"L3":1,"L5":1})
G.addNode("L5", {"K5":1,"L4":1,"L6":1})
G.addNode("L6", {"K6":1,"L5":1,"L7":1})
G.addNode("L7", {"K7":1,"L6":1,"L8":1})
G.addNode("L8", {"K8":1,"L7":1,"L9":1})
G.addNode("L9", {"K9":1,"L8":1,"L10":1})
G.addNode("L10", {"K10":1,"L9":1,"L11":1})
G.addNode("L11", {"K11":1,"L10":1,"L12":1})
G.addNode("L12", {"K12":1,"L11":1})

G.plotWeightedGraphWithHeuristic()
