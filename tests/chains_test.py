from matrix_utils import display_matrix, create_edges_matrix, maxmul
from similarity import get_similarity_matrix

"""
Graph A:
o -> o
o -> o -> o
o -> o -> o -> o
o -> o -> o -> o -> o
o -> o -> o -> o -> o -> o

Graph B:
o -> o -> o -> o -> o -> o
"""

edges_1 = [
    (0, 1),
    (2, 3), (3, 4),
    (5, 6), (6, 7), (7, 8),
    (9, 10), (10, 11), (11, 12), (12, 13),
    (14, 15), (15, 16), (16, 17), (17, 18), (18, 19),
]
edges_2 = [
    (0, 1), (1, 2), (2, 3)
]
edges_3 = [
    (0, 1), (1, 2), (2, 3), (3, 4)
]
edges_4 = [
    (0, 1), (1, 2), (2, 3), (3, 4), (4, 5)
]
edges_5 = [
    (0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)
]
edges_6 = [
    (0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10)
]

A = create_edges_matrix(edges_1)
B = create_edges_matrix(edges_2)
C = create_edges_matrix(edges_3)
D = create_edges_matrix(edges_4)
E = create_edges_matrix(edges_5)
F = create_edges_matrix(edges_6)

display_matrix(get_similarity_matrix(A, B, matmul=maxmul))
display_matrix(get_similarity_matrix(A, C, matmul=maxmul))
display_matrix(get_similarity_matrix(A, D, matmul=maxmul))
display_matrix(get_similarity_matrix(A, E, matmul=maxmul))
display_matrix(get_similarity_matrix(A, F, matmul=maxmul))
