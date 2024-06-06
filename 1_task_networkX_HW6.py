
#Транспортна мережа міста

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_nodes_from(['A', 'B', 'C', 'D', 'E'])

G.add_edge('A', 'B', weight=5)
G.add_edge('B', 'C', weight=7)
G.add_edge('C', 'D', weight=3)
G.add_edge('D', 'E', weight=6)
G.add_edge('E', 'A', weight=4)
G.add_edge('B', 'D', weight=8)

# Візуалізація графа
pos = nx.spring_layout(G)  # позиції вершин для візуалізації
nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=20, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title('Транспортна мережа міста')
plt.show()

# Аналіз основних характеристик
print("Кількість вершин:", G.number_of_nodes())
print("Кількість ребер:", G.number_of_edges())
print("Список вершин:", list(G.nodes()))
print("Список ребер:", list(G.edges()))
print("Ступінь вершин:", dict(G.degree()))
