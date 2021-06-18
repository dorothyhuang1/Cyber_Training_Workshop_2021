# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 15:53:31 2021

@author: dorothy
"""

import numpy as np

def lpfrg(q_prev, k, q, q_0, p, m, dt):
    """
    q, p, m are (n x 1) matrices where n is number of dimensions
    """
    f = -1.*k*(q-q_0)
    q_dt = 2.*q - q_prev + 2.*(dt**2)*f/m
    return (q_dt)    


def prop_lpfrg(k, q_0, q, q_prev, p, m, f, dt, n_steps):
    """
    loop over n_steps timesteps
    totaltime = t_0 + n_steps*dt
    """
    for i in range(0, n_steps+1):
        # Evaluate q and p at time t_0+dt
        q_dt = lpfrg(q_prev, q, q_0, p, m, dt)
        # Reset the q_prev values before the next timestep
        q_prev = q
        # Reset the q before the next timestep
        q = q_dt 
    return (q_dt)