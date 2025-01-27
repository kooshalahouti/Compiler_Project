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
        4,1,27,105,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        1,0,1,0,1,0,5,0,32,8,0,10,0,12,0,35,9,0,1,0,1,0,3,0,39,8,0,1,0,3,
        0,42,8,0,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,53,8,2,1,3,1,3,
        1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,
        1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,3,10,86,8,
        10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,
        12,1,12,1,12,1,12,1,12,1,12,0,0,13,0,2,4,6,8,10,12,14,16,18,20,22,
        24,0,1,1,0,4,7,101,0,26,1,0,0,0,2,43,1,0,0,0,4,52,1,0,0,0,6,54,1,
        0,0,0,8,58,1,0,0,0,10,62,1,0,0,0,12,66,1,0,0,0,14,70,1,0,0,0,16,
        74,1,0,0,0,18,78,1,0,0,0,20,82,1,0,0,0,22,89,1,0,0,0,24,97,1,0,0,
        0,26,27,3,2,1,0,27,28,5,1,0,0,28,33,3,4,2,0,29,30,5,2,0,0,30,32,
        3,4,2,0,31,29,1,0,0,0,32,35,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,
        34,36,1,0,0,0,35,33,1,0,0,0,36,38,5,3,0,0,37,39,3,20,10,0,38,37,
        1,0,0,0,38,39,1,0,0,0,39,41,1,0,0,0,40,42,3,24,12,0,41,40,1,0,0,
        0,41,42,1,0,0,0,42,1,1,0,0,0,43,44,7,0,0,0,44,3,1,0,0,0,45,53,3,
        6,3,0,46,53,3,8,4,0,47,53,3,10,5,0,48,53,3,12,6,0,49,53,3,14,7,0,
        50,53,3,16,8,0,51,53,3,18,9,0,52,45,1,0,0,0,52,46,1,0,0,0,52,47,
        1,0,0,0,52,48,1,0,0,0,52,49,1,0,0,0,52,50,1,0,0,0,52,51,1,0,0,0,
        53,5,1,0,0,0,54,55,5,8,0,0,55,56,5,9,0,0,56,57,5,23,0,0,57,7,1,0,
        0,0,58,59,5,10,0,0,59,60,5,9,0,0,60,61,5,23,0,0,61,9,1,0,0,0,62,
        63,5,11,0,0,63,64,5,9,0,0,64,65,5,23,0,0,65,11,1,0,0,0,66,67,5,12,
        0,0,67,68,5,9,0,0,68,69,5,24,0,0,69,13,1,0,0,0,70,71,5,13,0,0,71,
        72,5,9,0,0,72,73,5,23,0,0,73,15,1,0,0,0,74,75,5,14,0,0,75,76,5,9,
        0,0,76,77,5,25,0,0,77,17,1,0,0,0,78,79,5,15,0,0,79,80,5,9,0,0,80,
        81,5,26,0,0,81,19,1,0,0,0,82,83,5,16,0,0,83,85,5,1,0,0,84,86,3,22,
        11,0,85,84,1,0,0,0,85,86,1,0,0,0,86,87,1,0,0,0,87,88,5,3,0,0,88,
        21,1,0,0,0,89,90,5,17,0,0,90,91,5,9,0,0,91,92,5,21,0,0,92,93,5,2,
        0,0,93,94,5,18,0,0,94,95,5,9,0,0,95,96,5,21,0,0,96,23,1,0,0,0,97,
        98,5,19,0,0,98,99,5,1,0,0,99,100,5,20,0,0,100,101,5,9,0,0,101,102,
        5,22,0,0,102,103,5,3,0,0,103,25,1,0,0,0,5,33,38,41,52,85
    ]

class ClusteringParser ( Parser ):

    grammarFileName = "Clustering.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'", "'KMeans'", "'DBSCAN'", 
                     "'AgglomerativeClustering'", "'SpectralClustering'", 
                     "'n_clusters'", "'='", "'n_iters'", "'random_state'", 
                     "'epsilon'", "'min_sample'", "'linkage'", "'affinity'", 
                     "'plot'", "'x'", "'y'", "'dataset'", "'file'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "VAR", "STRING", "NUM", "FLOAT", "LINKAGE_TYPE", 
                      "AFFINITY_TYPE", "WS" ]

    RULE_cluster = 0
    RULE_clustering_method = 1
    RULE_args = 2
    RULE_n_clusters = 3
    RULE_n_iters = 4
    RULE_random_state = 5
    RULE_epsilon = 6
    RULE_min_sample = 7
    RULE_linkage = 8
    RULE_affinity = 9
    RULE_plot = 10
    RULE_plot_args = 11
    RULE_dataset = 12

    ruleNames =  [ "cluster", "clustering_method", "args", "n_clusters", 
                   "n_iters", "random_state", "epsilon", "min_sample", "linkage", 
                   "affinity", "plot", "plot_args", "dataset" ]

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
    VAR=21
    STRING=22
    NUM=23
    FLOAT=24
    LINKAGE_TYPE=25
    AFFINITY_TYPE=26
    WS=27

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ClusterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def clustering_method(self):
            return self.getTypedRuleContext(ClusteringParser.Clustering_methodContext,0)


        def args(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ClusteringParser.ArgsContext)
            else:
                return self.getTypedRuleContext(ClusteringParser.ArgsContext,i)


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
        self.enterRule(localctx, 0, self.RULE_cluster)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.clustering_method()
            self.state = 27
            self.match(ClusteringParser.T__0)
            self.state = 28
            self.args()
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 29
                self.match(ClusteringParser.T__1)
                self.state = 30
                self.args()
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 36
            self.match(ClusteringParser.T__2)
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 37
                self.plot()


            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 40
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
        self.enterRule(localctx, 2, self.RULE_clustering_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
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


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def n_clusters(self):
            return self.getTypedRuleContext(ClusteringParser.N_clustersContext,0)


        def n_iters(self):
            return self.getTypedRuleContext(ClusteringParser.N_itersContext,0)


        def random_state(self):
            return self.getTypedRuleContext(ClusteringParser.Random_stateContext,0)


        def epsilon(self):
            return self.getTypedRuleContext(ClusteringParser.EpsilonContext,0)


        def min_sample(self):
            return self.getTypedRuleContext(ClusteringParser.Min_sampleContext,0)


        def linkage(self):
            return self.getTypedRuleContext(ClusteringParser.LinkageContext,0)


        def affinity(self):
            return self.getTypedRuleContext(ClusteringParser.AffinityContext,0)


        def getRuleIndex(self):
            return ClusteringParser.RULE_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgs" ):
                listener.enterArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgs" ):
                listener.exitArgs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs" ):
                return visitor.visitArgs(self)
            else:
                return visitor.visitChildren(self)




    def args(self):

        localctx = ClusteringParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_args)
        try:
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.n_clusters()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.n_iters()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 47
                self.random_state()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 4)
                self.state = 48
                self.epsilon()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 5)
                self.state = 49
                self.min_sample()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 6)
                self.state = 50
                self.linkage()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 7)
                self.state = 51
                self.affinity()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class N_clustersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(ClusteringParser.NUM, 0)

        def getRuleIndex(self):
            return ClusteringParser.RULE_n_clusters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterN_clusters" ):
                listener.enterN_clusters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitN_clusters" ):
                listener.exitN_clusters(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitN_clusters" ):
                return visitor.visitN_clusters(self)
            else:
                return visitor.visitChildren(self)




    def n_clusters(self):

        localctx = ClusteringParser.N_clustersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_n_clusters)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(ClusteringParser.T__7)
            self.state = 55
            self.match(ClusteringParser.T__8)
            self.state = 56
            self.match(ClusteringParser.NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class N_itersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(ClusteringParser.NUM, 0)

        def getRuleIndex(self):
            return ClusteringParser.RULE_n_iters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterN_iters" ):
                listener.enterN_iters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitN_iters" ):
                listener.exitN_iters(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitN_iters" ):
                return visitor.visitN_iters(self)
            else:
                return visitor.visitChildren(self)




    def n_iters(self):

        localctx = ClusteringParser.N_itersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_n_iters)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(ClusteringParser.T__9)
            self.state = 59
            self.match(ClusteringParser.T__8)
            self.state = 60
            self.match(ClusteringParser.NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Random_stateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(ClusteringParser.NUM, 0)

        def getRuleIndex(self):
            return ClusteringParser.RULE_random_state

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRandom_state" ):
                listener.enterRandom_state(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRandom_state" ):
                listener.exitRandom_state(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRandom_state" ):
                return visitor.visitRandom_state(self)
            else:
                return visitor.visitChildren(self)




    def random_state(self):

        localctx = ClusteringParser.Random_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_random_state)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(ClusteringParser.T__10)
            self.state = 63
            self.match(ClusteringParser.T__8)
            self.state = 64
            self.match(ClusteringParser.NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EpsilonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(ClusteringParser.FLOAT, 0)

        def getRuleIndex(self):
            return ClusteringParser.RULE_epsilon

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEpsilon" ):
                listener.enterEpsilon(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEpsilon" ):
                listener.exitEpsilon(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEpsilon" ):
                return visitor.visitEpsilon(self)
            else:
                return visitor.visitChildren(self)




    def epsilon(self):

        localctx = ClusteringParser.EpsilonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_epsilon)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(ClusteringParser.T__11)
            self.state = 67
            self.match(ClusteringParser.T__8)
            self.state = 68
            self.match(ClusteringParser.FLOAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Min_sampleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(ClusteringParser.NUM, 0)

        def getRuleIndex(self):
            return ClusteringParser.RULE_min_sample

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMin_sample" ):
                listener.enterMin_sample(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMin_sample" ):
                listener.exitMin_sample(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMin_sample" ):
                return visitor.visitMin_sample(self)
            else:
                return visitor.visitChildren(self)




    def min_sample(self):

        localctx = ClusteringParser.Min_sampleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_min_sample)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(ClusteringParser.T__12)
            self.state = 71
            self.match(ClusteringParser.T__8)
            self.state = 72
            self.match(ClusteringParser.NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LinkageContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LINKAGE_TYPE(self):
            return self.getToken(ClusteringParser.LINKAGE_TYPE, 0)

        def getRuleIndex(self):
            return ClusteringParser.RULE_linkage

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLinkage" ):
                listener.enterLinkage(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLinkage" ):
                listener.exitLinkage(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLinkage" ):
                return visitor.visitLinkage(self)
            else:
                return visitor.visitChildren(self)




    def linkage(self):

        localctx = ClusteringParser.LinkageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_linkage)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(ClusteringParser.T__13)
            self.state = 75
            self.match(ClusteringParser.T__8)
            self.state = 76
            self.match(ClusteringParser.LINKAGE_TYPE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AffinityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AFFINITY_TYPE(self):
            return self.getToken(ClusteringParser.AFFINITY_TYPE, 0)

        def getRuleIndex(self):
            return ClusteringParser.RULE_affinity

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAffinity" ):
                listener.enterAffinity(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAffinity" ):
                listener.exitAffinity(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAffinity" ):
                return visitor.visitAffinity(self)
            else:
                return visitor.visitChildren(self)




    def affinity(self):

        localctx = ClusteringParser.AffinityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_affinity)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(ClusteringParser.T__14)
            self.state = 79
            self.match(ClusteringParser.T__8)
            self.state = 80
            self.match(ClusteringParser.AFFINITY_TYPE)
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
        self.enterRule(localctx, 20, self.RULE_plot)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(ClusteringParser.T__15)
            self.state = 83
            self.match(ClusteringParser.T__0)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 84
                self.plot_args()


            self.state = 87
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
        self.enterRule(localctx, 22, self.RULE_plot_args)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(ClusteringParser.T__16)
            self.state = 90
            self.match(ClusteringParser.T__8)
            self.state = 91
            self.match(ClusteringParser.VAR)
            self.state = 92
            self.match(ClusteringParser.T__1)
            self.state = 93
            self.match(ClusteringParser.T__17)
            self.state = 94
            self.match(ClusteringParser.T__8)
            self.state = 95
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
        self.enterRule(localctx, 24, self.RULE_dataset)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(ClusteringParser.T__18)
            self.state = 98
            self.match(ClusteringParser.T__0)
            self.state = 99
            self.match(ClusteringParser.T__19)
            self.state = 100
            self.match(ClusteringParser.T__8)
            self.state = 101
            self.match(ClusteringParser.STRING)
            self.state = 102
            self.match(ClusteringParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





