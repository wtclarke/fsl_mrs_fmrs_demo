from numpy import dot

# Parameter - functional relationships
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
def model_glm(p, t):
    return dot(t, p)


# Dynamic model gradients
def model_glm_grad(p, t):
    return t.T
