import numpy as np
def estimate_pi(num_samples):
    x = np.random.rand(num_samples)
    y = np.random.rand(num_samples)
    
    inside_circle = (x**2 + y**2) <= 1.0
    
    pi_estimate = 4 * np.mean(inside_circle)
    return pi_estimate