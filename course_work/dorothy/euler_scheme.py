# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 15:53:31 2021

@author: dorothy
"""

import numpy as np

def euler(q, p, m, f, dt):
    """
    q, p, m are (n x 1) matrices where n is number of dimensions
    """
    q_dt = q + dt*p/m
    p_dt = p + dt*f
    return (q_dt, p_dt)    


def prop_euler(k, q_0, q, p, m, f, dt, n_steps):
    """
    loop over n_steps timesteps
    totaltime = t_0 + n_steps*dt
    """
    for i in range(0, n_steps+1):
        # Evaluate the force at q 
        f = -1.*k*(q-q_0)
        # Evaluate q and p at time t_0+dt
        q_dt, p_dt = euler(q, p, m, f, dt)
        # Reset the q and p values before the next timestep
        q = q_dt 
        p = p_dt
    return (q_dt, p_dt)