from z3 import *
from func import *
import re
import time

class MutationTesting:
    def __init__(self):
        # Initialize MutationTesting class
        
        global result

        # self.mutation_number = 0
        self.old_expr = []
        self.old_logical_expr = []

    
    # mutant for each unsat [a1, a4]
    def mutant_each_unsat(self, assertion, unsat_core):
        for index in unsat_core:
            print_d("\n-------------------------------")
            print_d("Unsat index:" + str(index) + "\t"+ str(assertion[index]))
            print_d("-------------------------------")
            
            # implement different mutation types
            for mutation_type in mutation_orders:
                if mutation_type == "replace_constant":
                    print_d("*** Replace Constant Mutation ***\n")
                    self.replace_constant(assertion, index)
                    
                elif mutation_type == "replace_operator":
                    print_d("*** Replace Operator Mutation ***\n")
                    self.replace_operator(assertion, index)
                    
                elif mutation_type == "delete_assertion":
                    print_d("*** Delete Assertion Mutation ***\n")
                    self.delete_assertion(assertion, index)
                    
                else:
                    print_d("Unkown mutation type")
                
    
    # replace only one operator at the time 
    def replace_operator(self, assertion, unsat_index):
        asserts = assertion.copy() # make a new copy, old copy is modified
        expr = asserts[unsat_index][0]
        # call the operator in custom order
        for op_name in operator_orders:
            if op_name == "find_arithmetic_operators":
                print_d("** Find arithmetic method **")
                self.find_arithmetic_operators(asserts, expr, unsat_index)
            elif op_name == "find_comparison_operators":
                print_d("** Find comparison method **")
                self.find_comparison_operators(assertion, unsat_index)
            elif op_name == "find_logical_operators":
                print_d("** Find logical method **")
                self.find_logical_operators(assertion, expr, unsat_index)
            else:
                print("no operator to call")
            
    def delete_assertion(self, assertion, unsat_index):
        start_time = time.time()
        asserts = assertion.copy()
        print_d("Deleted Assertion index is: ",str(asserts[unsat_index]))
        asserts.pop(unsat_index)
        self.check_sat(asserts, start_time)


    def find_logical_operators(self, asserts, expr ,unsat_index):
        # print("expr : \t",expr)
        # print("is const: \t",is_const(expr))
        # print("is var: \t",is_var(expr))
        # Base case: if the expression is a constant or a simple variable, return
        if  is_const(expr) or is_var(expr) :
            return 
        # print("-----------------")
        self.old_logical_expr.append(expr)
        # print('length old_logical_expr is:\t',len(self.old_logical_expr)-1)
        # for old in self.old_logical_expr:
        #     print("old is ",old)
        # print("\n")
        
        # Check if the expression is an arithmetic operator
        if expr.decl().kind() in [Z3_OP_AND, Z3_OP_OR, Z3_OP_NOT]:
            # print_d("Default unsat bool index is: ",expr ,"\n")
            # check for the first logical operator
            start_time = time.time()
            if (len(self.old_logical_expr) > 1):
                asserts[unsat_index] = substitute(self.old_logical_expr[0], (self.old_logical_expr[len(self.old_logical_expr)-1] , replace_logical_operators(expr) ))
            #if it is not nested expression
            else:
                asserts[unsat_index] = replace_logical_operators(expr)
            print_d("revised assertions is: ",asserts[unsat_index])
            self.check_sat(asserts, start_time)
            
        # Recursively check the arguments of the expression
        for arg in expr.children():
            self.find_logical_operators(asserts ,arg ,unsat_index)



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
                    print_d("operator is: ",op )
                    start_time = time.time()
                    # replace new operator with the old one for nested expression
                    if (len(self.old_expr) > 1):
                        # print_d("index 0: ",self.old_expr[0])
                        # print_d("find: ", self.old_expr[len(self.old_expr)-1]);
                        # print_d("Default unsat index is: ",expr)
                        # print_d("operator is: ",op)
                        # print(replace_arithmetic_decl(expr, op))
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

        
    def find_comparison_operators(self ,assertion, unsat_index):
        # Find Comparison operator
        start_time = time.time()
        asserts = assertion.copy() # make a new copy, old copy is modified
        print("assertion index: ",assertion[unsat_index][0])
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
        for term in asserts[unsat_index][0].children():
            # print("number: ",is_rational_value(term))
            # print_d("term is: ",term)
            if (is_number(term)):
                XX = Real('X') if is_rational_value(term) else Int('X') 
                asserts[unsat_index] = substitute(asserts[unsat_index][0], (term, XX))
                print_d("New Assertion is:\t",asserts[unsat_index])
                self.check_sat(asserts, start_time)
            

    # check the satisfiability
    def check_sat(self, asserts, start_time = 0):
        if(asserts != []):
            # print_d("asserts is: ", asserts)  
            solver = Solver()
            solver.add(asserts)
            if solver.check() == sat:
                m = solver.model()
                result.append(solver)
                # self.mutation_number += 1
                print_d("Sat and model is: \n"+ str(m)+ "\n")
                print_p("Sat and New SMT-LIB formula is: \n"+ solver.to_smt2()) #sexpr
                print_d("Execution time in ms: ", round((time.time() - start_time) * 1000, 2)) 
                print_d("-----------------------------------")
            else:
                print_d("unsat and failed to find a Model")
                print_d("************* END *************")
                
        else:
            print("No assertion to check\n")
            
        