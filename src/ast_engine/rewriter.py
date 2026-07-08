import ast


class ASTRewriter(ast.NodeTransformer):
    """
    AST Rewriter for PyChronicle.

    This class injects trace() calls after assignment statements.
    """

    def visit_Assign(self, node):
        """
        Handle normal assignments.
        Example:
            a = 5
        """

        self.generic_visit(node)

        target = node.targets[0]

        if isinstance(target, ast.Name):
            trace_call = ast.Expr(
                value=ast.Call(
                    func=ast.Name(id="trace", ctx=ast.Load()),
                    args=[
                        ast.Constant(target.id),
                        ast.Name(id=target.id, ctx=ast.Load()),
                        ast.Constant(node.lineno),
                    ],
                    keywords=[],
                )
            )

            return [node, trace_call]

        return node

    def visit_AugAssign(self, node):
        """
        Handle augmented assignments.
        Example:
            a += 2
        """

        self.generic_visit(node)

        target = node.target

        if isinstance(target, ast.Name):
            trace_call = ast.Expr(
                value=ast.Call(
                    func=ast.Name(id="trace", ctx=ast.Load()),
                    args=[
                        ast.Constant(target.id),
                        ast.Name(id=target.id, ctx=ast.Load()),
                        ast.Constant(node.lineno),
                    ],
                    keywords=[],
                )
            )

            return [node, trace_call]

        return node