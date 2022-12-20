import numpy as np

from dict import load_words, load_edges, remove_common_words, input_word, display_synonyms
from draw import draw_graph
from matrix_utils import create_mapped_edges_matrix, get_neighborhood_graph
from similarity import get_similarity_matrix, get_central_scores

english_index_dir = r'croatian/index.txt'
english_dico_dir = r'croatian/dico.txt'


def main():
    words = load_words(english_index_dir)
    edges = load_edges(english_dico_dir)
    edges = remove_common_words(words, edges)

    word_ind = input_word(words)
    vertices, edges = get_neighborhood_graph(word_ind, edges)
    edges_matrix, vertices_mappings, reverse_mappings = create_mapped_edges_matrix(edges, vertices)

    # draw_graph(vertices, words, edges)

    A = np.array([[0, 1, 0], [0, 0, 1], [0, 0, 0]])
    similarity_matrix = get_similarity_matrix(A, edges_matrix)
    similarity_scores = get_central_scores(similarity_matrix)

    display_synonyms(reverse_mappings, similarity_scores, word_ind, words)


main()
