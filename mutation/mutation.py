from z3 import *
from func import *
import re
import time

class MutationTesting:
    def __init__(self):
        # Initialize MutationTesting class
        self.s = Solver()
        # replace_constant, replace_operator, delete_assertion
        self.mutation_types = ["replace_operator","delete_assertion"]
        self.asserts = []
        self.mutation_number = 0
        

    
    # mutant for each unsat [a1, a4]
    def mutant_each_unsat(self, assertion, unsat_core):
        for index in unsat_core:
            print_d("-------------------------------")
            print_d("Unsat index " + str(index) + "; assert is: "+ str(assertion[index]))
            print_d("-------------------------------\n")
            # self.implement_mutant_type(assertion, assertion[index])
            # implement different mutation types
            
            
            for mutation_type in self.mutation_types:
                result = self.mutate_test(assertion, index , mutation_type)
                # return ("for index "+ str(index) + "-" +str(result))
        # return result 
        
    
    
    def mutate_test(self, assertion, assertion_index , mutation_type):
        
        if mutation_type == "replace_constant":
            # replace constant
            print_d("Replace constant method\n")
            self.replace_constant(assertion, assertion_index)
            
        elif mutation_type == "replace_operator":
            # replace operator
            print_d("Replace operator method")
            self.replace_operator(assertion, assertion_index)
            
            
        elif mutation_type == "delete_assertion":
            # delete subformula
            print_d("Delete assertion method\n")
            self.delete_assertion(assertion, assertion_index)
            
    
        else:
            print_d("unkown mutation type")
        # return result
    
    
        
    
    def delete_assertion(self, assertion, unsat_index):
        start_time = time.time()
        asserts = assertion.copy()
        print_d("Deleted Assertion index is: ",str(asserts[unsat_index]))
        asserts.pop(unsat_index)
        self.check_sat(asserts, start_time)

    
    # replace only one operator at the time 
    def replace_operator(self, assertion, unsat_index):
        
        # Find Arithmetic operator
        asserts = assertion.copy()
        words = str(asserts[unsat_index]).split()
        start_time = time.time()
        print_d("Arithmetic operators: ")
        if array_check_for_match(words, arithmetic_operators):
            for i, word in enumerate(words):
                if word in arithmetic_operators:
                    print_d("found operator", word)
                    for op in arithmetic_operators:
                        orginal_operand = word
                        if (word != op): #we dont want to check assertion with same operator
                            words[i] =  word.replace(word, op)
                            print_d("New Assertions is: "," ".join(words));
                            asserts[unsat_index] = Bool(" ".join(words))
                            self.check_sat(asserts, start_time)
                            words[i] = orginal_operand
        else:
            print_d("No arithmetic operator found\n")
                
        # Find Comparison operator
        start_time = time.time()
        asserts = assertion.copy() # make a new copy, old copy is modified
        words = str(asserts[unsat_index]).split()
        print_d("Comparison operators: ")
        if array_check_for_match(words, comparison_operators):
            for i, word in enumerate(words):
                if word in comparison_operators:
                    print_d("found operator", word)
                    for op in comparison_operators:
                        orginal_operand = word
                        if (word != op): #we dont want to check assertion with same operator
                            words[i] =  word.replace(word, op)
                            print_d("New Assertions is: "," ".join(words));
                            asserts[unsat_index] = bool(" ".join(words))
                            self.check_sat(asserts, start_time)
                            words[i] = orginal_operand
        else:
            print_d("No comparison operator found\n")
                
        # Find Logical operator
        start_time = time.time()
        asserts = assertion.copy() # make a new copy, old copy is modified
        print_d("Logical operators:")
        if (contains_logical_operators(assertion[unsat_index][0])):
            print_d("Default unsat bool index is: ",assertion[unsat_index][0] ,"\n")
            # check for the first logical operator
            asserts[unsat_index] = replace_logical_operators(assertion[unsat_index][0])
            print_d("revised assertions is: ",asserts[unsat_index])
            print("assert is ",asserts);
            self.check_sat(asserts, start_time)
        else :
            print_d("No logical operator found\n")

        # return string
        
   
    # replace constant
    def replace_constant(self ,assertion, unsat_index):
        start_time = time.time()
        asserts = assertion.copy()
        asserts[unsat_index] = Bool(self.replace_integer_with_variable(str(asserts[unsat_index]), "X"))
        self.check_sat(asserts, start_time)
        
        
        
        
    def replace_integer_with_variable(self, equation, variable):
        # Find the integer in the equation using a regular expression, skip if there is number in the variable
        number_pattern = r'(?<!\w)(-?\d*\.?\d+(?:[eE][-+]?\d+)?)(?!\w)'
        match = re.search(number_pattern, equation)
        if match is not None:
            # If any datatype is found, replace it with the variable
            integer = match.group()
            new_equation = equation.replace(integer, variable)
            return new_equation
        else:
            # If no integer is found, return the original equation
            return equation
    
    
    
    
    # check the satisfiability
    def check_sat(self, asserts, start_time = 0):
        if(asserts != []):
            solver = Solver()
            solver.add(asserts)
            if solver.check() == sat:
                m = solver.model()
                self.mutation_number += 1
                print_d("Sat and model is: \n"+ str(m)+ "\n")
                print_d("Sat and New SMT-LIB formula is: \n"+ solver.to_smt2()) #sexpr
                print_d("Execution time in ms: ", (time.time() - start_time) * 1000 ) 
                print_d("-----------------------------------")
            else:
                print_d("unsat and failed to find a Model\n")
                print_d("-----------------------------------")
                
        else:
            print("No assertion to check\n")
            
        