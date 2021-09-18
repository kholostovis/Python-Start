# -*- coding: utf-8 -*-
"""
Created on Mon May 18 23:40:42 2020

@author: MAS
"""

import numpy as np
from scipy import linalg
from scipy import optimize

b = np.array([[-1,33,4,1], [0,1,1,0]])
print(b)
c = b.flatten()
print(c)
print(np.mean(c))

v1 = np.array([6,0,3])
v2 = np.array([0, -1, 2])
v3 = np.array([12,3,0]) 
m = np.array([v1, v2, v3])
print(m.shape[0])
print (np.linalg.matrix_rank(m) == m.shape[0])

X = np.array([[1,-1,-1,0], [-1,2,-1,-1], [-1,-1,2,-1], [0,-1,-1,1]])
eigenvalues, eigenvectors = linalg.eig(X)
print(eigenvalues)

Y = np.array([[2,4,0,4,1],\
              [2,4,1,1,0],\
              [1,1,1,2,2],\
              [0,1,3,2,4],\
              [2,2,2,0,2]])
K = linalg.inv(Y)

Z = np.diagonal(K)
print(np.sum(Z))

A = np.array([[0,9,19,13],\
              [1,20,5,13],\
              [12,11,3,4],\
              [2,0,0,0]])

B = np.array([[2,0,0,0],\
              [1,2,2,0],\
              [2,1,1,0],\
              [0,0,1,1]])
C = np.multiply(B,A)
print(C)