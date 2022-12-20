from matrix_utils import display_matrix, create_edges_matrix, maxmul
from similarity import get_similarity_matrix

"""
Graph A:
0 -> 1
  <-

"""

edges_1 = [
    (0, 1), (1, 0)
]
edges_2 = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10)
]
edges_3 = [
    (0, 1),
    (1, 2),
    (2, 0),
    (4, 5), (5, 6), (6, 7),
    (8, 9), (9, 8), (9, 10), (10, 11),
]
edges_4 = [
    (0, 1),
    (1, 2),
    (2, 0),
    (4, 5), (5, 6), (6, 7), (7, 8),
    (8, 9), (9, 8), (9, 10), (10, 4),
]

A = create_edges_matrix(edges_1)
B = create_edges_matrix(edges_2)
C = create_edges_matrix(edges_3)
D = create_edges_matrix(edges_4)

display_matrix(get_similarity_matrix(B, A, matmul=maxmul))
display_matrix(get_similarity_matrix(C, A, matmul=maxmul))
display_matrix(get_similarity_matrix(D, A, matmul=maxmul))
