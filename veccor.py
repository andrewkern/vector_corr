import numpy as np

# porting over code for the Crosby et al (1993)
# vector correlation

def veccor(u1, v1, u2, v2):
    """
    input is two vector timeseries
    u is angle? v is magnitude?
    """
    
    # not sure we need to do this centering
    #u1 -= np.mean(u1)
    #v1 -= np.mean(v1)
    #u2 -= np.mean(u2)
    #v2 -= np.mean(v2)
    # stuff vectors into matrix
    x = np.array([u1,v1,u2,v2])
    # compute covariance matrix
    sigma = np.cov(x)
    # f terms are those that appear from left to right in Crosby et al
    # need to double check these-- likely bug in indexes called
    f1 = sigma[0,0] * ((sigma[2,2] * sigma[1,3]**2) + (sigma[3,3] * sigma[1,2]**2))
    f2 = sigma[1,1] * ((sigma[2,2] * sigma[0,3]**2) + (sigma[3,3] * sigma[0,2]**2))
    f3 = 2 * sigma[0,1] * sigma[0,3] * sigma[1,2] * sigma[2,3]
    f4 = 2 * sigma[0,1] * sigma[0,2] * sigma[1,3] * sigma[2,3]
    f5 = -2 * sigma[0,0] * sigma[1,2] * sigma[1,3] * sigma[2,3]
    f6 = -2 * sigma[1,1] * sigma[0,2] * sigma[0,3] * sigma[2,3]
    f7 = -2 * sigma[2,2] * sigma[0,1] * sigma[0,3] * sigma[1,3]
    f8 = -2 * sigma[3,3] * sigma[0,1] * sigma[0,2] * sigma[1,2]
    # terms in denominator
    g1 = sigma[0,0] * sigma[1,1] - sigma[0,1]**2
    g2 = sigma[2,2] * sigma[3,3] - sigma[2,3]**2

    r = (f1 + f2 + f3 + f4 +  f5 + f6 + f7 + f8) / (g1 * g2)
    return r