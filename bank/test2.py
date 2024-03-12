from z3 import *

# Create variables
x, y = Ints('x y')

# Define the assertion
assertion = (x - 2)+y > 10

# Extract constant values
constants = set()

for term in assertion.children():
    print("term is:",term)
    if is_int_value(term):
        print("int value is:",term)
    # elif is_rational_value(term):
    #     print("rational value is:",term)
    #     # constants.add(term.as_long())

# print("Constant values in the assertion:", constants)

# Define Z3 variables
a = Int('x')
b = IntVal(5)

# Check if x has a discrete value
print(is_int_value(a))
    

# Check if z has a discrete value
print(is_int_value(b))
    

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

