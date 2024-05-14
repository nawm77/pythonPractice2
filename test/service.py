import csv
import networkx as nx

graph_data = []
with open('3st.csv', newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        graph_data.append(row)

G = nx.Graph()
for i, row in enumerate(graph_data):
    for j, cell in enumerate(row):
        if i != 0 and j != 0 and j < len(graph_data[0]) and i < len(graph_data):
            if cell.strip() != "" and cell.strip() != "99999":
                G.add_edge(graph_data[0][j], graph_data[i][0], weight=int(cell.strip()))
shortest_path = nx.shortest_path(G, source="1126", target="1129", weight="weight")

print("Кратчайший путь:", shortest_path)
