
arithmetic_operators = ['+', '-', '*', '/', '%']
comparison_operators = ['==','=', '!=', '>', '<', '>=', '<=']
logical_operators = ['and', 'or', 'not']

mutation_orders = ['delete_assertion','replace_constant', 'replace_operator']

# development or production
mode = "development"
dev = True
# show print only in development mode
if mode == "development":
    dev = True
else:
    dev = False    

    
