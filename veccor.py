import numpy as np

# Python implementation of Crosby et al (1993)
# vector correlation
# https://doi.org/10.1175/1520-0426(1993)010%3C0355:APDFVC%3E2.0.CO;2

def veccor(u1, v1, u2, v2):
    """
    input is two vector timeseries
    cartesian coords
    """

    # stuff vectors into matrix
    x = np.array([u1,v1,u2,v2])
    # compute covariance matrix
    sigma = np.cov(x)
    # f terms are those that appear from left to right in Crosby et al
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
