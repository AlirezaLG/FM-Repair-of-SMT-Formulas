from z3 import *
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


s = Solver()

# Either this
# x = Function('x', IntSort())
# or this works from python
x = Int('x')
y = Int('x')

assertion = parse_smt2_string('(assert (>= (* 2 x) 4))', decls={"x": x, "y": y})
s.add(assertion)
print(s.check())
print(s.model())