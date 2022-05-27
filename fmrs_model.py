
# Parameter - functional relationships
# Parameters = {
#     'conc'     : {'dynamic': 'model_glm', 'params': ['conc_stim1','conc_stim2','conc_drift','conc_intercept']},
#     'gamma'    : 'fixed',
#     'sigma'    : {'dynamic': 'model_glm', 'params': ['sigma_stim1','sigma_stim2','sigma_drift','sigma_intercept']},
#     'eps'      : 'fixed',
#     'baseline' : 'fixed',
#     'Phi_0'    : 'fixed',
#     'Phi_1'    : 'fixed'}

Parameters = {
    'conc'     : {'dynamic': 'model_glm', 'params': [f'beta{i}' for i in range(4)]},
    'gamma'    : 'fixed',
    'sigma'    : {'dynamic': 'model_glm', 'params': [f'beta{i}' for i in range(4)]},
    'eps'      : 'fixed',
    'baseline' : 'fixed',
    'Phi_0'    : 'fixed',
    'Phi_1'    : 'fixed'}

# Bounds on free fitted parameters
Bounds = {
    'gamma': (0, None),
    'beta3': (0, None)}


# Dynamic models
from numpy import dot

def model_glm(params, desmat):
    return dot(desmat, params)


# Dynamic model gradients
def model_glm_grad(params, desmat):
    return desmat.T
