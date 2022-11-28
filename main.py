import numpy as np

from similarity import get_similarity_matrix

common_words_threshold = 3000


def load_words():
    words = []
    with open(r'./index.txt', 'r') as fileReader:
        for line in fileReader.readlines():
            words.append(line.strip())
    return np.array(words)


def load_edges():
    edges = []
    with open(r'./dico.txt', 'r') as fileReader:
        for line in fileReader.readlines():
            splitLine = line.strip().split(" ")
            if len(splitLine) == 2:
                edges.append((int(splitLine[0]) - 1, int(splitLine[1]) - 1))
    edges = np.array(edges)
    return edges


def get_neighborhood_graph(ind, edges):
    firstCol = edges[:, 0]
    secondCol = edges[:, 1]

    vertices = np.concatenate([
        [ind],
        firstCol[secondCol == ind],
        secondCol[firstCol == ind]
    ])
    vertices = np.unique(np.sort(vertices))
    vertices_set = set(vertices)
    edges_with_ind = np.asarray([[i, j] for i, j in edges if i in vertices_set and j in vertices_set])

    return vertices, edges_with_ind


def remove_common_words(words, edges):
    common_words = get_common_words(words, edges)
    return remove_vertices(common_words, edges)


def get_common_words(words, edges):
    occurrences = [0] * len(words)
    for _, j in edges:
        occurrences[j] += 1
    nova = [(j, i) for i, j in enumerate(occurrences)]
    nova.sort(reverse=True)
    common_words = set([i for j, i in nova if j > common_words_threshold])
    return common_words


def remove_vertices(vertices_to_remove, edges):
    new_edges = []
    for edge in edges:
        if edge[1] not in vertices_to_remove:
            new_edges.append(edge)
    return np.asarray(new_edges)


def get_edge_matrix(vertices, edges):
    vertices_mappings = dict((j, i) for i, j in enumerate(vertices))
    reverse_mappings = dict(enumerate(vertices))
    n = len(vertices)
    edges_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i, j in edges:
        edges_matrix[vertices_mappings[i]][vertices_mappings[j]] = 1
    edges_matrix = np.array(edges_matrix)
    return edges_matrix, vertices_mappings, reverse_mappings


def input_word(words):
    word = input("Please type a word from dictionary: ")
    if word not in words:
        print("Word is not in dictionary!")
        exit(400)
    word_ind = np.where(words == word)[0][0]
    return word_ind


# =================== START ========================


def main():
    words = load_words()
    edges = load_edges()

    edges = remove_common_words(words, edges)

    word_ind = input_word(words)

    vertices, edges = get_neighborhood_graph(word_ind, edges)

    edges_matrix, vertices_mappings, reverse_mappings = get_edge_matrix(vertices, edges)

    # draw_graph(vertices, words, edges)

    # Method 1:
    A = np.array([[0, 1, 0], [0, 0, 1], [0, 0, 0]])
    similarity_matrix = get_similarity_matrix(A, edges_matrix)
    similarity_scores = [i[1] for i in similarity_matrix]  # Get central column of the matrix (central scores)
    similarity_scores /= np.linalg.norm(similarity_scores)  # Normalize the vector

    # Method 2:
    # similarity_scores = get_central_scores(edges_matrix)

    similarity_scores = [(j, i) for (i, j) in enumerate(similarity_scores)]
    similarity_scores.sort(reverse=True)

    for i, j in similarity_scores[:11]:
        h = reverse_mappings[j]
        if h != word_ind:
            print(i, words[h])
        # l1 = len(edges[edges[:, 1] == h])
        # l2 = len(edges[edges[:, 0] == h])
        # print(i, "|", l1, " -> ", words[h], " -> ", l2, " = ", l1 + l2)


main()
