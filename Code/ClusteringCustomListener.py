from gen.ClusteringListener import ClusteringListener
from Repository.ast import AST
from Repository.make_ast_subtree import make_ast_subtree

class ClusteringCustomListener(ClusteringListener):
    def __init__(self, rule_names):
        self.rule_names = rule_names
        self.ast = AST()
        self.binary = ["expr"]

        # Rules that need explicit AST nodes
        self.overridden_rules = [
            'assign',
            'clustering_method',
            'expr',
            'plot',
            'dataset'
        ]

    def exitEveryRule(self, ctx):
        rule_idx = ctx.getRuleIndex()
        rule_name = self.rule_names[rule_idx]

        if rule_name not in self.overridden_rules:
            if rule_name in self.binary and ctx.getChildCount() > 1:
                make_ast_subtree(self.ast, ctx, ctx.getChild(1).getText())
            else:
                make_ast_subtree(self.ast, ctx, rule_name)

    def exitCluster(self, ctx):
        make_ast_subtree(self.ast, ctx, "CLUSTER", keep_node=True)

    def exitClustering_method(self, ctx):
        method_name = ctx.getText()
        make_ast_subtree(self.ast, ctx, method_name, keep_node=True)

    def exitAssign(self, ctx):
        left = ctx.getChild(0).getText()
        right = ctx.getChild(2).getText()

        make_ast_subtree(self.ast, ctx, "=", keep_node=True)
        make_ast_subtree(self.ast, ctx.getChild(0), left, keep_node=True)
        make_ast_subtree(self.ast, ctx.getChild(2), right, keep_node=True)

    def exitExpr(self, ctx):
        expr_value = ctx.getText()
        make_ast_subtree(self.ast, ctx, expr_value, keep_node=True)

    def exitPlot(self, ctx):
        make_ast_subtree(self.ast, ctx, "PLOT", keep_node=True)

    def exitPlot_args(self, ctx):
        x_var = ctx.getChild(2).getText()
        y_var = ctx.getChild(6).getText()
        plot_args = f"X={x_var}, Y={y_var}"
        make_ast_subtree(self.ast, ctx, plot_args, keep_node=True)

    def exitDataset(self, ctx):
        file_name = ctx.getChild(4).getText()
        make_ast_subtree(self.ast, ctx, f"DATASET: {file_name}", keep_node=True)

    def exitNum(self, ctx):
        num_value = ctx.getText()
        make_ast_subtree(self.ast, ctx, num_value, keep_node=True)

    def exitString(self, ctx):
        string_value = ctx.getText()
        make_ast_subtree(self.ast, ctx, string_value, keep_node=True)

    def exitLinkage_type(self, ctx):
        linkage_type = ctx.getText()
        make_ast_subtree(self.ast, ctx, f"LINKAGE: {linkage_type}", keep_node=True)

    def exitAffinity_type(self, ctx):
        affinity_type = ctx.getText()
        make_ast_subtree(self.ast, ctx, f"AFFINITY: {affinity_type}", keep_node=True)

    def exitProgram(self, ctx):
        pass

    def exitVar(self, ctx):
        pass

    def exitFloat(self, ctx):
        pass

    def exitWs(self, ctx):
        pass