# from func import *

# from unsatcore.unsat import * 
# from mutation.mutation import * 

# doubleRainbow = Int('doubleRainbow')
# rainbow = Int("rainbow")
# rain = Int("rain")
# lightning = Int("lightning")
# solution = Int("solution")
# x = Int("x")

# assertion = [ 
#             (12 == (doubleRainbow - rainbow + rainbow)),
#             (4 == (doubleRainbow - rain - rain)),
#             (22 == ((rain * rainbow) - lightning)),
#             (x == doubleRainbow),
#             (solution == (doubleRainbow / lightning - rain))
#         ]
# assertion =[
#     doubleRainbow - rainbow + rainbow == x,
#     doubleRainbow - rain - rain == 4, 
#     rain*rainbow - lightning == 22, 
#     doubleRainbow == 13,
#     solution == doubleRainbow/lightning - rain]

# assertion =[
#     doubleRainbow - rainbow + rainbow == 12,
#     doubleRainbow - rain - rain == 4, 
#     rain*rainbow - lightning == 22, 
#     doubleRainbow == x,
#     solution == doubleRainbow/lightning - rain]


# solver.add(assertion)

# assertion = [ 
#                 '(= 12 (+ (- doubleRainbow rainbow) rainbow))',
#                 '(= 4 (- (- doubleRainbow rain) rain))',
#                 '(= 22 (- (* rain rainbow) lightning))',
#                 '(= 13 doubleRainbow)',
#                 '(= solution (- (/ doubleRainbow lightning) rain))'
#             ]

# Add declarations to the solver
# for constant in constants:
#     solver.add(Int(constant))

# Add assertions to the solver
# for assertion in assertions:
#     solver.add(eval(assertion))
#     # print(assertion)


# check model and unsat core
# if solver.check() == sat:
#     #read the model
#     model = solver.model()
#     print("\nSat and model is \n"+ str(model) + "\n")
# else:
#     print("unsat");
# 

# filename = "formula/formula2.txt"
# with open(filename, "r") as file:
#     smtlib_formula = file.read()

# if datatype == 'Int':
    #     context[constant] = Int(constant)
    # elif datatype == 'Real':
    #     context[constant] = Real(constant)
    # elif datatype == 'Bool':
    #     context[constant] = Bool(constant)
    # elif datatype == 'Bit-vectors':
    #     context[constant] = BitVec(constant)
    
    
    # print("Constants with Data Types:")
# for constant, datatype in constants.items():
#     print(f"{constant}: {datatype}")

# print("\nAssertions:")
# for assertion in assertions:
#     print(assertion)
