import numpy as np
import random
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_curve, auc

# Set the seed
random.seed(420)
np.random.seed(420)

num_samples = 100

# Generate sorted random samples
weight = np.sort(np.random.normal(loc=172, scale=29, size=num_samples))

print(weight)
