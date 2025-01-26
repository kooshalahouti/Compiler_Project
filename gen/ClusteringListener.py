# Generated from D:/uni/Compiler/finalProject/pythonProject/grammar/Clustering.g4 by ANTLR 4.13.1
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


    # Enter a parse tree produced by ClusteringParser#assign.
    def enterAssign(self, ctx:ClusteringParser.AssignContext):
        pass

    # Exit a parse tree produced by ClusteringParser#assign.
    def exitAssign(self, ctx:ClusteringParser.AssignContext):
        pass


    # Enter a parse tree produced by ClusteringParser#expr.
    def enterExpr(self, ctx:ClusteringParser.ExprContext):
        pass

    # Exit a parse tree produced by ClusteringParser#expr.
    def exitExpr(self, ctx:ClusteringParser.ExprContext):
        pass


    # Enter a parse tree produced by ClusteringParser#plot.
    def enterPlot(self, ctx:ClusteringParser.PlotContext):
        pass

    # Exit a parse tree produced by ClusteringParser#plot.
    def exitPlot(self, ctx:ClusteringParser.PlotContext):
        pass


    # Enter a parse tree produced by ClusteringParser#plot_args.
    def enterPlot_args(self, ctx:ClusteringParser.Plot_argsContext):
        pass

    # Exit a parse tree produced by ClusteringParser#plot_args.
    def exitPlot_args(self, ctx:ClusteringParser.Plot_argsContext):
        pass


    # Enter a parse tree produced by ClusteringParser#dataset.
    def enterDataset(self, ctx:ClusteringParser.DatasetContext):
        pass

    # Exit a parse tree produced by ClusteringParser#dataset.
    def exitDataset(self, ctx:ClusteringParser.DatasetContext):
        pass



del ClusteringParser