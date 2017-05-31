import numpy as np

def gen_expander(x, y, d):
    """Returns a random bipartite graph of set sizes `x` and `y` respectively. 
    The degree of vertices on the left setis restricted to 'd'.

    Such a a graph is an exander with high probablity. See Avi Widgerson's or
    Kowalski's lecture notes.
    
    Arguments:
        x : integer
        y : integer
        d : degree of vertices ion left set

    Returns:
        A numpy array of shape `(x, y)` with entry `(i,j)` being 1 for presence 
        of an edge, 0 otherwise
    """
    mask = np.zeros((x, y), float)
    ls = np.arange(y)
    for i in range(x):
        np.random.shuffle(ls)
        mask[i, ls[:d]] = 1.0

    return mask
