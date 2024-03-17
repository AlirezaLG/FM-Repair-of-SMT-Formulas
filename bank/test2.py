from z3 import *

# New dataset
datasets = {
    11: {':elim-unconstrained': 1, ':max-memory': 79.34, ':memory': 75.08, ':nlsat-propagations': 2, ':nlsat-stages': 3, ':num-allocs': 675596154, ':rlimit-count': 8961, ':solve-eqs-elim-vars': 4, ':solve-eqs-steps': 10, ':time': 0.04},
    12: {':elim-unconstrained': 1, ':max-memory': 79.34, ':memory': 80.08, ':nlsat-propagations': 2, ':nlsat-stages': 3, ':num-allocs': 675596154, ':rlimit-count': 8961, ':solve-eqs-elim-vars': 4, ':solve-eqs-steps': 2, ':time': 0.09},
    13: {':elim-unconstrained': 1, ':max-memory': 79.34, ':memory': 100.08, ':nlsat-propagations': 2, ':nlsat-stages': 3, ':num-allocs': 675596154, ':rlimit-count': 8961, ':solve-eqs-elim-vars': 4, ':solve-eqs-steps': 6, ':time': 0.01}
}
print(datasets.keys())
key_list = list(datasets.keys())
print(key_list[2])
# print(datasets,'\n')
# Define the weights based on priority
weights = {':time': -1, ':memory': 1, ':solve-eqs-steps': 1}  # Negative weight for ':time' since lower is better

# Normalize each parameter to [0, 1] and calculate the weighted score for each solution
max_values = {key: max(entry[key] for entry in datasets.values()) for key in weights}
min_values = {key: min(entry[key] for entry in datasets.values()) for key in weights}
    
def calculate_score(entry,  weights, dataset):
    

    score = 0
    for key, weight in weights.items():
        # Normalize the value to [0, 1] range
        normalized_value = (entry[key] - min_values[key]) / (max_values[key] - min_values[key]) if max_values[key] != min_values[key] else 0
        # Adjust score based on weight
        score += weight * normalized_value if weight > 0 else -weight * (1 - normalized_value)
    # print("Score for solution", entry, ":", score)
    return score

max_values = {key: max(entry[key] for entry in datasets.values()) for key in weights}
min_values = {key: min(entry[key] for entry in datasets.values()) for key in weights}
    
# Sort solutions based on their scores
sorted_solutions = sorted(datasets.items(), key=lambda item: calculate_score(item[1], weights ,datasets), reverse=True)

# print("Solutions sorted by composite score:")
# print(sorted_solutions)
# for solution in sorted_solutions:
#     print(solution)



# # Define the dataset
# solutions = {
#     0: {'elim-unconstrained': 1, 'max-memory': 79.34, 'memory': 75.08, 'nlsat-propagations': 2, 'nlsat-stages': 3, 'num-allocs': 675596154, 'rlimit-count': 8961, 'solve-eqs-elim-vars': 4, 'solve-eqs-steps': 10, "time": 0.1},
#     1: {'elim-unconstrained': 1, 'max-memory': 79.34, 'memory': 20.08, 'nlsat-propagations': 2, 'nlsat-stages': 3, 'num-allocs': 675596154, 'rlimit-count': 8961, 'solve-eqs-elim-vars': 4, 'solve-eqs-steps': 10, "time": 2.1},
#     # Add more solutions as needed
# }

# # Define the weights for all parameters based on priority (1 being the highest priority)
# weights = {'time': 1, 'memory': -2, 'solve-eqs-steps': 3, 'nlsat-stages': 4}

# # Normalize each parameter to [0, 1] and calculate the weighted score for each solution
# max_values = {key: max(solution[key] for solution in solutions.values() if key in solution) for key in weights}
# min_values = {key: min(solution[key] for solution in solutions.values() if key in solution) for key in weights}

# def calculate_score(solution):
#     score = 0
#     for key, weight in weights.items():
#         if key not in solution:
#             continue
#         # Normalize the value to [0, 1] range
#         if key == 'memory' or key == 'nlsat-stages':
#             normalized_value = 1 - (solution[key] - min_values[key]) / (max_values[key] - min_values[key]) if max_values[key] != min_values[key] else 0
#         else:
#             normalized_value = (solution[key] - min_values[key]) / (max_values[key] - min_values[key]) if max_values[key] != min_values[key] else 0
#         # Subtract from 1 if higher values are better
#         if weight < 0:
#             normalized_value = 1 - normalized_value
#             weight = -weight
#         score += weight * normalized_value
#     print("Score for solution", solution, ":", score)
#     return score

# # Sort solutions based on their scores
# sorted_solutions = sorted(solutions.items(), key=lambda x: calculate_score(x[1]), reverse=True)

# print("Solutions sorted by composite score:")
# for  solution in sorted_solutions:
#     print(f"Solution: {solution}")


# results = [
#     {'solve-eqs-steps': 11, 'nlsat stages': 90, 'memory': 20, 'time': 0.006, 'newval': 4, 'othernew': 45},
#     {'solve-eqs-steps': 10, 'nlsat stages': 3, 'memory': 20, 'time': 0.1, 'newval': 3, 'othernew': 4},
#     {'solve-eqs-steps': 10, 'nlsat stages': 40, 'memory': 33.4, 'time': 0.002, 'newval': 6, 'othernew': 44},
#     {'solve-eqs-steps': 100, 'nlsat stages': 1, 'memory': 71.5, 'time': 0.003, 'newval': 33, 'othernew': 3}
# ]

# # Define the weights based on priority (1 being the highest priority)
# # weights = {'time': 4, 'memory': 3, 'solve-eqs-steps': 2, 'nlsat stages': 1}
# weightz = {'time': 1, 'memory': 2, 'solve-eqs-steps': 3, 'nlsat stages': -4}

# # Normalize each parameter to [0, 1] and calculate the weighted score for each solution
    
    
# def calculate_score(solution, weights,solutions):
#     max_values = {key: max(solution[key] for solution in solutions) for key in weightz}
#     min_values = {key: min(solution[key] for solution in solutions) for key in weightz}

#     score = 0
#     for key, weight in weights.items():
#         # Normalize the value to [0, 1] range
#         if key == 'time' or key == 'memory': # Lower values are better
#             normalized_value = 1 - (solution[key] - min_values[key]) / (max_values[key] - min_values[key]) if max_values[key] != min_values[key] else 0
#         else: # Higher values are better
#             normalized_value = (solution[key] - min_values[key]) / (max_values[key] - min_values[key]) if max_values[key] != min_values[key] else 0
#         # Subtract from 1 if higher values are better
#         if weight < 0:
#             normalized_value = 1 - normalized_value
#             weight = -weight
#         score += weight * normalized_value
        
#     print("Score for solution", solution, ":", score)
#     return score

# # Sort solutions based on their scores
# # sorted_solutions = sorted(solutions, key=calculate_score)
    
# sorted_solutions = sorted(results, key=lambda x: calculate_score(x, weightz, results))


# print("Solutions sorted by composite score:")
# for solution in sorted_solutions:
#     print(solution)

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
# x = Int('x')
# y = Int('y')
# asserts = "(assert (= (/ x (* 2 y)) 20))"
# assertion = parse_smt2_string(asserts, decls={"x": x, "y": y})
# print("is expr", is_expr(assertion[0].arg(1)))
# print("is const", is_const(assertion[0].arg(1)))
# print("is const", is_const(assertion[0].arg(1).arg(0)) )
# print("main assertion is: ",assertion[0].arg(1).arg(0))


# The right-hand side of the equality expression, where the number 20 is located

# print("rhs value:", rhs)
# for term in assertion[0].children():
#     if isinstance(term, ArithRef):
#         # Check if the term is a division operation
#         if is_div(term):
#             # Access the numerator of the division
#             numerator = term.children()[0]
#             if is_const(numerator):
#                 constant_value = numerator.as_long()
#                 print("Constant value:", constant_value)



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

