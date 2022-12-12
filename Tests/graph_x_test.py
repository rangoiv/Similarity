import numpy as np

from matrix_utils import display_matrix, create_edges_matrix
from similarity import get_similarity_matrix

"""
o     o         o    o
 \   /          | \/ |
  v v           v /\ v
   1            2<  >3
  / \           | \/ |
 v   v          v /\ v
o     o         o<  >o

1=2, 2=7, 3=8
"""

A = np.array([[0, 1, 0], [0, 0, 1], [0, 0, 0]])
edges = [
    (0, 2),
    (1, 2),
    (2, 3),
    (2, 4),
    (5, 7),
    (5, 8),
    (6, 7),
    (6, 8),
    (7, 9),
    (7, 10),
    (8, 9),
    (8, 10),
]
B = create_edges_matrix(edges)

similarity_matrix = get_similarity_matrix(B, B)

display_matrix(similarity_matrix, p=35)
print("1-2: ", similarity_matrix[2, 7])
print("1-3: ", similarity_matrix[2, 8])
print("2-3: ", similarity_matrix[7, 8])