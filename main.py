from z3 import *
from unsatcore.unsat import * 
from mutation.mutation import * 
from func import *

# Read the SMT-LIB formula from a text file
file_path = './formula/formula33.txt';
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

print(context);

# Convert SMT-LIB[QF-LIA] to FOL 
assertions = []
for SMTLIB_assertion in SMTLIB_assertions:
    assertions.append(parse_smt2_string(SMTLIB_assertion, decls=context))

solver.add(assertions)

# Check for satisfiability
if solver.check() == sat:
    model = solver.model()
    print("\nFormula is sat \nour model is:\n",model,'\n')
    
elif solver.check() == unsat:
    # check the unsat core
    unsat = UnsatCoreChecker()
    unsat_result = unsat.check_unsat_core(solver)
    print("\nFormula is unsat \nunsat core at:"+ str(unsat_result) + "\n")
    
    # check the mutation
    mutation = MutationTesting()
    mutation_result = mutation.mutant_each_unsat(assertions, unsat_result)
    
else:
    print("The formula is unknown.") 
