from z3 import *
from unsatcore.unsat import * 
from mutation.mutation import * 
from func import *
import cProfile
import pstats

# Read the SMT-LIB formula from a text file
file_path = './formula/formula20.txt';
with open(file_path, 'r') as file:
    formula_string = file.read()

# Call the function to extract constants with data types and assertions
constants, SMTLIB_assertions = extract_constants_and_assertions_with_datatypes(formula_string)

# Create a solver
solver = Solver()

# Declare constants alonside their data types
context = {}
for constant, datatype in constants.items():
    context[constant] = eval(datatype)(constant) # {'x': x, 'y': y}

print("constants are: ", context);

# Convert SMT-LIB[QF-LIA] to FOL 
assertions = []

for SMTLIB_assertion in SMTLIB_assertions:
    try:
        assertions.append(parse_smt2_string(SMTLIB_assertion, decls=context))
    except Exception as e:
        print("\nError in parsing: ", SMTLIB_assertion, "\n", e, "\n")
        sys.exit()  


solver.add(assertions)
print_d("assertions are: ", assertions[2])

exit()
# check mode
print("You are in: ", mode, "mode \n ")
# with cProfile.Profile() as pr:
    # Check for satisfiability
if solver.check() == sat:
    model = solver.model()
    print("Formula is sat \nour model is:\n",model,'\n')
    print_p("Sat and New SMT-LIB formula is: \n"+ solver.sexpr() + "\n")
    
elif solver.check() == unsat:
    # check the unsat core
    unsat = UnsatCoreChecker()
    unsat_result = unsat.check_unsat_core(solver)
    print("Formula is unsat \nunsat core at:"+ str(unsat_result) + "\n")
    
    # check the mutation
    mutation = MutationTesting()
    new_solver = mutation.mutant_each_unsat(assertions, unsat_result)
    # print("\nMutation result is:\n"+ str(new_solver.to_smt2) + "\n")
else:
    print("The formula is unknown.") 
# result = pstats.Stats(pr).sort_stats('cumulative')
# result.print_stats(10)
