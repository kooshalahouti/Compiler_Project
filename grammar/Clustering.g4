grammar Clustering;

// Root rules
program: cluster;

cluster: clustering_method '(' assign (',' assign)* ')' plot? dataset?;

clustering_method: 'KMeans' | 'DBSCAN' | 'AgglomerativeClustering' | 'SpectralClustering';

assign: VAR '=' expr;

expr: NUM | STRING | LINKAGE_TYPE | AFFINITY_TYPE | VAR;

plot: 'plot' '(' plot_args? ')';
plot_args: 'x' '=' VAR ',' 'y' '=' VAR;

dataset: 'dataset' '(' 'file' '=' STRING ')';

NUM: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
VAR: [a-zA-Z_][a-zA-Z0-9_]*;
STRING: '"' (~["\r\n])* '"';
LINKAGE_TYPE: 'ward' | 'complete' | 'average' | 'single';
AFFINITY_TYPE: 'euclidean' | 'l1' | 'l2' | 'manhattan' | 'cosine';

WS: [ \t\r\n]+ -> skip;