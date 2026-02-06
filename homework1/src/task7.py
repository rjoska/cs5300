# Im gonna import numpy and its linalg stuff, because I need practice with it for another class
import numpy as np

A_matrix = np.array([
    [2,0],
    [0,0.25]
])

b_vector = np.array([2,3])

def do_some_linalg():
    x_vector = np.linalg.solve(A_matrix, b_vector)
    A_inv = np.linalg.inv(A_matrix)
    return x_vector, A_inv

def main():
    vect, inver = do_some_linalg()
    print(vect)
    print(inver)

if __name__ == "__main__":
    main()