# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 16:15:53 2021

@author: dorothy
"""

import numpy as np


def func(x):
    res = x**2
    return(res)

def simpson(func, x, dx, n):
    """
    evaluates the integral by simpsons rule
    n is the number of integration intervals
    the lower bound is x and the upper bound is x+n*dx
    """
    # Create list of weights
    weights = [1]
    if (n-1)%2 == 0:
        max = int((n-1)/2)
        weights += max*[4,2]
        weights += [1]
    elif (n-1)%2 == 1:
        max = int((n-2)/2)
        weights += max*[4,2]
        weights += [4,1]
    weights = np.array(weights)
    integral = 0.
    for i in range(0,n+1):
        func_comp = func(x+(i*dx))
        # calculate the product of the function at func(x+(i*dx)) 
        # and its corresponding weight
        integral += func_comp*weights[i]
    integral = integral*(dx/3.)
    return (integral)


