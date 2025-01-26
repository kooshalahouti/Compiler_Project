# Generated from D:/uni/Compiler/finalProject/pythonProject/grammar/Clustering.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ClusteringParser import ClusteringParser
else:
    from ClusteringParser import ClusteringParser

# This class defines a complete generic visitor for a parse tree produced by ClusteringParser.

class ClusteringVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ClusteringParser#program.
    def visitProgram(self, ctx:ClusteringParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClusteringParser#cluster.
    def visitCluster(self, ctx:ClusteringParser.ClusterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClusteringParser#clustering_method.
    def visitClustering_method(self, ctx:ClusteringParser.Clustering_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClusteringParser#assign.
    def visitAssign(self, ctx:ClusteringParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClusteringParser#expr.
    def visitExpr(self, ctx:ClusteringParser.ExprContext):
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