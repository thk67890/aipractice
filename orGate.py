# %%

import numpy as np

def OR(x1,x2):
    w1,w2,theta = 0.4,0.5,0.3
    temp = x1 * w1 + x2 * w2
    if temp <= theta:
        return 0
    if temp > theta:
        return 1

print(OR(1,0))
# %%
