from z3 import *

def smtlib_to_fol(smtlib_formula: str) -> str:
    # Initialize Z3 context
    ctx = Context()
    # Create a solver
    solver = Solver(ctx=ctx)
    # Declare variables dictionary
    variables = {}

    # Parse the SMT-LIB2 formula and add it to the solver
    formula = parse_smt2_string(smtlib_formula, decls=variables, ctx=ctx)
    solver.add(formula)

    # Convert the parsed formula to FOL format
    def fol_format(expr):
        if is_const(expr):
            return str(expr)
        elif is_app_of(expr, ctx):
            op = expr.decl()
            args = [fol_format(arg) for arg in expr.children()]
            return f"({op.name()} {' '.join(args)})"
        else:
            raise ValueError("Unsupported expression")

    # Get the converted FOL formula
    fol_formula = fol_format(formula)

    return fol_formula

# Example usage:
smtlib_formula = "(> (+ x 2) 5)"
fol_formula = smtlib_to_fol(smtlib_formula)
print(fol_formula)  # Output: "(> (+ x 2) 5)"
