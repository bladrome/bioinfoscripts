import numpy as np

n_samples = 100
n_species = 100


def jaccardindex(vab_p, vab_q):
    length = len(vab_p)
    p1 = float(np.sum(vab_p)) / length
    p0 = float(length - p1) / length
    q1 = float(np.sum(vab_q)) / length
    q0 = float(length - q1) / length

    p00 = p0 * q0
    p01 = p0 * q1
    p10 = p1 * q0
    p11 = p1 * q1

    return p00, p01, p10, p11

def entropy_jaccardindex(vab_p, vab_q):
    p = jaccardindex(vab_p, vab_q)
    entropy = -np.sum(p * np.log(p))
    return entropy

def entropy(vec_a, vec_b, operation="AND"):
    if operation == "AND":
        vec_c = np.array(np.logical_and(vec_a, vec_b))
    elif operation == "OR":
        vec_c = np.array(np.logical_or(vec_a, vec_b))
    length = len(vec_c)
    p1 = np.sum(vec_c) / np.float(length)
    p0 = 1 - p1
    funlog = lambda x: 0 if x == 0 else np.log(x)
    entropy = p0 * funlog(p0) + p1 * funlog(p1)
    entropy = -entropy
    return entropy


def entropy_shuffle(vec_a, vec_b, times=10, operation="AND"):
    entropylist = list()
    for i in range(times):
        np.random.shuffle(vec_b)
        tmp = (entropy(vec_a, vec_b))
        entropylist.append(tmp)
    return entropylist


def z_score_entropy(vec_a, vec_b, times=10, operation="AND"):
    x = entropy(vec_a, vec_b)
    vec_b_copy = vec_b.copy()
    varx = entropy_shuffle(vec_a, vec_b_copy, times, operation=operation)
    x_mean = np.mean(varx)
    x_std = np.std(varx)
    return 0 if x == x_mean else (x - x_mean) / x_std


def esabo(abundance_matrix):
    col_length = len(abundance_matrix[0, :])
    row_length = len(abundance_matrix[:, 0])
    res = np.zeros(shape=(col_length, col_length), dtype=float)
    for i in range(0, col_length):
        for j in range(0, col_length):
            res[i][j] = z_score_entropy(abundance_matrix[:, i], abundance_matrix[:, j], col_length)

    return res

def esabo_jaccardindex(abundance_matrix):
    col_length = len(abundance_matrix[0, :])
    res = np.zeros(shape=(col_length, col_length), dtype=float)
    for i in range(0, col_length):
        for j in range(0, col_length):
            res[i][j] = entropy_jaccardindex(abundance_matrix[:, i], abundance_matrix[:, j])

    return res

if __name__ == "__main__":
    for i in range(10):
        np.random.seed()
        A = np.random.randint(0, 2, (n_samples, n_species))
        print(A)
        R = esabo(A)
        print(len(R[R > 0]), len(R[R < 0]))
        # R = esabo_jaccardindex(A)
        # print(len(R[R > 1]), len(R[R < 1]))
