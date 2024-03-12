from z3 import *
from func import *
import re
import time

class MutationTesting:
    def __init__(self):
        # Initialize MutationTesting class
        self.mutation_types = ["replace_operator"] # replace_constant, replace_operator, delete_assertion
        self.mutation_number = 0
        self.old_expr = []

    
    # mutant for each unsat [a1, a4]
    def mutant_each_unsat(self, assertion, unsat_core):
        for index in unsat_core:
            print_d("-------------------------------")
            print_d("Unsat index:" + str(index) + "\t"+ str(assertion[index]))
            print_d("-------------------------------")
            # self.implement_mutant_type(assertion, assertion[index])
            # implement different mutation types
            
            
            for mutation_type in self.mutation_types:
                result = self.mutate_test(assertion, index , mutation_type)
                # return ("for index "+ str(index) + "-" +str(result))
        # return result 
        
    
    
    def mutate_test(self, assertion, assertion_index , mutation_type):
        
        if mutation_type == "replace_constant":
            # replace constant
            print_d("*** Replace Constant Mutation ***")
            self.replace_constant(assertion, assertion_index)
            
        elif mutation_type == "replace_operator":
            # replace operator
            print_d("*** Replace Operator Mutation ***")
            self.replace_operator(assertion, assertion_index)
            
            
        elif mutation_type == "delete_assertion":
            # delete subformula
            print_d("Delete Assertion Mutation")
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
        
        print_d("** Replace arithmetic method **")
        asserts = assertion.copy() # make a new copy, old copy is modified
        expr = asserts[unsat_index][0]
        self.find_arithmetic_operators(asserts, expr, unsat_index)
        # self.replace_arithmetic_operator(assertion, unsat_index)
        
        # self.replace_comparison_operator(assertion, unsat_index)
        
                
        # Find Logical operator 
        start_time = time.time()
        asserts = assertion.copy() # make a new copy, old copy is modified
        print_d("** Logical operators method **")
        if (contains_logical_operators(assertion[unsat_index][0])):
            print_d("Default unsat bool index is: ",assertion[unsat_index][0] ,"\n")
            # check for the first logical operator
            asserts[unsat_index] = replace_logical_operators(assertion[unsat_index][0])
            print_d("revised assertions is: ",asserts[unsat_index])
            print("assert is ",asserts);
            self.check_sat(asserts, start_time)
        else :
            print_d("No logical operator found\n")

    # def find_logical_operators(self, asserts, expr ,unsat_index):
    #     # Base case: if the expression is a constant or a simple variable, return
    #     if  not expr.decl().arity() == 2 or is_const(expr) or is_var(expr) :
    #         return 
    #     # print("-----------------")
    #     self.old_expr.append(expr)
    #     # print("expr is ",expr.decl().arity())
    #     # print('length old_expr is:\t',len(self.old_expr)-1)
    #     # for old in self.old_expr:
    #     #     print("old is ",old)
    #     # print("\n")
        
    #     # Check if the expression is an arithmetic operator
    #     if expr.decl().kind() in [Z3_OP_ADD, Z3_OP_SUB, Z3_OP_MUL, Z3_OP_DIV, Z3_OP_MOD, Z3_OP_IDIV]:
    #         for op in arithmetic_operators:
    #             if (str(expr.decl()) != op):
    #                 start_time = time.time()
    #                 # replace new operator with the old one for nested expression
    #                 if (len(self.old_expr) > 1):
    #                     asserts[unsat_index] = substitute(self.old_expr[0], (self.old_expr[len(self.old_expr)-1] , replace_arithmetic_decl(expr, op) ))
    #                 #if it is not nested expression
    #                 else:
    #                     asserts[unsat_index] = replace_arithmetic_decl(expr, op)
    #                 print_d("asserts[unsat_index] is:\t", asserts[unsat_index] )
    #                 # print("new assert is: \t",replace_arithmetic_decl(expr, op),' \n')
    #                 # print_d("assert is:", asserts )
    #                 self.check_sat(asserts, start_time)
        
    #     # Recursively check the arguments of the expression
    #     for arg in expr.children():
    #         self.find_arithmetic_operators(asserts ,arg ,unsat_index)



    def find_arithmetic_operators(self, asserts, expr ,unsat_index):
        # Base case: if the expression is a constant or a simple variable, return
        if  not expr.decl().arity() == 2 or is_const(expr) or is_var(expr) :
            return 
        # print("-----------------")
        self.old_expr.append(expr)
        # print("expr is ",expr.decl().arity())
        # print('length old_expr is:\t',len(self.old_expr)-1)
        # for old in self.old_expr:
        #     print("old is ",old)
        # print("\n")
        
        # Check if the expression is an arithmetic operator
        if expr.decl().kind() in [Z3_OP_ADD, Z3_OP_SUB, Z3_OP_MUL, Z3_OP_DIV, Z3_OP_MOD, Z3_OP_IDIV]:
            for op in arithmetic_operators:
                if (str(expr.decl()) != op):
                    start_time = time.time()
                    # replace new operator with the old one for nested expression
                    if (len(self.old_expr) > 1):
                        asserts[unsat_index] = substitute(self.old_expr[0], (self.old_expr[len(self.old_expr)-1] , replace_arithmetic_decl(expr, op) ))
                    #if it is not nested expression
                    else:
                        asserts[unsat_index] = replace_arithmetic_decl(expr, op)
                    print_d("asserts[unsat_index] is:\t", asserts[unsat_index] )
                    # print("new assert is: \t",replace_arithmetic_decl(expr, op),' \n')
                    # print_d("assert is:", asserts )
                    self.check_sat(asserts, start_time)
        
        # Recursively check the arguments of the expression
        for arg in expr.children():
            self.find_arithmetic_operators(asserts ,arg ,unsat_index)


        
        
        
        
        
    
        
    def replace_comparison_operator(self ,assertion, unsat_index):
        # Find Comparison operator
        print_d("** Replace comparison method **")
        start_time = time.time()
        asserts = assertion.copy() # make a new copy, old copy is modified
        expr = assertion[unsat_index][0]
        if (is_comperison_operator(expr)):
            for op in comparison_operators:
                if (str(expr.decl()) != op):
                    asserts[unsat_index] = replace_comparison_decl(expr, op)
                    print_d("Comparison operators: [", op, "] " , asserts[unsat_index] )
                    self.check_sat(asserts, start_time)
        else:
            print_d("No comparison operator found\n")
        
   
    # replace constant
    def replace_constant(self ,assertion, unsat_index):
        start_time = time.time()
        asserts = assertion.copy()
        asserts[unsat_index] = self.replace_number_with_variable(asserts[unsat_index][0])
        self.check_sat(asserts, start_time)
        
        
        
        
    def replace_number_with_variable(self, unsat_assert):
        # check first arg if it is a number (int or real)
        for term in unsat_assert.children():
            if (is_number(term)):
                new_assert = substitute(unsat_assert, (term, Int('X')))
                print_d("New Assertion is:\t",new_assert)
                return new_assert
            
    
    
    
    
    # check the satisfiability
    def check_sat(self, asserts, start_time = 0):
        if(asserts != []):
            solver = Solver()
            solver.add(asserts)
            if solver.check() == sat:
                m = solver.model()
                self.mutation_number += 1
                print_d("Sat and model is: \n"+ str(m)+ "\n")
                print_p("Sat and New SMT-LIB formula is: \n"+ solver.to_smt2()) #sexpr
                print_d("Execution time in ms: ", round((time.time() - start_time) * 1000, 2)) 
                print_d("-----------------------------------")
            else:
                print_d("unsat and failed to find a Model")
                print_d("************* END *************")
                
        else:
            print("No assertion to check\n")
            
        