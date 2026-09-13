from simplex_method import initial_simplex_method, np
from input import numberInput, vectorInput, matrixInput

def gomori_restriction(c, A, b):
    x, B, A, b = initial_simplex_method(c, A, b)
    if x is None:
        return None, None, None
    
    if np.all(x % 1 == 0):
        print("Simplex method returned optimal plan with integer numbers")
        return x, None, None
    
    print("Simplex method returned optimal plan containing float number, applying Gomori's restriction")
    k = np.argmax(x % 1 != 0)
    x_i = x[k]

    B = [i - 1 for i in B]
    N = []
    N = [i for i in range(len(x)) if i not in B]

    AB = A[:, B]
    AN = A[:, N]
    x_b = x[B]
    x_n = x[N]

    AB_inv = []
    try:
        AB_inv = np.linalg.inv(AB)
    except np.linalg.LinAlgError:
        print("Basis matrix AB cannot be inverted")
        return None, None, None
    
    Q = AB_inv @ AN
    
    l = Q[k, :]
    for n in l:
        n = n - int(n)

    x_i_float = x_i - int(x_i)
    x_l = np.zeros(len(x))
    for l_i, n_i in zip(l, N):
        x_l[n_i] = l_i

    return x_l, x_i_float, N

if __name__ == "__main__":
    print("Enter matrix height (m > 0, number of restrictions): ")
    m = numberInput(int, lambda v: v > 0)
    print("Enter vectors size (n > 0, number of variables): ")
    n = numberInput(int, lambda v: v > 0)

    print("Enter target functional coefficients vector-column c: ")
    c = vectorInput(n)

    print("Enter matrix A (constraint coefficients):")
    A = matrixInput(n, m)

    print("Enter right-parts vector vector b:")
    b = vectorInput(m)

    print(f"Vector c:\n{c}\n")
    print(f"Matrix A:\n{A}\n")
    print(f"Vector b:\n{b}\n")

    l, x, N = gomori_restriction(c, A, b)
    if l is not None and x is not None and N is not None:
        restriction = ""
        for l_i, i in zip(l, range(len(l))):
            if i in N:
                restriction += f"{l_i}*x{i + 1}"
                restriction += f" - s = {x}" if i + 1 == len(l) else " + "
        print(f"Gomori restriction: {restriction}")
    elif l is not None:
        print(f"Optimal plan: {l}")