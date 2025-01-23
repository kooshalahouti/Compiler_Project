grammar Clustering;

program: imports loadData preprocessData applyClustering evaluateResults visualization EOF;

imports:
    'import numpy as np'
    'import pandas as pd'
    'from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering'
    'from sklearn.preprocessing import StandardScaler'
    'import matplotlib.pyplot as plt';

loadData: 'data = pd.read_csv(' STRING_LITERAL ')';

preprocessData:
    'scaler = StandardScaler()'
    'data_scaled = scaler.fit_transform(data)';

applyClustering: kmeansClustering dbscanClustering aggClustering;

kmeansClustering:
    'kmeans = KMeans(n_clusters=' NUMBER_LITERAL ', random_state=42)'
    'kmeans_labels = kmeans.fit_predict(data_scaled)';

dbscanClustering:
    'dbscan = DBSCAN(eps=' FLOAT_LITERAL ', min_samples=' NUMBER_LITERAL ')'
    'dbscan_labels = dbscan.fit_predict(data_scaled)';

aggClustering:
    'agglo = AgglomerativeClustering(n_clusters=' NUMBER_LITERAL ')'
    'agglo_labels = agglo.fit_predict(data_scaled)';

evaluateResults:
    'print(' STRING_LITERAL ', np.unique(kmeans_labels))'
    'print(' STRING_LITERAL ', np.unique(dbscan_labels))'
    'print(' STRING_LITERAL ', np.unique(agglo_labels))';

visualization:
    'plt.scatter(data_scaled[:, 0], data_scaled[:, 1], c=kmeans_labels, cmap=' STRING_LITERAL ')'
    'plt.title(' STRING_LITERAL ')'
    'plt.show()';

STRING_LITERAL: '"' (~["\\] | '\\' .)* '"';
NUMBER_LITERAL: [0-9]+;
FLOAT_LITERAL: [0-9]+ '.' [0-9]+;

WS: [ \t\r\n]+ -> skip;
