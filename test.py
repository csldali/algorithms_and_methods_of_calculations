# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 11:04:16 2018

@author: Zina
"""

import numpy as np
import sympy as sym
import matplotlib.pyplot as plt


def Spline3GI(X, F, a0, b0):
    x = sym.Symbol('x')
    n = len(X) - 1
    a = F[0:n]
    h = (b0 - a0) / n
    A = np.diag(4 * np.ones((n - 1,))) + np.diag(np.ones((n - 2,)), k=1) + np.diag(np.ones((n - 2,)), k=-1)

    Ff = np.zeros((n - 1,))
    for i in range(n - 1):
        Ff[i] = (6 * (F[i] - 2 * F[i + 1] + F[i + 2])) / h / h
    c = np.zeros((n + 1,))
    c[1:n] = np.linalg.solve(A, Ff)  # решить СЛАУ методом прогонки!
    print(np.linalg.solve(A, Ff))
    #print(A)
    #print(Ff)
    d = np.zeros((n,))
    b = np.zeros((n,))
    S = n * [0]
    for i in range(n):
        d[i] = (c[i + 1] - c[i]) / h
        b[i] = (F[i + 1] - F[i]) / h - h / 2 * c[i] - h * h / 6 * d[i]
        S[i] = a[i] + b[i] * (x - X[i]) + c[i] / 2 * (x - X[i]) ** 2 + d[i] / 6 * (x - X[i]) ** 3
    return S


def f(x):
    return x * np.cos(x)


a = -np.pi
b = np.pi
x = sym.Symbol('x')
n = 5
h = (b - a) / n
X = np.linspace(a, b, num=n+1)
F = f(X)
S = Spline3GI(X, F, a, b)
XX = np.linspace(a, b)
S3 = np.zeros(XX.shape)
num = 0
for i in range(len(XX)):
    if XX[i] > X[num + 1]:
        num += 1
    S3[i] = S[num].subs(x, XX[i])
fig, ax = plt.subplots()
ax.plot(XX, f(XX), color='blue')
ax.plot(XX, S3, color='green', ls='--')
ax.scatter(X, F, marker='o', color='red')
