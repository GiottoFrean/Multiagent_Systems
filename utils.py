import numpy as np
from scipy.optimize import linprog
from scipy.spatial import HalfspaceIntersection, ConvexHull
from itertools import combinations

# Lemke-Howson stuff
def pivot(AB_inv_A,AB_inv_b,B,i):
    np.seterr(divide='ignore')
    ratio = AB_inv_b / AB_inv_A[:,i]
    np.seterr(divide='warn')
    ratio[ratio<0]=np.inf # ignore in argmin
    j_row = np.argmin(ratio)
    j = B[j_row]
    if ratio[j_row]>0 and not ratio[j_row]==np.inf:
        AB_inv_b[j_row] = AB_inv_b[j_row] / AB_inv_A[j_row,i]
        AB_inv_A[j_row] = AB_inv_A[j_row] / AB_inv_A[j_row,i]
        for row in range (len(B)):
            if not row==j_row:
                AB_inv_b[row] -= AB_inv_b[j_row]*AB_inv_A[row,i]
                AB_inv_A[row] -= AB_inv_A[j_row]*AB_inv_A[row,i]
        B[B.index(j)]=i

    return AB_inv_A,AB_inv_b,B

def lemke_howson(U1,U2):
    n,m = U1.shape
    IU1 = np.concatenate([np.eye(n),U1],axis=1)
    U2TI = np.concatenate([U2.T,np.eye(m)],axis=1)
    AB_inv_A_1 = IU1.copy()
    AB_inv_A_2 = U2TI.copy()
    AB_inv_b_1 = np.ones(n)
    AB_inv_b_2 = np.ones(m)
    B_1 = list(range(n))
    B_2 = list(range(n,n+m))
    
    AB_inv_A_2,AB_inv_b_2,B_2 = pivot(AB_inv_A_2,AB_inv_b_2,B_2,np.random.randint(n)) # random first pivot

    last_changed = 2
    for i in range(1000):
        gap = list(set(range(n+m))-set(B_1)-set(B_2))
        if(len(gap)==0):
            values_1 = np.zeros(n+m)
            values_2 = np.zeros(n+m)
            values_1[B_1] = AB_inv_b_1
            values_2[B_2] = AB_inv_b_2
            strategy_1 = values_1[n:]
            strategy_2 = values_2[:n]
            if np.sum(strategy_1)==0:
                strategy_1 = np.ones(len(strategy_1))
            if np.sum(strategy_2)==0:
                strategy_2 = np.ones(len(strategy_2))
            strategy_1 = strategy_1/np.sum(strategy_1)
            strategy_2 = strategy_2/np.sum(strategy_2)
            return strategy_1,strategy_2
        else:
            if last_changed==2:
                AB_inv_A_1,AB_inv_b_1,B_1 = pivot(AB_inv_A_1,AB_inv_b_1,B_1,gap[0])
                last_changed = 1
            else:
                AB_inv_A_2,AB_inv_b_2,B_2 = pivot(AB_inv_A_2,AB_inv_b_2,B_2,gap[0])
                last_changed = 2

