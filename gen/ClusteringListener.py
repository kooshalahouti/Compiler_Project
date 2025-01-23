# Generated from F:/university/term 7/compiler/finalproject/Compiler_Project/grammar/Clustering.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ClusteringParser import ClusteringParser
else:
    from ClusteringParser import ClusteringParser

# This class defines a complete listener for a parse tree produced by ClusteringParser.
class ClusteringListener(ParseTreeListener):

    # Enter a parse tree produced by ClusteringParser#program.
    def enterProgram(self, ctx:ClusteringParser.ProgramContext):
        pass

    # Exit a parse tree produced by ClusteringParser#program.
    def exitProgram(self, ctx:ClusteringParser.ProgramContext):
        pass


    # Enter a parse tree produced by ClusteringParser#imports.
    def enterImports(self, ctx:ClusteringParser.ImportsContext):
        pass

    # Exit a parse tree produced by ClusteringParser#imports.
    def exitImports(self, ctx:ClusteringParser.ImportsContext):
        pass


    # Enter a parse tree produced by ClusteringParser#loadData.
    def enterLoadData(self, ctx:ClusteringParser.LoadDataContext):
        pass

    # Exit a parse tree produced by ClusteringParser#loadData.
    def exitLoadData(self, ctx:ClusteringParser.LoadDataContext):
        pass


    # Enter a parse tree produced by ClusteringParser#preprocessData.
    def enterPreprocessData(self, ctx:ClusteringParser.PreprocessDataContext):
        pass

    # Exit a parse tree produced by ClusteringParser#preprocessData.
    def exitPreprocessData(self, ctx:ClusteringParser.PreprocessDataContext):
        pass


    # Enter a parse tree produced by ClusteringParser#applyClustering.
    def enterApplyClustering(self, ctx:ClusteringParser.ApplyClusteringContext):
        pass

    # Exit a parse tree produced by ClusteringParser#applyClustering.
    def exitApplyClustering(self, ctx:ClusteringParser.ApplyClusteringContext):
        pass


    # Enter a parse tree produced by ClusteringParser#kmeansClustering.
    def enterKmeansClustering(self, ctx:ClusteringParser.KmeansClusteringContext):
        pass

    # Exit a parse tree produced by ClusteringParser#kmeansClustering.
    def exitKmeansClustering(self, ctx:ClusteringParser.KmeansClusteringContext):
        pass


    # Enter a parse tree produced by ClusteringParser#dbscanClustering.
    def enterDbscanClustering(self, ctx:ClusteringParser.DbscanClusteringContext):
        pass

    # Exit a parse tree produced by ClusteringParser#dbscanClustering.
    def exitDbscanClustering(self, ctx:ClusteringParser.DbscanClusteringContext):
        pass


    # Enter a parse tree produced by ClusteringParser#aggClustering.
    def enterAggClustering(self, ctx:ClusteringParser.AggClusteringContext):
        pass

    # Exit a parse tree produced by ClusteringParser#aggClustering.
    def exitAggClustering(self, ctx:ClusteringParser.AggClusteringContext):
        pass


    # Enter a parse tree produced by ClusteringParser#evaluateResults.
    def enterEvaluateResults(self, ctx:ClusteringParser.EvaluateResultsContext):
        pass

    # Exit a parse tree produced by ClusteringParser#evaluateResults.
    def exitEvaluateResults(self, ctx:ClusteringParser.EvaluateResultsContext):
        pass


    # Enter a parse tree produced by ClusteringParser#visualization.
    def enterVisualization(self, ctx:ClusteringParser.VisualizationContext):
        pass

    # Exit a parse tree produced by ClusteringParser#visualization.
    def exitVisualization(self, ctx:ClusteringParser.VisualizationContext):
        pass



del ClusteringParser