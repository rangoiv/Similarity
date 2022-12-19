import numpy as np

from matrix_utils import maxmul


def get_similarity_matrix(A, B, k=100, matmul=np.matmul):
    Z1 = np.array([[1 for _ in range(len(A))] for _ in range(len(B))])
    Zk = Z1
    for i in range(k):
        Zk = __iterate(Zk, A, B, matmul)
        Zk = __iterate(Zk, A, B, matmul)
    return Zk


def __iterate(Zk, A, B, matmul):
    # Use np.multiply for normal similarity scores
    first = matmul(B, Zk)
    first = matmul(first, A.T)
    second = matmul(B.T, Zk)
    second = matmul(second, A)
    Zk1 = np.add(first, second)
    Zk1 = Zk1 / np.linalg.norm(Zk1)
    return Zk1


def get_central_scores(B):
    M = np.matmul(B.T, B) + np.matmul(B, B.T)
    eig_vals, eig_vectors = np.linalg.eig(M)
    max_eig_ind = np.argmax(eig_vals)
    return np.real(eig_vectors[:, max_eig_ind])


