import numpy as np
import graphviz as gv


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
    print()
    vertices = np.concatenate([
        [ind],
        firstCol[secondCol == ind],
        secondCol[firstCol == ind]
    ])
    vertices = np.unique(np.sort(vertices))
    vertices_set = set(vertices)
    edges_with_ind = np.asarray([[i, j] for i, j in edges if i in vertices_set and j in vertices_set])

    return vertices, edges_with_ind


def get_similarity_matrix(A, B):
    Z1 = np.array([[1 for i in range(len(A))] for j in range(len(B))])
    Zk = Z1
    print("Starting iterations")
    for i in range(100):
        Zk = iterate(Zk, A, B)
        Zk = iterate(Zk, A, B)
    return Zk


def iterate(Zk, A, B):
    first = np.matmul(B, Zk)
    first = np.matmul(first, A.T)
    second = np.matmul(B.T, Zk)
    second = np.matmul(second, A)
    Zk1 = np.add(first, second)
    Zk1 = Zk1 / np.linalg.norm(Zk1)
    return Zk1


def draw_graph(vertices, names, edges):
    g = gv.Digraph('graph',
                   engine='neato',
                   graph_attr=dict(splines='true',
                                   overlap='scale'),
                   node_attr=dict(shape='plaintext',
                                  margin='0',
                                  fontsize='10', ),
                   edge_attr=dict(arrowsize='0.4'))
    g.engine = 'circo'
    for v in vertices:
        g.node(str(v), label=names[v])
    for e in edges:
        g.edge(str(e[0]), str(e[1]))
    print("viewing")
    g.view()


# =================== START ========================


def main():
    words = load_words()
    edges = load_edges()

    word = input("Please type a word from dictionary: ")

    if word not in words:
        print("Word is not in dictionary!")
        exit(400)
    word_ind = np.where(words == word)[0][0]
    print("Word index: ", word_ind)

    vertices, edges = get_neighborhood_graph(word_ind, edges)

    vertices_mappings = dict((j, i) for i, j in enumerate(vertices))
    # draw_graph(vertices, words, edges)
    n = len(vertices)
    edges_matrix = [[0 for i in range(n)] for j in range(n)]
    for i, j in edges:
        edges_matrix[vertices_mappings[i]][vertices_mappings[j]] = 1
    edges_matrix = np.array(edges_matrix)

    A = np.array([[0, 1, 0], [0, 0, 1], [0, 0, 0]])
    similarity_matrix = get_similarity_matrix(A, edges_matrix)
    similarity_scores = [i[1] for i in similarity_matrix]
    similarity_scores = [(j, i) for (i, j) in enumerate(similarity_scores)]
    similarity_scores.sort(reverse=True)

    reverse_mappings = dict(enumerate(vertices))
    for i, j in similarity_scores[:30]:
        h = reverse_mappings[j]
        # print(i, words[h])
        l1 = len(edges[edges[:, 1] == h])
        l2 = len(edges[edges[:, 0] == h])
        print(i, "|", l1, " -> ", words[h], " -> ", l2, " = ", l1 + l2)


main()
