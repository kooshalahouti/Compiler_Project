# Generated from F:/university/term 7/compiler/finalproject/Compiler_Project/grammar/Clustering.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,28,81,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,
        1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,
        5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,
        7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,0,0,10,0,2,4,6,8,10,12,14,16,18,0,0,70,0,20,1,0,0,
        0,2,28,1,0,0,0,4,34,1,0,0,0,6,38,1,0,0,0,8,41,1,0,0,0,10,45,1,0,
        0,0,12,50,1,0,0,0,14,57,1,0,0,0,16,62,1,0,0,0,18,72,1,0,0,0,20,21,
        3,2,1,0,21,22,3,4,2,0,22,23,3,6,3,0,23,24,3,8,4,0,24,25,3,16,8,0,
        25,26,3,18,9,0,26,27,5,0,0,1,27,1,1,0,0,0,28,29,5,1,0,0,29,30,5,
        2,0,0,30,31,5,3,0,0,31,32,5,4,0,0,32,33,5,5,0,0,33,3,1,0,0,0,34,
        35,5,6,0,0,35,36,5,25,0,0,36,37,5,7,0,0,37,5,1,0,0,0,38,39,5,8,0,
        0,39,40,5,9,0,0,40,7,1,0,0,0,41,42,3,10,5,0,42,43,3,12,6,0,43,44,
        3,14,7,0,44,9,1,0,0,0,45,46,5,10,0,0,46,47,5,26,0,0,47,48,5,11,0,
        0,48,49,5,12,0,0,49,11,1,0,0,0,50,51,5,13,0,0,51,52,5,27,0,0,52,
        53,5,14,0,0,53,54,5,26,0,0,54,55,5,7,0,0,55,56,5,15,0,0,56,13,1,
        0,0,0,57,58,5,16,0,0,58,59,5,26,0,0,59,60,5,7,0,0,60,61,5,17,0,0,
        61,15,1,0,0,0,62,63,5,18,0,0,63,64,5,25,0,0,64,65,5,19,0,0,65,66,
        5,18,0,0,66,67,5,25,0,0,67,68,5,20,0,0,68,69,5,18,0,0,69,70,5,25,
        0,0,70,71,5,21,0,0,71,17,1,0,0,0,72,73,5,22,0,0,73,74,5,25,0,0,74,
        75,5,7,0,0,75,76,5,23,0,0,76,77,5,25,0,0,77,78,5,7,0,0,78,79,5,24,
        0,0,79,19,1,0,0,0,0
    ]

class ClusteringParser ( Parser ):

    grammarFileName = "Clustering.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'import numpy as np'", "'import pandas as pd'", 
                     "'from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering'", 
                     "'from sklearn.preprocessing import StandardScaler'", 
                     "'import matplotlib.pyplot as plt'", "'data = pd.read_csv('", 
                     "')'", "'scaler = StandardScaler()'", "'data_scaled = scaler.fit_transform(data)'", 
                     "'kmeans = KMeans(n_clusters='", "', random_state=42)'", 
                     "'kmeans_labels = kmeans.fit_predict(data_scaled)'", 
                     "'dbscan = DBSCAN(eps='", "', min_samples='", "'dbscan_labels = dbscan.fit_predict(data_scaled)'", 
                     "'agglo = AgglomerativeClustering(n_clusters='", "'agglo_labels = agglo.fit_predict(data_scaled)'", 
                     "'print('", "', np.unique(kmeans_labels))'", "', np.unique(dbscan_labels))'", 
                     "', np.unique(agglo_labels))'", "'plt.scatter(data_scaled[:, 0], data_scaled[:, 1], c=kmeans_labels, cmap='", 
                     "'plt.title('", "'plt.show()'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "STRING_LITERAL", "NUMBER_LITERAL", "FLOAT_LITERAL", 
                      "WS" ]

    RULE_program = 0
    RULE_imports = 1
    RULE_loadData = 2
    RULE_preprocessData = 3
    RULE_applyClustering = 4
    RULE_kmeansClustering = 5
    RULE_dbscanClustering = 6
    RULE_aggClustering = 7
    RULE_evaluateResults = 8
    RULE_visualization = 9

    ruleNames =  [ "program", "imports", "loadData", "preprocessData", "applyClustering", 
                   "kmeansClustering", "dbscanClustering", "aggClustering", 
                   "evaluateResults", "visualization" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    STRING_LITERAL=25
    NUMBER_LITERAL=26
    FLOAT_LITERAL=27
    WS=28

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def imports(self):
            return self.getTypedRuleContext(ClusteringParser.ImportsContext,0)


        def loadData(self):
            return self.getTypedRuleContext(ClusteringParser.LoadDataContext,0)


        def preprocessData(self):
            return self.getTypedRuleContext(ClusteringParser.PreprocessDataContext,0)


        def applyClustering(self):
            return self.getTypedRuleContext(ClusteringParser.ApplyClusteringContext,0)


        def evaluateResults(self):
            return self.getTypedRuleContext(ClusteringParser.EvaluateResultsContext,0)


        def visualization(self):
            return self.getTypedRuleContext(ClusteringParser.VisualizationContext,0)


        def EOF(self):
            return self.getToken(ClusteringParser.EOF, 0)

        def getRuleIndex(self):
            return ClusteringParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ClusteringParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.imports()
            self.state = 21
            self.loadData()
            self.state = 22
            self.preprocessData()
            self.state = 23
            self.applyClustering()
            self.state = 24
            self.evaluateResults()
            self.state = 25
            self.visualization()
            self.state = 26
            self.match(ClusteringParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ClusteringParser.RULE_imports

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImports" ):
                listener.enterImports(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImports" ):
                listener.exitImports(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImports" ):
                return visitor.visitImports(self)
            else:
                return visitor.visitChildren(self)




    def imports(self):

        localctx = ClusteringParser.ImportsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_imports)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(ClusteringParser.T__0)
            self.state = 29
            self.match(ClusteringParser.T__1)
            self.state = 30
            self.match(ClusteringParser.T__2)
            self.state = 31
            self.match(ClusteringParser.T__3)
            self.state = 32
            self.match(ClusteringParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoadDataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_LITERAL(self):
            return self.getToken(ClusteringParser.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return ClusteringParser.RULE_loadData

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoadData" ):
                listener.enterLoadData(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoadData" ):
                listener.exitLoadData(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoadData" ):
                return visitor.visitLoadData(self)
            else:
                return visitor.visitChildren(self)




    def loadData(self):

        localctx = ClusteringParser.LoadDataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_loadData)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(ClusteringParser.T__5)
            self.state = 35
            self.match(ClusteringParser.STRING_LITERAL)
            self.state = 36
            self.match(ClusteringParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PreprocessDataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ClusteringParser.RULE_preprocessData

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreprocessData" ):
                listener.enterPreprocessData(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreprocessData" ):
                listener.exitPreprocessData(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreprocessData" ):
                return visitor.visitPreprocessData(self)
            else:
                return visitor.visitChildren(self)




    def preprocessData(self):

        localctx = ClusteringParser.PreprocessDataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_preprocessData)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(ClusteringParser.T__7)
            self.state = 39
            self.match(ClusteringParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ApplyClusteringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def kmeansClustering(self):
            return self.getTypedRuleContext(ClusteringParser.KmeansClusteringContext,0)


        def dbscanClustering(self):
            return self.getTypedRuleContext(ClusteringParser.DbscanClusteringContext,0)


        def aggClustering(self):
            return self.getTypedRuleContext(ClusteringParser.AggClusteringContext,0)


        def getRuleIndex(self):
            return ClusteringParser.RULE_applyClustering

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterApplyClustering" ):
                listener.enterApplyClustering(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitApplyClustering" ):
                listener.exitApplyClustering(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitApplyClustering" ):
                return visitor.visitApplyClustering(self)
            else:
                return visitor.visitChildren(self)




    def applyClustering(self):

        localctx = ClusteringParser.ApplyClusteringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_applyClustering)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.kmeansClustering()
            self.state = 42
            self.dbscanClustering()
            self.state = 43
            self.aggClustering()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KmeansClusteringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_LITERAL(self):
            return self.getToken(ClusteringParser.NUMBER_LITERAL, 0)

        def getRuleIndex(self):
            return ClusteringParser.RULE_kmeansClustering

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKmeansClustering" ):
                listener.enterKmeansClustering(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKmeansClustering" ):
                listener.exitKmeansClustering(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKmeansClustering" ):
                return visitor.visitKmeansClustering(self)
            else:
                return visitor.visitChildren(self)




    def kmeansClustering(self):

        localctx = ClusteringParser.KmeansClusteringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_kmeansClustering)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(ClusteringParser.T__9)
            self.state = 46
            self.match(ClusteringParser.NUMBER_LITERAL)
            self.state = 47
            self.match(ClusteringParser.T__10)
            self.state = 48
            self.match(ClusteringParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DbscanClusteringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT_LITERAL(self):
            return self.getToken(ClusteringParser.FLOAT_LITERAL, 0)

        def NUMBER_LITERAL(self):
            return self.getToken(ClusteringParser.NUMBER_LITERAL, 0)

        def getRuleIndex(self):
            return ClusteringParser.RULE_dbscanClustering

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDbscanClustering" ):
                listener.enterDbscanClustering(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDbscanClustering" ):
                listener.exitDbscanClustering(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDbscanClustering" ):
                return visitor.visitDbscanClustering(self)
            else:
                return visitor.visitChildren(self)




    def dbscanClustering(self):

        localctx = ClusteringParser.DbscanClusteringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_dbscanClustering)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(ClusteringParser.T__12)
            self.state = 51
            self.match(ClusteringParser.FLOAT_LITERAL)
            self.state = 52
            self.match(ClusteringParser.T__13)
            self.state = 53
            self.match(ClusteringParser.NUMBER_LITERAL)
            self.state = 54
            self.match(ClusteringParser.T__6)
            self.state = 55
            self.match(ClusteringParser.T__14)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AggClusteringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_LITERAL(self):
            return self.getToken(ClusteringParser.NUMBER_LITERAL, 0)

        def getRuleIndex(self):
            return ClusteringParser.RULE_aggClustering

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggClustering" ):
                listener.enterAggClustering(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggClustering" ):
                listener.exitAggClustering(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggClustering" ):
                return visitor.visitAggClustering(self)
            else:
                return visitor.visitChildren(self)




    def aggClustering(self):

        localctx = ClusteringParser.AggClusteringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_aggClustering)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(ClusteringParser.T__15)
            self.state = 58
            self.match(ClusteringParser.NUMBER_LITERAL)
            self.state = 59
            self.match(ClusteringParser.T__6)
            self.state = 60
            self.match(ClusteringParser.T__16)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EvaluateResultsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(ClusteringParser.STRING_LITERAL)
            else:
                return self.getToken(ClusteringParser.STRING_LITERAL, i)

        def getRuleIndex(self):
            return ClusteringParser.RULE_evaluateResults

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEvaluateResults" ):
                listener.enterEvaluateResults(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEvaluateResults" ):
                listener.exitEvaluateResults(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEvaluateResults" ):
                return visitor.visitEvaluateResults(self)
            else:
                return visitor.visitChildren(self)




    def evaluateResults(self):

        localctx = ClusteringParser.EvaluateResultsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_evaluateResults)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(ClusteringParser.T__17)
            self.state = 63
            self.match(ClusteringParser.STRING_LITERAL)
            self.state = 64
            self.match(ClusteringParser.T__18)
            self.state = 65
            self.match(ClusteringParser.T__17)
            self.state = 66
            self.match(ClusteringParser.STRING_LITERAL)
            self.state = 67
            self.match(ClusteringParser.T__19)
            self.state = 68
            self.match(ClusteringParser.T__17)
            self.state = 69
            self.match(ClusteringParser.STRING_LITERAL)
            self.state = 70
            self.match(ClusteringParser.T__20)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VisualizationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(ClusteringParser.STRING_LITERAL)
            else:
                return self.getToken(ClusteringParser.STRING_LITERAL, i)

        def getRuleIndex(self):
            return ClusteringParser.RULE_visualization

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVisualization" ):
                listener.enterVisualization(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVisualization" ):
                listener.exitVisualization(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVisualization" ):
                return visitor.visitVisualization(self)
            else:
                return visitor.visitChildren(self)




    def visualization(self):

        localctx = ClusteringParser.VisualizationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_visualization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(ClusteringParser.T__21)
            self.state = 73
            self.match(ClusteringParser.STRING_LITERAL)
            self.state = 74
            self.match(ClusteringParser.T__6)
            self.state = 75
            self.match(ClusteringParser.T__22)
            self.state = 76
            self.match(ClusteringParser.STRING_LITERAL)
            self.state = 77
            self.match(ClusteringParser.T__6)
            self.state = 78
            self.match(ClusteringParser.T__23)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





