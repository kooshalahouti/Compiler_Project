# Generated from D:/uni/Compiler/finalProject/pythonProject/grammar/Clustering.g4 by ANTLR 4.13.1
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
        4,1,20,66,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,1,1,1,1,1,1,1,1,1,5,1,24,8,1,10,1,12,1,27,9,
        1,1,1,1,1,3,1,31,8,1,1,1,3,1,34,8,1,1,2,1,2,1,3,1,3,1,3,1,3,1,4,
        1,4,1,5,1,5,1,5,3,5,47,8,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,0,0,8,0,2,4,6,8,10,12,14,0,2,1,
        0,4,7,2,0,14,14,16,19,61,0,16,1,0,0,0,2,18,1,0,0,0,4,35,1,0,0,0,
        6,37,1,0,0,0,8,41,1,0,0,0,10,43,1,0,0,0,12,50,1,0,0,0,14,58,1,0,
        0,0,16,17,3,2,1,0,17,1,1,0,0,0,18,19,3,4,2,0,19,20,5,1,0,0,20,25,
        3,6,3,0,21,22,5,2,0,0,22,24,3,6,3,0,23,21,1,0,0,0,24,27,1,0,0,0,
        25,23,1,0,0,0,25,26,1,0,0,0,26,28,1,0,0,0,27,25,1,0,0,0,28,30,5,
        3,0,0,29,31,3,10,5,0,30,29,1,0,0,0,30,31,1,0,0,0,31,33,1,0,0,0,32,
        34,3,14,7,0,33,32,1,0,0,0,33,34,1,0,0,0,34,3,1,0,0,0,35,36,7,0,0,
        0,36,5,1,0,0,0,37,38,5,16,0,0,38,39,5,8,0,0,39,40,3,8,4,0,40,7,1,
        0,0,0,41,42,7,1,0,0,42,9,1,0,0,0,43,44,5,9,0,0,44,46,5,1,0,0,45,
        47,3,12,6,0,46,45,1,0,0,0,46,47,1,0,0,0,47,48,1,0,0,0,48,49,5,3,
        0,0,49,11,1,0,0,0,50,51,5,10,0,0,51,52,5,8,0,0,52,53,5,16,0,0,53,
        54,5,2,0,0,54,55,5,11,0,0,55,56,5,8,0,0,56,57,5,16,0,0,57,13,1,0,
        0,0,58,59,5,12,0,0,59,60,5,1,0,0,60,61,5,13,0,0,61,62,5,8,0,0,62,
        63,5,17,0,0,63,64,5,3,0,0,64,15,1,0,0,0,4,25,30,33,46
    ]

class ClusteringParser ( Parser ):

    grammarFileName = "Clustering.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'", "'KMeans'", "'DBSCAN'", 
                     "'AgglomerativeClustering'", "'SpectralClustering'", 
                     "'='", "'plot'", "'x'", "'y'", "'dataset'", "'file'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NUM", "FLOAT", "VAR", "STRING", 
                      "LINKAGE_TYPE", "AFFINITY_TYPE", "WS" ]

    RULE_program = 0
    RULE_cluster = 1
    RULE_clustering_method = 2
    RULE_assign = 3
    RULE_expr = 4
    RULE_plot = 5
    RULE_plot_args = 6
    RULE_dataset = 7

    ruleNames =  [ "program", "cluster", "clustering_method", "assign", 
                   "expr", "plot", "plot_args", "dataset" ]

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
    NUM=14
    FLOAT=15
    VAR=16
    STRING=17
    LINKAGE_TYPE=18
    AFFINITY_TYPE=19
    WS=20

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

        def cluster(self):
            return self.getTypedRuleContext(ClusteringParser.ClusterContext,0)


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
            self.state = 16
            self.cluster()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClusterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def clustering_method(self):
            return self.getTypedRuleContext(ClusteringParser.Clustering_methodContext,0)


        def assign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ClusteringParser.AssignContext)
            else:
                return self.getTypedRuleContext(ClusteringParser.AssignContext,i)


        def plot(self):
            return self.getTypedRuleContext(ClusteringParser.PlotContext,0)


        def dataset(self):
            return self.getTypedRuleContext(ClusteringParser.DatasetContext,0)


        def getRuleIndex(self):
            return ClusteringParser.RULE_cluster

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCluster" ):
                listener.enterCluster(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCluster" ):
                listener.exitCluster(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCluster" ):
                return visitor.visitCluster(self)
            else:
                return visitor.visitChildren(self)




    def cluster(self):

        localctx = ClusteringParser.ClusterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_cluster)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.clustering_method()
            self.state = 19
            self.match(ClusteringParser.T__0)
            self.state = 20
            self.assign()
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 21
                self.match(ClusteringParser.T__1)
                self.state = 22
                self.assign()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 28
            self.match(ClusteringParser.T__2)
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 29
                self.plot()


            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 32
                self.dataset()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Clustering_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ClusteringParser.RULE_clustering_method

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClustering_method" ):
                listener.enterClustering_method(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClustering_method" ):
                listener.exitClustering_method(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClustering_method" ):
                return visitor.visitClustering_method(self)
            else:
                return visitor.visitChildren(self)




    def clustering_method(self):

        localctx = ClusteringParser.Clustering_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_clustering_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 240) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ClusteringParser.VAR, 0)

        def expr(self):
            return self.getTypedRuleContext(ClusteringParser.ExprContext,0)


        def getRuleIndex(self):
            return ClusteringParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = ClusteringParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(ClusteringParser.VAR)
            self.state = 38
            self.match(ClusteringParser.T__7)
            self.state = 39
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(ClusteringParser.NUM, 0)

        def STRING(self):
            return self.getToken(ClusteringParser.STRING, 0)

        def LINKAGE_TYPE(self):
            return self.getToken(ClusteringParser.LINKAGE_TYPE, 0)

        def AFFINITY_TYPE(self):
            return self.getToken(ClusteringParser.AFFINITY_TYPE, 0)

        def VAR(self):
            return self.getToken(ClusteringParser.VAR, 0)

        def getRuleIndex(self):
            return ClusteringParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ClusteringParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 999424) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PlotContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def plot_args(self):
            return self.getTypedRuleContext(ClusteringParser.Plot_argsContext,0)


        def getRuleIndex(self):
            return ClusteringParser.RULE_plot

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlot" ):
                listener.enterPlot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlot" ):
                listener.exitPlot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlot" ):
                return visitor.visitPlot(self)
            else:
                return visitor.visitChildren(self)




    def plot(self):

        localctx = ClusteringParser.PlotContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_plot)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(ClusteringParser.T__8)
            self.state = 44
            self.match(ClusteringParser.T__0)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 45
                self.plot_args()


            self.state = 48
            self.match(ClusteringParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Plot_argsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self, i:int=None):
            if i is None:
                return self.getTokens(ClusteringParser.VAR)
            else:
                return self.getToken(ClusteringParser.VAR, i)

        def getRuleIndex(self):
            return ClusteringParser.RULE_plot_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlot_args" ):
                listener.enterPlot_args(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlot_args" ):
                listener.exitPlot_args(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlot_args" ):
                return visitor.visitPlot_args(self)
            else:
                return visitor.visitChildren(self)




    def plot_args(self):

        localctx = ClusteringParser.Plot_argsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_plot_args)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(ClusteringParser.T__9)
            self.state = 51
            self.match(ClusteringParser.T__7)
            self.state = 52
            self.match(ClusteringParser.VAR)
            self.state = 53
            self.match(ClusteringParser.T__1)
            self.state = 54
            self.match(ClusteringParser.T__10)
            self.state = 55
            self.match(ClusteringParser.T__7)
            self.state = 56
            self.match(ClusteringParser.VAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DatasetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(ClusteringParser.STRING, 0)

        def getRuleIndex(self):
            return ClusteringParser.RULE_dataset

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDataset" ):
                listener.enterDataset(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDataset" ):
                listener.exitDataset(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDataset" ):
                return visitor.visitDataset(self)
            else:
                return visitor.visitChildren(self)




    def dataset(self):

        localctx = ClusteringParser.DatasetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_dataset)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(ClusteringParser.T__11)
            self.state = 59
            self.match(ClusteringParser.T__0)
            self.state = 60
            self.match(ClusteringParser.T__12)
            self.state = 61
            self.match(ClusteringParser.T__7)
            self.state = 62
            self.match(ClusteringParser.STRING)
            self.state = 63
            self.match(ClusteringParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





