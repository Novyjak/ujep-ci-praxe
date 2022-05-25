from scipy.spatial import distance as dist
import numpy as np
np.random.seed(42)
objectCentroids = np.random.uniform(size=(2, 2))
centroids = np.random.uniform(size=(3, 2))
D = dist.cdist(objectCentroids, centroids)
D
D.min(axis=1)
rows = D.min(axis=1).argsort()
rows
D.argmin(axis=1)
cols = D.argmin(axis=1)[rows]
cols
print(list(zip(rows, cols)))
