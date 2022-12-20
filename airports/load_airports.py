import numpy as np
import pandas as pd

from matrix_utils import create_edges_matrix, display_matrix
from similarity import get_similarity_matrix, get_central_scores

airports = {}
reverse_airports = {}
k = 0


def add_airport(airport):
    global k
    if airport not in airports:
        airports[airport] = k
        reverse_airports[k] = airport
        k += 1


edges = []

print("Loading file")
df = pd.read_csv('Airports.csv')

print("Loading flights data")
for index, row in df.iterrows():
    add_airport(row.Origin_airport)
    add_airport(row.Destination_airport)
    edges.append((airports[row.Origin_airport], airports[row.Destination_airport]))

print("Airports: ", len(airports))
print("Flights:", len(edges))

A = np.array([[0, 1, 0], [0, 0, 1], [0, 0, 0]])
B = create_edges_matrix(edges)

similarity_matrix = get_similarity_matrix(A, B)
similarity_scores = get_central_scores(similarity_matrix)

for i in range(10):
    print(reverse_airports[similarity_scores[i][1]], similarity_scores[i][0])
