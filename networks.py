import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

file_path = "networks_assignment.csv"
data = pd.read_csv(file_path, index_col=0)

G = nx.Graph()

for source in data.index:
    for target in data.columns:
        weight = data.loc[source, target]
        if weight > 0:
            G.add_edge(source, target, weight=weight)

blue_nodes = ['D', 'F', 'I', 'N', 'S']
green_nodes = ['BIH', 'GEO', 'ISR', 'MNE', 'SRB', 'CHE', 'TUR', 'UKR', 'GBR', 'AUS', 'HKG', 'USA']
yellow_nodes = ['AUT', 'BEL', 'BGR', 'HRV', 'CZE', 'EST', 'FRA', 'DEU', 'GRC', 'HUN', 'IRL', 'ITA', 'LVA', 'LUX', 'NLD', 'PRT', 'ROU', 'SVK', 'SVN', 'ESP']

node_colors = []
for node in G.nodes:
    if node in blue_nodes:
        node_colors.append("#35a2b5")
    elif node in green_nodes:
        node_colors.append("#35b56f")
    elif node in yellow_nodes:
        node_colors.append("#ffd000")
    else:
        node_colors.append("black")  # if not classified

pos = {}
pentagram_nodes = ["D", "F", "I", "N", "S"]
pentagram_positions = nx.circular_layout(pentagram_nodes)
pos.update(pentagram_positions)

outer_nodes = [node for node in G.nodes if node not in pentagram_nodes]
outer_positions = nx.circular_layout(outer_nodes, scale=2.0)
pos.update(outer_positions)

plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color="black", node_size=800, font_size=11, font_color="white")

# plt.title("Network Graph", fontsize=16)
# plt.tight_layout()
plt.show()
