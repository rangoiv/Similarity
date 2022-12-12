import numpy as np


def display_matrix(M, p=2):
    for i, row in enumerate(M):
        print("%2d" % i, end=" ")
        for j in row:
            print(f"%.{p}f" % j, end=" ")
        print()
    print()


def create_edges_matrix(edges):
    n = max(max(i, j) for i, j in edges) + 1
    edges_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i, j in edges:
        edges_matrix[i][j] = 1
    edges_matrix = np.array(edges_matrix)
    return edges_matrix


def create_mapped_edges_matrix(edges, vertices):
    vertices_mappings = dict((j, i) for i, j in enumerate(vertices))
    reverse_mappings = dict(enumerate(vertices))
    n = len(vertices)
    edges_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i, j in edges:
        edges_matrix[vertices_mappings[i]][vertices_mappings[j]] = 1
    edges_matrix = np.array(edges_matrix)
    return edges_matrix, vertices_mappings, reverse_mappings
