# %%  Using numpy module
import numpy as np
print(np.linalg.inv([[1, 3, -1], [2, 5, 1], [-1, -4, 2]]))

# %%


def inverseMatrix(x):
    if len(x) == len(x[0]):
        determinant = (x[0][0]*(x[1][1]*x[2][2] - x[1][2]*x[2][1])) + (x[0][1]*(
            x[1][0]*x[2][2] - x[1][2]*x[2][0])) + (x[0][2]*(x[1][0]*x[2][1] - x[1][1]*x[2][0]))
        if determinant != 0:
            our_matrix_ = x
            identity_matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

            indices = list(range(len(x)))

            for fd in range(len(x)):
                fdScaler = 1 / our_matrix_[fd][fd]

                for j in range(len(x)):
                    our_matrix_[fd][j] *= fdScaler
                    identity_matrix[fd][j] *= fdScaler

                for i in indices[0:fd] + indices[fd+1:]:
                    crScaler = our_matrix_[i][fd]

                    for j in range(len(x)):
                        our_matrix_[i][j] = our_matrix_[i][j] - \
                            crScaler * our_matrix_[fd][j]
                        identity_matrix[i][j] = identity_matrix[i][j] - \
                            crScaler * identity_matrix[fd][j]

            print("The inverse of your matrix is:")
            for row in identity_matrix:
                print([x for x in row])
        else:
            print(
                "The determinant of this matrix is 0.")
    else:
        print("This is not a square matrix")


# call function
our_matrix_ = [[1, 3, -1], [2, 5, 1], [-1, -4, 2]]
inverseMatrix(our_matrix_)
