from input import numberInput, matrixInput
import numpy as np

def dynamic_straight(A, P, Q):
    B = np.zeros((P, Q), dtype=int)
    C = np.zeros((P, Q), dtype=int)
    for p in range(P):
        for q in range(Q):
            if p == 0:
                B[p, q] = A[p, q]
                C[p, q] = q
            else:
                for i in range(q + 1):
                    new_value = A[p, i] + B[p - 1, q - i]
                    if B[p, q] < new_value:
                        B[p, q] = new_value
                        C[p, q] = i
    print(f"B:\n{B}")
    print(f"C:\n{C}")
    return B[P - 1, Q - 1], C

def dynamic_reverse(C, P, Q):
    p = P
    q = Q - 1
    distribution = np.zeros(P)
    while p > 0:
        p = p - 1
        distribution[p] = C[p, q]
        q = q - C[p, q]
    return distribution

if __name__ == "__main__":
    print("Enter matrix height (p > 0, number of restrictions (agents)): ")
    p = numberInput(int, lambda v: v > 0)
    print("Enter vectors size (q > 0, number of variables (resources)): ")
    q = numberInput(int, lambda v: v > 0)
    q = q + 1
    
    print("Enter matrix A (Agent-resource cost matrix):")
    A = np.array(matrixInput(q, p))

    print(f"Agents count: {p}\nResources count: {q-1}")
    print(f"Matrix A:\n{A}\n")

    result, C = dynamic_straight(A, p, q)
    distribution = dynamic_reverse(C, p, q)
    print(f"Max income: {result}")
    print(f"Per-agent resource distribution:\n {distribution}")