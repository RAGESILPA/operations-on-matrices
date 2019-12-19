#using python numpy some algebraic function
import numpy as np
a=np.array(input('enter the 2*2 matrix'));
b=np.array(input('enter the 2*2 matrix'));
print(a);
print(b);
#addition of two matrixes
print('addition of two matrixes',np.add(a,b));
#subtraction of two matrixes
print('subtraction of two matrixes',np.subtract(a,b));
#multiplication of two matrixes
print('multiplication of two matrixes',np.matmul(a,b));
#trace of matrixe 'a'
print('trace of matrixe a',np.trace(a));
#trace of matrix 'b'
print('trace of matrix b',np.trace(b));
#transpose of matrix 'a'
print('transpose of matrix a',np.transpose(a));
#rank of matrix 'a'
print('rank of a',np.linalg.matrix_rank(a));
#rank of matrix 'b'
print('rank of b',np.linalg.matrix_rank(b));
#determent of matrix 'a'
print('determinant of a',np.linalg.det(a));
#inverse of matrix 'a'
print('inverse of a',np.linalg.inv(a));
#eigenvectors of matrix 'a'
print('eigenvectors a',np.linalg.eig(a)[1]);
#squareroot of matrix 'a'
print('square root a',np.sqrt(a));
#squareroot of matrix
print('square root b',np.sqrt(b));


																
