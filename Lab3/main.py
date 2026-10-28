from input import numberInput, vectorInput
import numpy as np

def bag_task(c, v, n, B):
    x = np.zeros((n, B + 1), dtype=int)
    max_value = opt_kb(c, v, n - 1, B, x)
    taken_items = x_nb(v, x, n, B)
    return max_value, taken_items

def opt_kb(c, v, k, b, x):
    if k == 0:
        if v[k] <= b:
            x[k, b] == 1
            return c[k]
        else:
            return 0
    else:
        opt1 = opt_kb(c, v, k - 1, b, x)
        if v[k] <= b:
            opt2 = opt_kb(c, v, k - 1, b - v[k], x) + c[k]
            if opt1 < opt2:
                x[k, b] = 1
                return opt2
        return opt1
    
def x_nb(v, x, n, B):
    b = B
    _x = np.zeros(n)
    for l in range(n - 1, 0, -1):
        if x[l, b] == 1:
            _x[l] = 1
            b -= v[l]
    return _x

if __name__ == "__main__":
    print("Enter bag capacity (B > 0)")
    B = numberInput(int, lambda v: v > 0)
    print("Enter item count (n > 0, number of items): ")
    n = numberInput(int, lambda v: v > 0)
    
    print("Enter item costs vector c:")
    c = np.array(vectorInput(n, int))
    print("Enter item volume vector v:")
    v = np.array(vectorInput(n, int))

    print(f"Bag capacity: {B}\nItem count: {n}")
    print(f"Cost vector c:\n{c}\n")
    print(f"Volume vector v:\n{v}\n")

    max_value, taken_items = bag_task(c, v, n, B)
    print(f"Max value: {max_value}")
    print(f"Items taken: {"".join(f"{i + 1} " if v else "" for i, v in enumerate(taken_items))}")