
from gen.ClusteringListener import ClusteringListener
from Repository.ast import AST
from Repository.make_ast_subtree import make_ast_subtree

class ClusteringCustomListener(ClusteringListener):
    def __init__(self, rule_names):
        self.rule_names = rule_names
        self.ast = AST()

        # We'll keep these rules as explicit nodes
        self.overridden_rules = [
            'setDatasetStmt',
            'methodStmt',
            'clustersStmt',
            'epsStmt',
            'minSamplesStmt',
            'scaleStmt',
            'fitStmt',
            'plotStmt',
            'spectralClustersStmt',
            'clusteringMethod'
        ]

    def exitEveryRule(self, ctx):
        rule_idx = ctx.getRuleIndex()
        rule_name = self.rule_names[rule_idx]
        if rule_name not in self.overridden_rules:
            make_ast_subtree(self.ast, ctx, rule_name)

    def exitSetDatasetStmt(self, ctx):
        make_ast_subtree(self.ast, ctx, "SET_DATASET", keep_node=True)

    def exitMethodStmt(self, ctx):
        make_ast_subtree(self.ast, ctx, "METHOD", keep_node=True)

    def exitClustersStmt(self, ctx):
        make_ast_subtree(self.ast, ctx, "CLUSTERS", keep_node=True)

    def exitEpsStmt(self, ctx):
        make_ast_subtree(self.ast, ctx, "EPS", keep_node=True)

    def exitMinSamplesStmt(self, ctx):
        make_ast_subtree(self.ast, ctx, "MIN_SAMPLES", keep_node=True)

    def exitScaleStmt(self, ctx):
        make_ast_subtree(self.ast, ctx, "SCALE", keep_node=True)

    def exitFitStmt(self, ctx):
        make_ast_subtree(self.ast, ctx, "FIT", keep_node=True)

    def exitPlotStmt(self, ctx):
        make_ast_subtree(self.ast, ctx, "PLOT", keep_node=True)

    def exitSpectralClustersStmt(self, ctx):
        make_ast_subtree(self.ast, ctx, "SPECTRAL_CLUSTERS", keep_node=True)

    def exitClusteringMethod(self, ctx):
        # KMEANS, DBSCAN, AGGLOMERATIVE, SPECTRAL
        make_ast_subtree(self.ast, ctx, ctx.getText(), keep_node=False)
