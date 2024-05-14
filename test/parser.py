import csv
import networkx as nx
for number in range(1, 6):
    if(number != 2):
        name = f'{number}st.csv'
        with open(name, 'r') as file:
            reader = csv.reader(file, delimiter=';')
            rows = list(reader)
        G = nx.Graph()
        points = rows[0][1:]
        for point in points:
            G.add_node(point)
        for i, row in enumerate(rows[1:], start=1):
            source_point = points[i - 1]
            for j, time in enumerate(row[1:], start=1):
                target_point = points[j - 1]
                if time and time != '99999':
                    G.add_edge(source_point, target_point, time=time)
        nx.write_graphml(G, f'{number}st.graphml')
