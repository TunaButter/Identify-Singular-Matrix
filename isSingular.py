import numpy as np

def isSingular(A):
    B = np.array(A, dtype=float)
    try:
        nrow = np.size(B, 0)
        for i in range(nrow):
            fixRow(B, i)
    except IsSingular:
        return True
    return False
    
class IsSingular(Exception): 
    pass

def fixRow(A, r):
    for i in range(r):
        A[r] = A[r] - A[i] * A[r, i]
    
    for i in range(np.size(A, 0)-r-1):
        if A[r, r] == 0:
            A[r] = A[r] + A[r+i+1]
            for i in range(r):
                A[r] = A[r] - A[i] * A[r, i]
    if A[r, r] == 0:
        raise IsSingular('The matrix is singular.')
            
    A[r] = A[r] / A[r,r]
        
def main():
    A = [[0, 3, 2], 
         [0, 1, 4], 
         [0, 0, 2]]
    if isSingular(A):
        print('singular')
    else:
        print('not singular')

if __name__ == "__main__":
    main()