grammar Clustering;

cluster: clustering_method '(' args (',' args)* ')';
clustering_method: 'KMeans' | 'DBSCAN' | 'AgglomerativeClustering' | 'SpectralClustering';

args: n_clusters | n_iters | random_state | epsilon | min_sample | linkage | affinity;

n_clusters: 'n_clusters' '=' NUM;
n_iters: 'n_iters' '=' NUM;
random_state: 'random_state' '=' NUM;
epsilon: 'epsilon' '=' FLOAT;
min_sample: 'min_sample' '=' NUM;
linkage: 'linkage' '=' LINKAGE_TYPE;
affinity: 'affinity' '=' AFFINITY_TYPE;

NUM: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
LINKAGE_TYPE: 'ward' | 'complete' | 'average' | 'single';
AFFINITY_TYPE: 'euclidean' | 'l1' | 'l2' | 'manhattan' | 'cosine';

WS : [ \t\r\n}]+ -> skip;