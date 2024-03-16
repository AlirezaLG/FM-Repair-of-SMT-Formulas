from z3 import *
# import z3


# # Create a solver
# solver = z3.Solver()

# # Add some constraints
# x = z3.Int('x')
# y = z3.Int('y')
# solver.add(x > 0)
# solver.add(y < 10)
# solver.add(x + y == 15)

# # Check satisfiability
# result = solver.check()

# # Print the result
# print("Result:", result)

# # Access and print statistics
# print("\nStatistics:")
# for key, value in solver.statistics():
#     print("- {}: {}".format(key, value))



# # Declare a boolean constant
# p = Bool('p')

# # Define the assertion
# assertion = Or(p, Not(p))

# # Create a solver
# solver = Solver()

# # Add the assertion to the solver
# solver.add(assertion)

# # Check if the assertion is satisfiable
# if solver.check() == sat:
#     # Get the model
#     model = solver.model()
#     # Display the model
#     print(model)
# else:
#     print("Assertion is unsatisfiable")
    
# x = Int('x')
# y = Int('y')
# n = x + y >= 3
# x = 20
x = Int('x')
y = Int('y')
asserts = "(assert (= (/ x (* 2 y)) 20))"
assertion = parse_smt2_string(asserts, decls={"x": x, "y": y})
print("is expr", is_expr(assertion[0].arg(1)))
print("is const", is_const(assertion[0].arg(1)))
print("is const", is_const(assertion[0].arg(1).arg(0)) )
print("main assertion is: ",assertion[0].arg(1).arg(0))


# The right-hand side of the equality expression, where the number 20 is located

# print("rhs value:", rhs)
for term in assertion[0].children():
    if isinstance(term, ArithRef):
        # Check if the term is a division operation
        if is_div(term):
            # Access the numerator of the division
            numerator = term.children()[0]
            if is_const(numerator):
                constant_value = numerator.as_long()
                print("Constant value:", constant_value)



# print ("num args: ", n.num_args())
# print ("children: ", n.children()[0])
# print ("1st child:", n.arg(0))
# print ("2nd child:", n.arg(1))
# print ("operator: ", n.decl())
# print ("op name:  ", n.decl().name())

# def find_arithmetic_operators(expr):
#     # Base case: if the expression is a constant or a simple variable, return
#     if is_const(expr) or is_var(expr):
#         return
    
#     # Check if the expression is an arithmetic operator
#     if expr.decl().kind() in [Z3_OP_ADD, Z3_OP_SUB, Z3_OP_MUL, Z3_OP_DIV, Z3_OP_MOD, Z3_OP_REM]:
#         # Print the operator
#         print(expr.decl())
    
#     # Recursively check the arguments of the expression
#     for arg in expr.children():
#         find_arithmetic_operators(arg)

# # Example usage
# x, y, z = Ints('x y z')
# original_expr = 12 < x - y + z + 1 + 4

# Traverse the expression and find arithmetic operators
# find_arithmetic_operators(original_expr)
# from z3 import *

# # Create a Z3 context
# ctx = Context()

# # Define functions for each operator
# def eq(x, y):
#     return x == y

# def gt(x, y):
#     return x > y

# def lt(x, y):
#     return x < y

# def ge(x, y):
#     return x >= y

# def le(x, y):
#     return x <= y

# # Create FuncDeclRef objects for each operator
# eq_func = Function('==', IntSort(ctx), IntSort(ctx), BoolSort(ctx))
# gt_func = Function('>', IntSort(ctx), IntSort(ctx), BoolSort(ctx))
# lt_func = Function('<', IntSort(ctx), IntSort(ctx), BoolSort(ctx))
# ge_func = Function('>=', IntSort(ctx), IntSort(ctx), BoolSort(ctx))
# le_func = Function('<=', IntSort(ctx), IntSort(ctx), BoolSort(ctx))

# # Print the FuncDeclRef objects for each operator
# print("FuncDeclRef for '==':", eq_func)
# print("FuncDeclRef for '>':", gt_func)
# print("FuncDeclRef for '<':", lt_func)
# print("FuncDeclRef for '>=':", ge_func)
# print("FuncDeclRef for '<=':", le_func)

# Create variables
# x, y,z = Ints('x y z')
# comparison_operators = [ '==', '>', '<', '>=', '<=']
# # Define the assertion
# assertion = 12 < x - y + z
# for op in comparison_operators:
#     print(type(assertion))
#     print(type(Bool(op)))
#     new_assert = substitute(assertion, (Bool(str(assertion.decl())), '\<' ))
#     print("New Assertion is:\t", new_assert)

# Extract constant values
# constants = set()

# for term in assertion.children():
#     print("term is:",term)
#     if is_int_value(term):
#         print("int value is:",term)
    # elif is_rational_value(term):
    #     print("rational value is:",term)
    #     # constants.add(term.as_long())

# print("Constant values in the assertion:", constants)

# Define Z3 variables
a = Int('x')
b = IntVal(5)

# Check if x has a discrete value
# print(is_int_value(a))
    

# Check if z has a discrete value
# print(is_int_value(b))
    

# print(is_int(IntVal('z')))

# print(substitute(x + 1, (x, y + 1)))
# s.add(assertion)
# print(s.check())
# print(s.model())
# # from func import *

# from z3 import *

# solver = Solver()

# # (declare-const x Int)
# # (declare-const y Int)
# # this is SMT-lib format
# # (assert (> (+ x y) 10))
# # (assert (< x 5))

# x = Int("x")
# y = Int("y")

# # python or z3 solver format 
# solver.add(x+y < 10)
# solver.add(x < 5)



# print('\n'+solver.to_smt2()+'\n')
# # sexpr


# if solver.check() == sat:
#     print("The formula is satisfiable.")
#     model = solver.model()
#     print("Model:")
#     print(model)
# else:
#     print("The formula is unsatisfiable.")




# Either this
# x = Function('x', IntSort())
# or this works from python
# x = Int('x')
# y = Int('x')

# assertion = parse_smt2_string('(assert (>= (* 2 x) 4))', decls={"x": x, "y": y})

