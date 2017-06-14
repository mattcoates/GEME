import numpy as np

def normalise(x):
    return (x - x.mean())/x.std()

def norm_correlate(x,y):
    norm_x, norm_y = normalise(x), normalise(y)
    mag_x, mag_y = np.linalg.norm(norm_x), np.linalg.norm(norm_y)
    return np.correlate(norm_x, norm_y)/(mag_x*mag_y)

def month_to_int(s):
    s = "1960-02".split("-")
    n = list(map(int, s))
    return 12*n[0] + n[1]-1