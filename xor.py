#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

INPUT_X = np.array([[0,0], [0,1], [1,0], [1,1]])
print INPUT_X
print "\n"
EXPECTED_RESULT = np.array([[0,1,1,0]]).T
print(EXPECTED_RESULT)

print "RESULT:\n", np.append(INPUT_X,EXPECTED_RESULT, axis=1)


def sigmoid(x, deriv=False):
    if deriv:
        return x*(1-x)
    return 1/(1+np.exp(-x))

np.random.seed(0)

SYN0 = 2*np.random.random((2,1)) - 1

for i in xrange(20000):
    l0 = INPUT_X
    l1 = sigmoid(np.dot(l0, SYN0))
    l1_error = EXPECTED_RESULT - l1
    
    l1_delta = l1_error * sigmoid(l1, True)
    SYN0 += np.dot(l0.T, l1_delta)
    if (i % 1000) == 0 :
        print "Error:" + str(np.mean(np.abs(l1_error)))

print l1