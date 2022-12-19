from matrix_utils import display_matrix, create_edges_matrix, maxmul
from similarity import get_similarity_matrix

"""
Graph A:
0 -> 1
  <-

"""

edges_1 = [
    (0, 1),
    (1, 2),
    (2, 0),
    (3, 4), (4, 5), (5, 6)
]
edges_2 = [
    (0, 1), (1, 0)
]
edges_3 = [
    (0, 1), (1, 2), (2, 3)
]
edges_4 = [
    (0, 1), (1, 0),
    (2, 3), (3, 4), (4, 5), (5, 2),
    (6, 7), (7, 8), (8, 9), (9, 10)
]
edges_5 = [
    (0, 1), (1, 0),
    (2, 3), (3, 4), (4, 2), (4, 5),
    (7, 8), (8, 9), (9, 10), (10, 11), (11, 12)
]

A = create_edges_matrix(edges_1)
B = create_edges_matrix(edges_2)
C = create_edges_matrix(edges_3)
D = create_edges_matrix(edges_4)
E = create_edges_matrix(edges_5)

display_matrix(get_similarity_matrix(A, C, matmul=maxmul))
display_matrix(get_similarity_matrix(D, B, matmul=maxmul))
display_matrix(get_similarity_matrix(D, C, matmul=maxmul))
display_matrix(get_similarity_matrix(E, C, matmul=maxmul))
display_matrix(get_similarity_matrix(E, B, matmul=maxmul))
