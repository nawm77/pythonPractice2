import networkx as nx

merged_graph = nx.Graph()
graph_list = []
for i in range(0, 6):
    if (i != 2):
        graph = nx.read_graphml(f'{i}st.graphml')
        print(i)
        print(graph)
        graph_list.append(graph)
merged_graph = nx.compose_all(graph_list)
nx.write_graphml(merged_graph, 'merged_graph.graphml')