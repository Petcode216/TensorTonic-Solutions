import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write code here
    #1st way
    # sum = 0.0
    # for i in range(len(x)):
    #     sum += x[i]* y[i]
    # return sum

    #2nd way
    return float(np.dot(x,y))