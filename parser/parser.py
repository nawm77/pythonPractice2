import csv
import networkx as nx

building_graph = nx.Graph()

for floor_number in range(1, 6):
    if(floor_number != 2):
        with open(f'{floor_number}st.csv', 'r') as file:
            reader = csv.reader(file, delimiter=';')
            rows = list(reader)
        floor_graph = nx.Graph()
        stairs_row = None
        stairs_column = None
        for i, row in enumerate(rows):
            for j, cell in enumerate(row):
                if 'лестница' not in cell.lower() and cell.strip() and cell.strip() != '99999':
                    # Проверяем, что переменные не равны None
                    if stairs_row is not None and stairs_column is not None:
                        source_node = rows[i][stairs_column].strip()
                        target_node = rows[stairs_row][j].strip()
                        floor_graph.add_edge(source_node, target_node, time=int(cell.strip()))

                else:
                    floor_graph.add_node(cell.strip())

        for i, row in enumerate(rows):
            for j, cell in enumerate(row):
                if i != stairs_row and j != stairs_column:
                    if cell.strip() and cell.strip() != '99999':
                        source_node = rows[i][stairs_column].strip()
                        target_node = rows[stairs_row][j].strip()
                        print(floor_number)
                        floor_graph.add_edge(source_node, target_node, time=int(cell.strip()))
        building_graph = nx.compose(building_graph, floor_graph)
nx.write_graphml(building_graph, 'building_graph.graphml')
