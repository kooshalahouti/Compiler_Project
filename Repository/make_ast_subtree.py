def make_ast_subtree(ast, tree_node_ctx, node_value, keep_node=False):
    children = []
    raw_children_count = tree_node_ctx.getChildCount()

    ignored_tokens = {"(", ")", ","}

    for i in range(raw_children_count):
        child = tree_node_ctx.getChild(i)
        child_text = child.getText()

        if child_text in ignored_tokens:
            continue

        if hasattr(child, "ast_value"):
            children.append(child.ast_value)
        else:
            children.append(ast.make_node(value=child_text, children=[]))

    if raw_children_count == 3 and tree_node_ctx.getChild(1).getText() == '=':
        key = tree_node_ctx.getChild(0).getText()
        value = tree_node_ctx.getChild(2).getText()

        if node_value == "=" and any(child.value == "=" for child in children):
            tree_node_ctx.ast_value = children[0]
        else:
            assign_node = ast.make_node(value="=", children=[
                ast.make_node(value=key, children=[]),
                ast.make_node(value=value, children=[])
            ])
            tree_node_ctx.ast_value = assign_node
            ast.root = assign_node
    else:
        tree_node_ctx.ast_value = ast.make_node(value=node_value, children=children)
        ast.root = tree_node_ctx.ast_value

    print(
        f"Created node: {tree_node_ctx.ast_value.value}, Children: {[child.value for child in tree_node_ctx.ast_value.children]}"
    )