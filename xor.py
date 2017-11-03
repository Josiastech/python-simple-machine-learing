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