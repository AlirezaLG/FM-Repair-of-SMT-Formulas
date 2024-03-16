from z3 import * 
from config import *


def replace_logical_operators(expr):
    # expr = Bool(str(expr))
    if is_and(expr):
        # Replace AND with your desired operation
        return Or(expr.children())
    elif is_or(expr):
        # Replace OR with your desired operation
        return And(expr.children())
    elif is_not(expr):
        # Replace NOT with your desired operation
        return expr.arg(0)
    else:
        # If it's not a logical operator, return as it is
        return expr

# def contains_logical_operators(expr):
#     if is_and(expr) or is_or(expr) or is_not(expr):
#         return True
#     elif is_const(expr):
#         return False
#     else:
#         for child in expr.children():
#             if contains_logical_operators(child):
#                 return True
#     return False

def array_check_for_match(array1, array2):
    set1 = set(array1)
    set2 = set(array2)
    
    # Check if there's any intersection between the sets
    if set1.intersection(set2):
        return True  # Match found
    else:
        return False  # No match found

# def convert_SMTlib_to_Z3Solver(smtlib_formula, index):
#     # Split the formula into parts
#     parts = smtlib_formula.strip().split()
#     for part in parts:
#         print("part " +part)
#     # Extract the operator and operands
#     operator = parts[0]
#     # print('line '+str(index)+" operator " +operator)
#     operands = parts[1:]
#     # for operand in operands:
#     #     print('line '+str(index)+" operand " +operand)
#     # Convert operator and operands to Python/Z3 format
#     python_formula = ""
#     if operator == ">":
#         python_formula = f"{operands[0]} + {operands[1]} < {operands[2]}"
#     elif operator == "<":
#         python_formula = f"{operands[0]} + {operands[1]} > {operands[2]}"
#     # Add support for other operators as needed...

#     return python_formula

def is_number(num):
    if is_int_value(num):
        return True
    elif is_rational_value(num):
        return True
    else:
        return False
    
def is_comperison_operator(op):
    if is_lt(op): #<
        return True
    if is_gt(op): #>
        return True
    if is_le(op): #<=
        return True
    if is_ge(op): #>=
        return True
    if is_eq(op): #==
        return True
    else:
        return False
    
    
def is_arithmetic_operator(op):
    if is_add(op): #+
        return True 
    if is_sub(op): #-
        return True
    if is_mul(op): #*
        return True
    if (is_div(op) or is_idiv(op) ): #/
        return True
    if is_mod(op): #%
        return True
    else:
        return False

# comparison_operators = ['==', '>', '<', '>=', '<=']
def replace_comparison_decl(expr, new_op):
    # Ensure the expression is a comparison operation
    if not is_expr(expr) or not expr.decl().arity() == 2 or not expr.decl().kind() in [Z3_OP_GT, Z3_OP_LT, Z3_OP_GE, Z3_OP_LE, Z3_OP_EQ]:
        raise ValueError("Expression is not a binary comparison operation")
    
    # Extract operands
    lhs, rhs = expr.children()
    
    # Apply the new operator
    if new_op == "==":
        return lhs == rhs
    elif new_op == ">":
        return lhs > rhs
    elif new_op == "<":
        return lhs < rhs
    elif new_op == ">=":
        return lhs >= rhs
    elif new_op == "<=":
        return lhs <= rhs
    else:
        raise ValueError("Unsupported operator")

# arithmetic_operators = ['+', '-', '*', '/', '%']
def replace_arithmetic_decl(expr, new_op):
    # Ensure the expression is a arithmetic operation
    if not is_expr(expr) or not expr.decl().arity() == 2 or not expr.decl().kind() in [Z3_OP_ADD, Z3_OP_SUB, Z3_OP_MUL, Z3_OP_DIV, Z3_OP_IDIV ]: #arity is number of parameters
        raise ValueError("Expression is not a binary Arithmetic operation")
    
    # Extract operands
    lhs, rhs = expr.children()
    # print("lhs is ",type(lhs))
    # print("rhs is ",type(rhs))    
    # Apply the new operator
    if new_op == "+":
        return lhs + rhs
    elif new_op == "-":
        return lhs - rhs
    elif new_op == "*":
        return lhs * rhs
    elif new_op == "/":
        return lhs / rhs
    # elif new_op == "%":
    #     return lhs % rhs
    else:
        raise ValueError("Unsupported operator")

    
    
def extract_constants_and_assertions_with_datatypes(formula_string):
    constants = {}
    assertions = []
    lines = formula_string.split('\n')
    for line in lines:
        if line.startswith('(declare-const'):
            parts = line.split()
            constant = parts[1]
            datatype = parts[2]
            constants[constant] = datatype[:-1]  # Remove the closing bracket
        elif line.startswith('(declare-fun'):
            parts = line.split()
            constant = parts[1]
            datatype = parts[3]
            constants[constant] = datatype[:-1]  # Remove the closing bracket
        elif line.startswith('(assert'):
            assertions.append(line)
            # assertions.append(line[8:-1])
    return constants, assertions   

#     return constants, assertions
# print works only on Development mode
def print_d(*args, **kwargs):
    if dev:
        print(*args, **kwargs)

# print work only on Production mode 
def print_p(*args, **kwargs):
    if dev == False:
        print(*args, **kwargs)
        

