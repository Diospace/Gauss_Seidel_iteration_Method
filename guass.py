
import numpy as np
#Gauss Seidel iteration method
#this program is Write By Endurance ogun and is part of the Sfip program
#CopyRight:: can be use for any of your project but one should not delete this comment or claim ownship of the program.
#sign by the Sfip.inc

def G_S(A,B):
    t=float(input("the toll::"))
    L = np.tril(A)
    U = A - L
    L_inv = np.linalg.inv(L)
    x = np.zeros_like(B)
    N = 1
    M = 0
    j=0
    while True:
        for i in range(N):
            j=j+1
            print("Iteration::" + str(j))
            Ux = np.dot(U, x)
            x_new = np.dot(L_inv, B - Ux)
            M = np.allclose(x, x_new, t)
           # if np.allclose(x, x_new, t):
            #    break
            x = x_new
            print(x)

        if M:
            break
        N = N + 1



def get_matrixA(m_len,variable_type=float):
    A=[]
    for i in range(1,m_len+1):
        for j in range(1,m_len+1):
            m_col_row= float(input("enter value for \n a"+str(i)+str(j)+"::"))
            A.append(m_col_row)

    A=np.array(A).reshape(m_len,m_len)

    print(A)
    return A

def get_matrixB(m_len, variable_type=float):
    B = []
    for h in range(1, m_len + 1):
        m_col = float((input("enter value for  \n b" + str(h) + "::")))
        B.append(m_col)

    B = np.array(B).reshape(m_len, 1)
    print(B)
    return B

def get_solution():
    N=int(input("dimension of Matrix:"))
    A=get_matrixA(N)
    B=get_matrixB(N)
    G_S(A,B)


get_solution()
