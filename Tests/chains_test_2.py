from matrix_utils import display_matrix, create_edges_matrix
from similarity import get_similarity_matrix

"""
Graph A:
o -> o
|
o -> o -> o
o -> o -> o -> o
o -> o -> o -> o -> o
o -> o -> o -> o -> o -> o

Graph B:
o -> o -> o -> o -> o -> o

1=2, 2=7, 3=8
"""

edges_1 = [
    (0, 1),
    (0, 2),
    (2, 3), (3, 4),
    (5, 6), (6, 7), (7, 8),
    (9, 10), (10, 11), (11, 12), (12, 13),
    (14, 15), (15, 16), (16, 17), (17, 18), (18, 19),
]
edges_2 = [
    (0, 1), (1, 2), (2, 3), (3, 4), (4, 5)
]
edges_3 = [
    (0, 1), (1, 2), (2, 3), (3, 4)
]
edges_4 = [
    (0, 1), (1, 2), (2, 3)
]

A = create_edges_matrix(edges_1)
B = create_edges_matrix(edges_2)
C = create_edges_matrix(edges_3)
D = create_edges_matrix(edges_4)

display_matrix(get_similarity_matrix(A, B))
display_matrix(get_similarity_matrix(A, C))
display_matrix(get_similarity_matrix(A, D))
