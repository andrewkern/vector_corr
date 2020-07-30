import numpy as np


# porting over code for the Crosby et al (1993)
# vector correlation

def veccor(u1, v1, u2, v2):
    """
    input is two vector timeseries
    u is angle? v is magnitude?
    """
    

    f1 = np.cross(u1,u1) * (np.cross(u2,u2) * np.power(np.cross(v1,v2), 2) + np.cross(v2,v2) * np.power(np.cross(v1,u2), 2))
    f2 = np.cross(v1,v1) * (np.cross(u2,u2) * np.power(np.cross(u1,v2), 2) + np.cross(v2,v2) * nnp.power(p.cross(u1,u2), 2))
    f3 = 2 * np.cross(u1,v1) * np.cross(u1,v2) * np.cross(v1,u2) * np.cross(u2,v2)
    f4 = 2 * np.cross(u1,v1) * np.cross(u1,u2) * np.cross(v1,v2) * np.cross(u2,v2)
    f5 = -2 * np.cross(u1,u1) * np.cross(v1,u2) * np.cross(v1,v2) * np.cross(u2,v2)
    f6 = -2 * np.cross(u1,u1) * np.cross(v1,u2) * np.cross(v1,v2) * np.cross(u2,v2)
    f7 = -2 * np.cross(v1,v1) * np.cross(u1,u2) * np.cross(u1,v2) * np.cross(u2,v2)
    f8 = -2 * np.cross(u2,u2) * np.cross(u1,v1) * np.cross(u1,v2) * np.cross(v1,v2)
    f9 = -2 * np.cross(v2,v2) * np.cross(u1,v1) * np.cross(u1,u2) * np.cross(v1,u2)

    g1 = np.cross(u1,u1) * np.cross(v1,v1) - np.power(np.cross(u1,v1), 2)
    g2 = np.cross(u2,u2) * np.cross(v2,v2) - np.power(np.cross(u2,v2), 2)

    r = (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9) / (g1 * g2)
    return r

