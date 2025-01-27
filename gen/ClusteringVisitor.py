# Generated from D:/uni/Compiler/finalProject/pythonProject/grammar/Clustering.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ClusteringParser import ClusteringParser
else:
    from ClusteringParser import ClusteringParser

# This class defines a complete generic visitor for a parse tree produced by ClusteringParser.

class ClusteringVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ClusteringParser#cluster.
    def visitCluster(self, ctx:ClusteringParser.ClusterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClusteringParser#clustering_method.
    def visitClustering_method(self, ctx:ClusteringParser.Clustering_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClusteringParser#args.
    def visitArgs(self, ctx:ClusteringParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClusteringParser#n_clusters.
    def visitN_clusters(self, ctx:ClusteringParser.N_clustersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClusteringParser#n_iters.
    def visitN_iters(self, ctx:ClusteringParser.N_itersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClusteringParser#random_state.
    def visitRandom_state(self, ctx:ClusteringParser.Random_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClusteringParser#epsilon.
    def visitEpsilon(self, ctx:ClusteringParser.EpsilonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClusteringParser#min_sample.
    def visitMin_sample(self, ctx:ClusteringParser.Min_sampleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClusteringParser#linkage.
    def visitLinkage(self, ctx:ClusteringParser.LinkageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClusteringParser#affinity.
    def visitAffinity(self, ctx:ClusteringParser.AffinityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClusteringParser#plot.
    def visitPlot(self, ctx:ClusteringParser.PlotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClusteringParser#plot_args.
    def visitPlot_args(self, ctx:ClusteringParser.Plot_argsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClusteringParser#dataset.
    def visitDataset(self, ctx:ClusteringParser.DatasetContext):
        return self.visitChildren(ctx)



del ClusteringParser