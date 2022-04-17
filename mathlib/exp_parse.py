#Set with all operators
oprts_set = {"+", "-", "*", "/", "^", "!", "nthrt", "log"}


"""
STRING TO INT
brief: Converting string to integer (if possible)
param: str s
return: int(str)
"""
def str_to_int(s):
    try:
        res = int(s)
    except ValueError:
        print("Argument is not an integer")
        return False
    return res


"""
STRING TO INT
brief: Converting string to float (if possible)
param: str s
return: int(s)
"""
def str_to_float(s):
    try:
        res = float(s)
    except ValueError:
        print("Argument is not a number")
        return False
    return res


#TODO: probably fine for now, but it doesnt check the content of the brackets
"""
CHECKING PAIRS OF BRACKETS
brief: Checking if there is always a complementary bracket
param: str exp
return True / False
"""
def bracket_pair_check(exp):
    n_left_br = 0
    n_right_br = 0
    for c in exp:
        if c == "(":
            n_left_br += 1
        if c == ")":
            n_right_br += 1
        if n_right_br > n_left_br:
            return False
    return True if n_left_br == n_right_br else False


"""
FIND OPERATORS IN EXPRESSION
brief: Looking for operators in the expression 
param: str exp, set {oprts}
return: dict {index: oprt}
"""
def find_oprts(exp, oprts):
    found_oprts = {}
    i = 0
    for i, c in enumerate(exp):
        for op in oprts:
            if c == op:
                found_oprts[i] = op
    return found_oprts


"""
FIND LEFT OPERAND OF THE EXPRESSION
brief: Looking for the left opearnd of the operation
param: str exp, 
return: str left_oprnd 
"""
def find_left_oprnd(exp, op):

    return


"""
FIND RIGHT OPERAND OF THE EXPRESSION
brief: Looking for the right opearnd of the operation
param: str exp, 
return: str right_oprnd 
"""
def find_right_oprnd(exp, op):

    return


"""
VALIDATE OPERANDS
brief: 
param: str oprtr, list [oprnds]
return: True / False
"""
def vld_oprnds():
    return


"""
EXPRESSION PARSER
brief: Parsing the whole expression and dividing it to the seperate operations
param: str exp, dict {oprtrs}
return: dict{} of elementary operations and their order of execution
"""
def exp_parse(exp, ops):
    #validation part
    if not bracket_pair_check:
        print("Missing bracket")
        return False
    
    for key in ops.keys(): 
        print(key)
    return