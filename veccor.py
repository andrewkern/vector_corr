import numpy as np


# porting over code for the Crosby et al (1993)
# vector correlation

def veccor(u1, v1, u2, v2):
    """
    input is two vector timeseries
    u is angle? v is magnitude?
    """
    
    u1 -= np.mean(u1)
    v1 -= np.mean(v1)
    u2 -= np.mean(u2)
    v2 -= np.mean(v2)
    x = np.array([u1,v1,u2,v2])
    sigma = np.cov(x)
    f1 = sigma[0,0] * ((sigma[2,2] * sigma[1,3]**2) + (sigma[3,3] * sigma[1,2]**2))
    f2 = sigma[1,1] * ((sigma[2,2] * sigma[1,3]**2) + (sigma[3,3] * sigma[1,2]**2))
    f3 = 2 * sigma[0,1] * sigma[0,3] * sigma[1,2] * sigma[2,3]
    f4 = 2 * sigma[0,1] * sigma[0,2] * sigma[1,3] * sigma[2,3]
    f6 = -2 * sigma[0,0] * sigma[1,2] * sigma[1,3] * sigma[2,3]
    f7 = -2 * sigma[1,1] * sigma[0,2] * sigma[0,3] * sigma[2,3]
    f8 = -2 * sigma[2,2] * sigma[0,1] * sigma[0,3] * sigma[1,3]
    f9 = -2 * sigma[3,3] * sigma[0,1] * sigma[0,2] * sigma[1,2]

    g1 = sigma[0,0] * sigma[1,1] - sigma[0,1]**2
    g2 = sigma[2,2] * sigma[3,3] - sigma[2,3]**2
    print(x)
    print(sigma)
    print(f1,f2,f3,f4,f6,f7,f8,f9)
    print(g1,g2)
    r = (f1 + f2 + f3 + f4 +  f6 + f7 + f8 + f9) / (g1 * g2)
    return r


u1 = np.array([1., 2., 3.])
v1 = np.array([10.,1.,5.])
u2 = u1 
v2 = v1 

print(veccor(u1,v1,u2,v2))
