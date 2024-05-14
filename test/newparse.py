import csv
import networkx as nx

floor_files = ['0st.csv', '1st.csv', '3st.csv', '4st.csv', '5st.csv']
#
floor_graphs = {}
for f in floor_files:
    graph_data = []
    with open(f, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            graph_data.append(row)

    G = nx.Graph()
    for i, row in enumerate(graph_data):
        for j, cell in enumerate(row):
            if i != 0 and j != 0 and j < len(graph_data[0]) and i < len(graph_data):
                if cell.strip() != "" and cell.strip() != "99999":
                    G.add_edge(graph_data[0][j], graph_data[i][0], weight=int(cell.strip()))
    floor_graphs[str(f)[0]] = G


def get_floor(point):
    return str(point)[1]


def find_start_path(start_point):
    floor = get_floor(start_point)
    if floor in floor_graphs.keys():
        G = floor_graphs[floor]
        shortest_path = nx.shortest_path(G, source=start_point, target='Гл. лестница')
        return shortest_path
    else:
        print("Этаж не найден")
        return None


def find_end_path(end_point):
    floor = get_floor(end_point)
    if floor in floor_graphs.keys():
        G = floor_graphs[floor]
        shortest_path = nx.shortest_path(G, source='Гл. лестница', target=end_point)
        return shortest_path
    else:
        print("Этаж не найден")
        return None


def find_shortest_on_floor(start, end):
    floor = get_floor(start)
    G = floor_graphs[floor]
    shortest_path = nx.shortest_path(G, source=start, target=end)
    return shortest_path


start_point = "1301"
end_point = "1320"

start_path = find_start_path(start_point)
end_path = find_end_path(end_point)

if start_path and end_path:
    if get_floor(start_point) == get_floor(end_point):
        print(find_shortest_on_floor(start_point, end_point))
    else:
        print("Путь от", start_point, "до главной лестницы:", start_path)
        print("Путь от главной лестницы до", end_point, ":", end_path)
