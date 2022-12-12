from matrix_utils import display_matrix, create_edges_matrix
from similarity import get_similarity_matrix

"""
Graph A:
o -> o
|    |
o -> o
o -> o -> o -> o -> o -> o

Graph B:
o -> o -> o -> o -> o -> o

1=2, 2=7, 3=8
"""

edges_1 = [
    (0, 1),
    (1, 2),
    (1, 3),
    (1, 4),
    (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11)
]
edges_2 = [
    (0, 1), (1, 2), (2, 3)
]

A = create_edges_matrix(edges_1)
B = create_edges_matrix(edges_2)

display_matrix(get_similarity_matrix(A, B), p=7)
