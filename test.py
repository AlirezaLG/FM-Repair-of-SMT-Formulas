from z3 import * 
# from unsatcore.unsat import * 
# from mutation.mutation import * 

solver = Solver()

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
assertions = []
filename = "bank/formula2.txt"

with open(filename, "r") as file:
    for line in file:
        # Check if the line contains an assertion
        if line.startswith('(assert'):
            # Extract the assertion
            assertion = line.strip()
            assertions.append(assertion)
    smtlib_formula = file.read()

for assertion in assertions:
    print("Assertion:", assertion)

            
solver.from_string(smtlib_formula)


# check model and unsat core
if solver.check() == sat:
    
    #read the model
    model = solver.model()
    print("\nSat and model is \n"+ str(model) + "\n")
else:
    print("unsat");
# 