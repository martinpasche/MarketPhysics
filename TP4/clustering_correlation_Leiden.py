from numpy import linalg as LA
import numpy as np
import pandas as pd



def compute_filtered_C(R):
    ### fillme
    pass


from sknetwork.clustering import Leiden
from scipy import sparse


def LeidenCorrelationClustering(C_s):   # C_s is the filtered correlation matrix

    ##fillme: ensure posivity of

    adjacency = sparse.csr_matrix(C_s)   # C_s is not sparse but it is the only current format that works for now.


    leiden = Leiden()
    labels = leiden.fit_predict(adjacency)

    return labels