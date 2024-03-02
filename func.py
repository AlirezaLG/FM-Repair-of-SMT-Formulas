from z3 import * 

def value_to_decimal_or_int(value):
    if value.is_rational():
        return float(value.as_decimal(10))  # Convert fraction to decimal
    else:
        return int(value)
