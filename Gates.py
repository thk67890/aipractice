# %%

import numpy as np

x = np.array([1,1])

def GATE(x):
    w = np.array([-0.5,-0.5])
    b = 0.7

    if np.sum(w * x) + b <= 0:
        return 0
    else:
        return 1

GATE(x)

# %%
