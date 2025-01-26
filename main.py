from antlr4 import *
import  argparse
from gen.ClusteringLexer import ClusteringLexer
from gen.ClusteringParser import ClusteringParser
from Repository.ast_to_networkx_graph import show_ast
from Repository.post_order_ast_traverser import PostOrderASTTraverser
from Code.ClusteringCodeGenerator import ClusteringCodeGenerator
from Code.ClusteringCustomListener import ClusteringCustomListener

def main(arg):
    stream = FileStream(arg.input, encoding="utf-8")
    lexer = ClusteringLexer(stream)
    token_stream = CommonTokenStream(lexer)
    parser = ClusteringParser(token_stream)

    parse_tree = parser.cluster()
    ast_builder_listener = ClusteringCustomListener(parser.ruleNames)
    walker = ParseTreeWalker()
    walker.walk(t=parse_tree, listener=ast_builder_listener)

    ast = ast_builder_listener.ast
    show_ast(ast.root)

    traverser = PostOrderASTTraverser()
    traverser.node_attributes = ['label']
    traversal = traverser.traverse_ast(ast.root)
    print("traversal", traversal)
    # tr = [item['label'] for item in traversal]


    generator = ClusteringCodeGenerator()
    generated = generator.generate_code(traversal)
    print(generated)

    with open(arg.output, 'w') as out:
        out.write(generated)

if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-i', '--input', help='Input source', default=r'input.txt')
    argparser.add_argument('-o', '--output', help='Output path', default=r'gen.py')
    args = argparser.parse_args()
    main(args)