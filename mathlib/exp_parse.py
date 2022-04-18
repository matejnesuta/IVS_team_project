#Set with all operators
oprtrs_set = {"+", "-", "*", "/", "^", "!", "nthrt", "log"}


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
param: str exp
return: dict {index: oprtr}
"""
def find_oprtrs(exp):
    found_oprtrs = {}
    f_p = 0
    op_i = 0
    for op in oprtrs_set:
        while exp.find(op, f_p) != -1:
            op_i = exp.find(op, f_p)
            found_oprtrs[op_i] = op
            f_p = op_i + 1
        f_p = 0
    return found_oprtrs


"""
FIND OPERANDS OF THE EXPRESSION
brief: Looking for opearnds of the operation
param: str exp, int op_i, str op
return: list[l_oprnd, r_oprnd] 
"""
def find_oprnds(exp, op_i, op):
    oprnds = []
    #some kind of a switch
    match op:
        case '!':
            print('!')
        case 'nthrt':
            print('rt')
        case 'log':
            print('log')
        #default case
        #case _:

    l_part = exp[0:op_i]
    r_part = exp[op_i + 1:]
    oprnds.append(l_part)
    oprnds.append(r_part)
    return oprnds


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
def exp_parse(exp):
    #validation part
    if not bracket_pair_check:
        print("Missing bracket")
        return False
    

    exp_oprts = find_oprtrs(exp, oprtrs_set)
    for op_i in exp_oprts:
        print(find_oprnds(exp, op_i, exp_oprts[op_i]))
    return