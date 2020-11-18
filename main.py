import sys


def import_data_to_adjacency_dict(filename):
    '''
    Imports the data into list of vertices and edges.
    :param filename:
    :return:
    '''
    with open(filename, 'r') as file:
        data = file.readlines()

    number_of_nodes = int(data[0])
    number_of_edges = int(data[number_of_nodes+1])
    adjacency = dict()

    for vertex in data[1:number_of_nodes+1]:
        adjacency[int(vertex)] = []
    for edges in data[number_of_nodes + 2: number_of_nodes + 2 + number_of_edges]:
        node_1, node_2, weight = edges.split()
        adjacency[int(node_1)].append((int(node_2), int(weight)))
        adjacency[int(node_2)].append((int(node_1), int(weight)))
    return adjacency


def get_sp_dijkstra(adjacency, start_vertex, end_vertex):
    '''
    does dijkstra (or something like it :P) and returns the distance requested.
    :param adjacency:
    :param start_vertex:
    :param end_vertex:
    :return:
    '''
    dist_to_vert = [(start_vertex, 0)]
    shortest_path_tree_set = set()
    while end_vertex not in shortest_path_tree_set:
        current = min({i for i in dist_to_vert if i[0] not in shortest_path_tree_set}, key=lambda t: t[1])
        shortest_path_tree_set.add(current[0])
        for i in adjacency[current[0]]:
            dist_to_vert.append((i[0], i[1] + current[1]))
    for potential_end in dist_to_vert:
        if potential_end[0] == end_vertex:
            return potential_end[1]
    return None


if __name__ == '__main__':
    if len(sys.argv) < 3:
        raise Exception('Arguments not given')
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    adjacency_dict = import_data_to_adjacency_dict('open-street-maps-data.dat')
    if start not in adjacency_dict:
        raise Exception('Given start is not in verticies')
    if end not in adjacency_dict:
        raise Exception('Given end is not in verticies')
    path_length = get_sp_dijkstra(adjacency_dict, start, end)
    if not path_length:
        raise Exception('Given end could not be reached from start')
    print(path_length)
