from z3 import * 
from unsatcore.unsat import * 
from mutation.mutation import * 

solver = Solver()

# variable declarations
doubleRainbow = Int('doubleRainbow')
rainbow = Int("rainbow")
rain = Int("rain")
lightning = Int("lightning")
solution = Int("solution")

# assertions
assertion = [ 
            (13 == (doubleRainbow - rainbow + rainbow)),
            (40 == (doubleRainbow - rain - rain)),
            (22 == ((rain * rainbow) - lightning)),
            (13 == doubleRainbow),
            (solution == (doubleRainbow / lightning - rain))
        ]

solver.add(assertion)


# check model and unsat core
if solver.check() == sat:
    
    #read the model
    model = solver.model()
    print("\nSat and model is \n"+ str(model) + "\n")

elif solver.check() == unsat:
    
    # check the unsat core
    u = UnsatCoreChecker()
    unsat_result = u.check_unsat_core(solver)
    
    print("\nunsat core at: "+ str(unsat_result) + "\n")
    
    # implement test mutation here
    m = MutationTesting()
    
    mutation_result = m.mutant_each_unsat(assertion, unsat_result)
    print("\n mutation result is: "+ str(mutation_result) + "\n")
    
    
else:
    print("unkown")





# doubleRainbow - rainbow + rainbow == 12
# doubleRainbow - rain - rain == 4
# rain * rainbow - lightning == 22
# doubleRainbow / lightning - rain == solution

# 12 + 2 -2 = 12
# 12 - 4 - 4 = 4
# (4 * -2) - (-30) = 22
# (12 / -30) - 4 = -4