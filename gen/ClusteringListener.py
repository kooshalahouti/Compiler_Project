# Generated from F:/university/term 7/compiler/finalproject/Compiler_Project/grammar/Clustering.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ClusteringParser import ClusteringParser
else:
    from ClusteringParser import ClusteringParser

# This class defines a complete listener for a parse tree produced by ClusteringParser.
class ClusteringListener(ParseTreeListener):

    # Enter a parse tree produced by ClusteringParser#cluster.
    def enterCluster(self, ctx:ClusteringParser.ClusterContext):
        pass

    # Exit a parse tree produced by ClusteringParser#cluster.
    def exitCluster(self, ctx:ClusteringParser.ClusterContext):
        pass


    # Enter a parse tree produced by ClusteringParser#clustering_method.
    def enterClustering_method(self, ctx:ClusteringParser.Clustering_methodContext):
        pass

    # Exit a parse tree produced by ClusteringParser#clustering_method.
    def exitClustering_method(self, ctx:ClusteringParser.Clustering_methodContext):
        pass


    # Enter a parse tree produced by ClusteringParser#args.
    def enterArgs(self, ctx:ClusteringParser.ArgsContext):
        pass

    # Exit a parse tree produced by ClusteringParser#args.
    def exitArgs(self, ctx:ClusteringParser.ArgsContext):
        pass


    # Enter a parse tree produced by ClusteringParser#n_clusters.
    def enterN_clusters(self, ctx:ClusteringParser.N_clustersContext):
        pass

    # Exit a parse tree produced by ClusteringParser#n_clusters.
    def exitN_clusters(self, ctx:ClusteringParser.N_clustersContext):
        pass


    # Enter a parse tree produced by ClusteringParser#n_iters.
    def enterN_iters(self, ctx:ClusteringParser.N_itersContext):
        pass

    # Exit a parse tree produced by ClusteringParser#n_iters.
    def exitN_iters(self, ctx:ClusteringParser.N_itersContext):
        pass


    # Enter a parse tree produced by ClusteringParser#random_state.
    def enterRandom_state(self, ctx:ClusteringParser.Random_stateContext):
        pass

    # Exit a parse tree produced by ClusteringParser#random_state.
    def exitRandom_state(self, ctx:ClusteringParser.Random_stateContext):
        pass


    # Enter a parse tree produced by ClusteringParser#epsilon.
    def enterEpsilon(self, ctx:ClusteringParser.EpsilonContext):
        pass

    # Exit a parse tree produced by ClusteringParser#epsilon.
    def exitEpsilon(self, ctx:ClusteringParser.EpsilonContext):
        pass


    # Enter a parse tree produced by ClusteringParser#min_sample.
    def enterMin_sample(self, ctx:ClusteringParser.Min_sampleContext):
        pass

    # Exit a parse tree produced by ClusteringParser#min_sample.
    def exitMin_sample(self, ctx:ClusteringParser.Min_sampleContext):
        pass


    # Enter a parse tree produced by ClusteringParser#linkage.
    def enterLinkage(self, ctx:ClusteringParser.LinkageContext):
        pass

    # Exit a parse tree produced by ClusteringParser#linkage.
    def exitLinkage(self, ctx:ClusteringParser.LinkageContext):
        pass


    # Enter a parse tree produced by ClusteringParser#affinity.
    def enterAffinity(self, ctx:ClusteringParser.AffinityContext):
        pass

    # Exit a parse tree produced by ClusteringParser#affinity.
    def exitAffinity(self, ctx:ClusteringParser.AffinityContext):
        pass



del ClusteringParser