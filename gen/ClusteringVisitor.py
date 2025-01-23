# Generated from F:/university/term 7/compiler/finalproject/Compiler_Project/grammar/Clustering.g4 by ANTLR 4.13.1
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


    # Visit a parse tree produced by ClusteringParser#imports.
    def visitImports(self, ctx:ClusteringParser.ImportsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClusteringParser#loadData.
    def visitLoadData(self, ctx:ClusteringParser.LoadDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClusteringParser#preprocessData.
    def visitPreprocessData(self, ctx:ClusteringParser.PreprocessDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClusteringParser#applyClustering.
    def visitApplyClustering(self, ctx:ClusteringParser.ApplyClusteringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClusteringParser#kmeansClustering.
    def visitKmeansClustering(self, ctx:ClusteringParser.KmeansClusteringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClusteringParser#dbscanClustering.
    def visitDbscanClustering(self, ctx:ClusteringParser.DbscanClusteringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClusteringParser#aggClustering.
    def visitAggClustering(self, ctx:ClusteringParser.AggClusteringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClusteringParser#evaluateResults.
    def visitEvaluateResults(self, ctx:ClusteringParser.EvaluateResultsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ClusteringParser#visualization.
    def visitVisualization(self, ctx:ClusteringParser.VisualizationContext):
        return self.visitChildren(ctx)



del ClusteringParser