import ast


class ASTRewriter(ast.NodeTransformer):
    """
    Inserts a trace() call after every assignment.
    """

    def visit_Assign(self, node):
        self.generic_visit(node)

        target = node.targets[0]

        if isinstance(target, ast.Name):
            trace_call = ast.Expr(
                value=ast.Call(
                    func=ast.Name(id="trace", ctx=ast.Load()),
                    args=[
                        ast.Constant(target.id)
                    ],
                    keywords=[]
                )
            )

            return [node, trace_call]

        return node