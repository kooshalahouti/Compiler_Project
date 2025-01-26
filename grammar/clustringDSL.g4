grammar ClusteringDSL;

script
    : statement* EOF
    ;

// Each statement can be e.g. "SET_DATASET "data.csv"", "METHOD KMEANS", "CLUSTERS 3", ...
statement
    : setDatasetStmt
    | methodStmt
    | clustersStmt
    | epsStmt
    | minSamplesStmt
    | scaleStmt
    | fitStmt
    | plotStmt
    | spectralClustersStmt
    ;

// SET_DATASET "data.csv"
setDatasetStmt
    : 'SET_DATASET' STRING
    ;

// METHOD KMEANS | DBSCAN | AGGLOMERATIVE | SPECTRAL
methodStmt
    : 'METHOD' clusteringMethod
    ;

clusteringMethod
    : 'KMEANS'
    | 'DBSCAN'
    | 'AGGLOMERATIVE'
    | 'SPECTRAL'
    ;

// CLUSTERS 3
clustersStmt
    : 'CLUSTERS' INT
    ;

// EPS 0.5
epsStmt
    : 'EPS' FLOAT
    ;

// MIN_SAMPLES 5
minSamplesStmt
    : 'MIN_SAMPLES' INT
    ;

// SCALE TRUE | FALSE
scaleStmt
    : 'SCALE' BOOL
    ;

// FIT
fitStmt
    : 'FIT'
    ;

// PLOT
plotStmt
    : 'PLOT'
    ;

// SPECTRAL can also accept cluster param, so let's do an optional
// or the user might just do CLUSTERS 3 separately. 
// We'll keep it consistent with the rest.

spectralClustersStmt
    : 'SPECTRAL_CLUSTERS' INT
    ;

// ---------- LEXER RULES ----------

BOOL
    : 'true'
    | 'false'
    ;

STRING
    : '"' ( ~["] )* '"'
    ;

INT
    : [0-9]+
    ;

FLOAT
    : [0-9]+ '.' [0-9]+
    ;

WS
    : [ \t\r\n]+ -> skip
    ;
