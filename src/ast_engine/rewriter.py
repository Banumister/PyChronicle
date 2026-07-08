import ast


class ASTRewriter(ast.NodeTransformer):
    """
    AST Rewriter for PyChronicle.

    This class visits assignment statements and injects a
    trace() function call immediately after each assignment.

    Example:

    Original:
        a = 5

    Rewritten:
        a = 5
        trace("a", a, 1)
    """

    def visit_Assign(self, node):
        """
        Visit assignment nodes and inject a trace() call.
        """
        # Visit child nodes first
        self.generic_visit(node)

        # Handle only simple variable assignments
        target = node.targets[0]

        if isinstance(target, ast.Name):

            trace_call = ast.Expr(
                value=ast.Call(
                    func=ast.Name(
                        id="trace",
                        ctx=ast.Load()
                    ),
                    args=[
                        # Variable name
                        ast.Constant(target.id),

                        # Current variable value
                        ast.Name(
                            id=target.id,
                            ctx=ast.Load()
                        ),

                        # Line number
                        ast.Constant(node.lineno)
                    ],
                    keywords=[]
                )
            )

            # Return the original assignment followed by trace()
            return [node, trace_call]

        return node