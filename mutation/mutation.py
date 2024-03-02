from z3 import * 
import re
class MutationTesting:
    def __init__(self):
        # Initialize MutationTesting class
        self.s = Solver()
        self.mutation_types = ["replace_constant"]
        self.asserts = []
        
    
    # mutant for each unsat [a1, a4]
    def mutant_each_unsat(self, assertion, unsat_core):
        for index in unsat_core:
            print("\nassertion index is:"+str(index))
            # self.implement_mutant_type(assertion, assertion[index])
            # implement different mutation types
            for mutation_type in self.mutation_types:
                result = self.mutate_test(assertion, index , mutation_type)
                # return ("for index "+ str(index) + "-" +str(result))
    
    
    def mutate_test(self, assertion, assertion_index , mutation_type):
        if mutation_type == "replace_constant":
            # replace constant
            result = self.replace_constant(assertion, assertion_index)
            
        elif mutation_type == "replace_operator":
            # replace operator
            print("replace operator")
            
        elif mutation_type == "delete_subformula":
            # delete subformula
            print("delete subformula")
            
        else:
            print("unkown mutation type")
        
        return "unsat";
    
      
    def replace_constant(self ,assertion, unsat_index):
        
        self.asserts = assertion.copy()
        self.asserts[unsat_index] = Bool(self.replace_integer_with_variable(str(self.asserts[unsat_index]), "x"))
        print(self.asserts)
        solver = Solver()
        solver.add(self.asserts)
        self.check_sat(solver)
        print("end")
    
    
    def replace_integer_with_variable(self, equation, variable):
        # Find the integer in the equation using a regular expression
        number_pattern = r'(?<!\w)(-?\d*\.?\d+(?:[eE][-+]?\d+)?)(?!\w)'
        match = re.search(number_pattern, equation)
        if match is not None:
            # If an integer is found, replace it with the variable
            integer = match.group()
            new_equation = equation.replace(integer, variable)
            return new_equation
        else:
            # If no integer is found, return the original equation
            return equation
    
    
    def check_sat(self, solver):
        if solver.check() == sat:
            m = solver.model()
            print("\nSat and model is \n"+ str(m))
        else:
            print("unsat and failed to find a model")
        