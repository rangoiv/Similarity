import numpy as np


def load_words(index_dir):
    words = []
    with open(index_dir, 'r', encoding='utf8') as fileReader:
        for line in fileReader.readlines():
            words.append(line.strip())
    return np.array(words)


def load_edges(dico_dir):
    edges = []
    with open(dico_dir, 'r') as fileReader:
        for line in fileReader.readlines():
            splitLine = line.strip().split(" ")
            if len(splitLine) == 2:
                edges.append((int(splitLine[0]) - 1, int(splitLine[1]) - 1))
    edges = np.array(edges)
    return edges


def remove_common_words(words, edges, common_words_threshold=3000):
    common_words = _get_common_words(words, edges, common_words_threshold)
    return _remove_vertices(common_words, edges)


def _get_common_words(words, edges, common_words_threshold):
    occurrences = [0] * len(words)
    for _, j in edges:
        occurrences[j] += 1
    nova = [(j, i) for i, j in enumerate(occurrences)]
    nova.sort(reverse=True)
    common_words = set([i for j, i in nova if j > common_words_threshold])
    return common_words


def _remove_vertices(vertices_to_remove, edges):
    new_edges = []
    for edge in edges:
        if edge[1] not in vertices_to_remove:
            new_edges.append(edge)
    return np.asarray(new_edges)


def input_word(words):
    word = input("Please type a word from dictionary: ")
    if word not in words:
        print("Word is not in dictionary!")
        exit(400)
    word_ind = np.where(words == word)[0][0]
    return word_ind


def display_synonyms(reverse_mappings, similarity_scores, word_ind, words):
    for i, j in similarity_scores[:11]:
        h = reverse_mappings[j]
        if h != word_ind:
            print(i, words[h])
        #     l1 = len(edges[edges[:, 1] == h])
        #     l2 = len(edges[edges[:, 0] == h])
        #     print(i, "|", l1, " -> ", words[h], " -> ", l2, " = ", l1 + l2)