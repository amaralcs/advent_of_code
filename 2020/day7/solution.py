import re
import networkx as nx
import matplotlib.pyplot as plt
from utils import read_file

def create_edge(source, destination):
    if destination == 'no other':
        return None
    qty = re.search(r"^(\d+)", destination).group()
    name = re.search(r"(\w+\s?\w+$)", destination).group()
    return (source, name, int(qty))

def find_dag(entry, sep=" contain "):
    edge = entry.split(sep)
    edge[0] = re.sub(r" bags?\.?$", "", edge[0])
    edge[1] = edge[1].split(", ")
    edge[1] = [re.sub(r" bags?\.?$", "", val) for val in edge[1]]
    edges = [create_edge(edge[0], val) for val in edge[1]]
    return edges

def calc_traversal(G, node):
    if len(G[node]) == 0:
        return 0
    else:
        return sum([calc_traversal(G, n) * w['weight'] + w['weight'] for n, w in G[node].items()])


if __name__ == "__main__":
    data = read_file("day7/data.txt")
    graph_edges = [find_dag(entry) for entry in data]
    
    G = nx.DiGraph()
    for edge in graph_edges:
        G.add_weighted_edges_from(edge)
    
    history = nx.ancestors(G, 'shiny gold')
    print(f"There are {len(history)} bags that can hold shiny gold bag")

    ans = calc_traversal(G, 'shiny gold')
    print(f"We need {ans} bags to bring our shiny gold bag!")