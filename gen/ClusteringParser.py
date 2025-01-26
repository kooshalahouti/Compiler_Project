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
        4,1,20,72,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,1,0,1,0,5,0,26,8,0,10,0,12,
        0,29,9,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,42,8,2,
        1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,
        1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,0,0,10,0,2,4,
        6,8,10,12,14,16,18,0,1,1,0,4,7,68,0,20,1,0,0,0,2,32,1,0,0,0,4,41,
        1,0,0,0,6,43,1,0,0,0,8,47,1,0,0,0,10,51,1,0,0,0,12,55,1,0,0,0,14,
        59,1,0,0,0,16,63,1,0,0,0,18,67,1,0,0,0,20,21,3,2,1,0,21,22,5,1,0,
        0,22,27,3,4,2,0,23,24,5,2,0,0,24,26,3,4,2,0,25,23,1,0,0,0,26,29,
        1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,30,1,0,0,0,29,27,1,0,0,0,
        30,31,5,3,0,0,31,1,1,0,0,0,32,33,7,0,0,0,33,3,1,0,0,0,34,42,3,6,
        3,0,35,42,3,8,4,0,36,42,3,10,5,0,37,42,3,12,6,0,38,42,3,14,7,0,39,
        42,3,16,8,0,40,42,3,18,9,0,41,34,1,0,0,0,41,35,1,0,0,0,41,36,1,0,
        0,0,41,37,1,0,0,0,41,38,1,0,0,0,41,39,1,0,0,0,41,40,1,0,0,0,42,5,
        1,0,0,0,43,44,5,8,0,0,44,45,5,9,0,0,45,46,5,16,0,0,46,7,1,0,0,0,
        47,48,5,10,0,0,48,49,5,9,0,0,49,50,5,16,0,0,50,9,1,0,0,0,51,52,5,
        11,0,0,52,53,5,9,0,0,53,54,5,16,0,0,54,11,1,0,0,0,55,56,5,12,0,0,
        56,57,5,9,0,0,57,58,5,17,0,0,58,13,1,0,0,0,59,60,5,13,0,0,60,61,
        5,9,0,0,61,62,5,16,0,0,62,15,1,0,0,0,63,64,5,14,0,0,64,65,5,9,0,
        0,65,66,5,18,0,0,66,17,1,0,0,0,67,68,5,15,0,0,68,69,5,9,0,0,69,70,
        5,19,0,0,70,19,1,0,0,0,2,27,41
    ]

class ClusteringParser ( Parser ):

    grammarFileName = "Clustering.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "','", "')'", "'KMeans'", "'DBSCAN'", 
                     "'AgglomerativeClustering'", "'SpectralClustering'", 
                     "'n_clusters'", "'='", "'n_iters'", "'random_state'", 
                     "'epsilon'", "'min_sample'", "'linkage'", "'affinity'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NUM", "FLOAT", "LINKAGE_TYPE", "AFFINITY_TYPE", "WS" ]

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

    ruleNames =  [ "cluster", "clustering_method", "args", "n_clusters", 
                   "n_iters", "random_state", "epsilon", "min_sample", "linkage", 
                   "affinity" ]

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
    NUM=16
    FLOAT=17
    LINKAGE_TYPE=18
    AFFINITY_TYPE=19
    WS=20

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
            self.state = 20
            self.clustering_method()
            self.state = 21
            self.match(ClusteringParser.T__0)
            self.state = 22
            self.args()
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 23
                self.match(ClusteringParser.T__1)
                self.state = 24
                self.args()
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 30
            self.match(ClusteringParser.T__2)
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
            self.state = 32
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
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.n_clusters()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.n_iters()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 36
                self.random_state()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 4)
                self.state = 37
                self.epsilon()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 5)
                self.state = 38
                self.min_sample()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 6)
                self.state = 39
                self.linkage()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 7)
                self.state = 40
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
            self.state = 43
            self.match(ClusteringParser.T__7)
            self.state = 44
            self.match(ClusteringParser.T__8)
            self.state = 45
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
            self.state = 47
            self.match(ClusteringParser.T__9)
            self.state = 48
            self.match(ClusteringParser.T__8)
            self.state = 49
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
            self.state = 51
            self.match(ClusteringParser.T__10)
            self.state = 52
            self.match(ClusteringParser.T__8)
            self.state = 53
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
            self.state = 55
            self.match(ClusteringParser.T__11)
            self.state = 56
            self.match(ClusteringParser.T__8)
            self.state = 57
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
            self.state = 59
            self.match(ClusteringParser.T__12)
            self.state = 60
            self.match(ClusteringParser.T__8)
            self.state = 61
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
            self.state = 63
            self.match(ClusteringParser.T__13)
            self.state = 64
            self.match(ClusteringParser.T__8)
            self.state = 65
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
            self.state = 67
            self.match(ClusteringParser.T__14)
            self.state = 68
            self.match(ClusteringParser.T__8)
            self.state = 69
            self.match(ClusteringParser.AFFINITY_TYPE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





