import numpy as np
import pandas as pd
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering, SpectralClustering
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# 1) Load dataset
data = pd.read_csv("data.csv")
X = data.values

# 2) Define model based on DSL instructions
model = KMeans(n_clusters=3, random_state=42)

# 3) Fit model & get labels
labels = model.fit_predict(X)
print("Unique cluster labels:", np.unique(labels))

# 4) Plot the results
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.title('KMeans Clustering')
plt.show()