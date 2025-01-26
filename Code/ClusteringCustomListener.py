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

        # def exitExpr(self, ctx: calculatorParser.ExprContext):
        #     if ctx.getChildCount() == 1:
        #         self.result = ctx.getChild(0).value
        #         ctx.value = self.result
        #     else:
        #         result = ctx.getChild(0).value
        #         length = ctx.getChildCount() - 1
        #         for i in range(1, length, 2):
        #             op = ctx.getChild(i).getText()
        #             if op == '+':
        #                 value = ctx.getChild(i + 1).value
        #                 result = result + value
        #             elif op == '-':
        #                 value = ctx.getChild(i + 1).value
        #                 result = result - value
        #         self.result = result
        #         ctx.value = result
    def exitEveryRule(self, ctx):
        rule_idx = ctx.getRuleIndex()
        rule_name = self.rule_names[rule_idx]
        print(f"Processing rule: {rule_name}, ctx: {ctx.getText()}")
        if rule_name not in self.overridden_rules:
            if ctx.getChildCount() > 1:
                length = ctx.getChildCount() - 1
                for i in range(1, length, 2):
                    if rule_name == '=':
                        value = ctx.getChild(i + 1).value
                        print(value)
                        make_ast_subtree(self.ast, ctx, '=', keep_node=True)
                        make_ast_subtree(self.ast, ctx.getChild(i+1), value, keep_node=True)
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




    # def exitAssign(self, ctx: ClusteringParser.AssignContext):
    #     make_ast_subtree(self.ast, ctx, '=', keep_node=True)
    #     print(ctx.getText())
    #
    # def exitExpr(self, ctx):
    #     expr_value = ctx.getText()
    #     print(expr_value)
    #     make_ast_subtree(self.ast, ctx, expr_value, keep_node=True)

    # def exitPlot(self, ctx):
    #     make_ast_subtree(self.ast, ctx, "PLOT", keep_node=True)
    #
    # def exitPlot_args(self, ctx):
    #     x_var = ctx.getChild(2).getText()
    #     y_var = ctx.getChild(6).getText()
    #     make_ast_subtree(self.ast, ctx, "PLOT_ARGS", keep_node=True)
    #     make_ast_subtree(self.ast, ctx.getChild(2), f"X={x_var}", keep_node=True)
    #     make_ast_subtree(self.ast, ctx.getChild(6), f"Y={y_var}", keep_node=True)
    #
    # def exitDataset(self, ctx):
    #     file_name = ctx.getChild(4).getText()
    #     make_ast_subtree(self.ast, ctx, f"DATASET: {file_name}", keep_node=True)
    #
    # def exitNum(self, ctx):
    #     num_value = ctx.getText()
    #     make_ast_subtree(self.ast, ctx, num_value, keep_node=True)
    #
    # def exitString(self, ctx):
    #     string_value = ctx.getText()
    #     make_ast_subtree(self.ast, ctx, string_value, keep_node=True)
    #
    # def exitVar(self, ctx):
    #     var_name = ctx.getText()
    #     make_ast_subtree(self.ast, ctx, var_name, keep_node=True)

    # def exitLinkage_type(self, ctx):
    #     linkage_value = ctx.getText()
    #     make_ast_subtree(self.ast, ctx, linkage_value, keep_node=True)
    #
    # def exitAffinity_type(self, ctx):
    #     affinity_value = ctx.getText()
    #     make_ast_subtree(self.ast, ctx, affinity_value, keep_node=True)