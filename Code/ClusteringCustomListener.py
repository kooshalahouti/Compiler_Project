from gen.ClusteringListener import ClusteringListener
from Repository.ast import AST
from Repository.make_ast_subtree import make_ast_subtree
from gen.ClusteringParser import ClusteringParser

class ClusteringCustomListener(ClusteringListener):
    def __init__(self, rule_names):
        self.rule_names = rule_names
        self.ast = AST()
        self.overridden_rules = [
            'assign',
            'clustering_method',
            'expr',
            'plot',
            'dataset',
            'num',
            'string',
            'VAR',
            'linkage_type',
            'affinity_type',
            'n_clusters',
            'n_iters',
            'random_state',
            'epsilon',
            'min_sample',
            'linkage',
            'affinity',
        ]

    def exitEveryRule(self, ctx):
        rule_idx = ctx.getRuleIndex()
        rule_name = self.rule_names[rule_idx]
        print(f"Processing rule: {rule_name}, ctx: {ctx.getText()}")

        if rule_name in self.overridden_rules:
            if ctx.getChildCount() > 1:
                length = ctx.getChildCount() - 1
                for i in range(0, length, 2):
                    if ctx.getChild(i + 1).getText() == '=':
                        key = ctx.getChild(i).getText()
                        value = ctx.getChild(i + 2).getText()

                        if not hasattr(ctx, "has_assign_node"):
                            assign_node = make_ast_subtree(self.ast, ctx.getChild(i + 1), '=')
                            ctx.has_assign_node = True

                            make_ast_subtree(self.ast, ctx.getChild(i), key)
                            make_ast_subtree(self.ast, ctx.getChild(i + 2), value)
                            print(f"Adding node: '=' with key '{key}' and value '{value}'")
        else:
            make_ast_subtree(self.ast, ctx, rule_name)


    # def exitProgram(self, ctx):
    #     make_ast_subtree(self.ast, ctx, "PROGRAM", keep_node=True)

    def exitCluster(self, ctx):
        make_ast_subtree(self.ast, ctx, "CLUSTER", keep_node=True)

    def exitClustering_method(self, ctx):
        # method_name = ctx.getText()
        make_ast_subtree(self.ast, ctx, "method_name", keep_node=True)

    def exitArgs(self, ctx):
        # print(ctx.getChild(0).getText())
        make_ast_subtree(self.ast, ctx, '=', keep_node=True)
        # pass
    def exitN_clusters(self, ctx):
        # print(ctx.getChild(0).getText())
        make_ast_subtree(self.ast, ctx, "n_clusters", keep_node=True)
        # pass
    def exitN_iters(self, ctx):
        print(ctx.getText())
        make_ast_subtree(self.ast, ctx, "n_iters", keep_node=True)
    def exitRandom_state(self, ctx):
        make_ast_subtree(self.ast, ctx, "random_state", keep_node=True)
        print(ctx.getText())
    def exitEpsilon(self, ctx:ClusteringParser.EpsilonContext):
        make_ast_subtree(self.ast, ctx, "epsilon", keep_node=True)

    def exitMin_sample(self, ctx):
        make_ast_subtree(self.ast, ctx, "min_sample", keep_node=True)
    def exitLinkage(self, ctx:ClusteringParser.LinkageContext):
        make_ast_subtree(self.ast, ctx, "linkage", keep_node=True)

    def exitAffinity(self, ctx:ClusteringParser.AffinityContext):
        make_ast_subtree(self.ast, ctx, "affinity", keep_node=True)

    def exitPlot(self, ctx):
        make_ast_subtree(self.ast, ctx, "plot", keep_node=True)

    def exitPlot_args(self, ctx):
        make_ast_subtree(self.ast, ctx, "plot_args", keep_node=True)

    def exitDataset(self, ctx):
        make_ast_subtree(self.ast, ctx, "dataset", keep_node=True)
