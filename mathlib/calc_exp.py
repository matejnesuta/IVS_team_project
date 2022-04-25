import math_funcs
from exp_parse import exp_parse


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
STRING TO FLOAT
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


"""
CALCULATION OUTPUT
brief: 
param: list[] ops
return: float output
"""
def calc_output(exp):
    ops = exp_parse(exp)
    #sorting the list of operations by priority
    ops_pr_sorted = sorted(ops, reverse=True, key=lambda op: op['pr'])
    cur_op = ops_pr_sorted[0]
    cur_oprtr = cur_op[list(cur_op)[0]]
    cur_l_op = cur_op[list(cur_op)[1]]
    cur_r_op = cur_op[list(cur_op)[2]]
    #maybe seperate func?

    #TODO:validation
    if '.' in cur_l_op:
        cur_l_op = str_to_float(cur_l_op)
    else:
        cur_l_op = str_to_int(cur_l_op)

    if '.' in cur_r_op:
        cur_r_op = str_to_float(cur_r_op)
    else:
        cur_r_op = str_to_int(cur_r_op)

    match cur_oprtr:
        case '+':
            pass
        case '-':
            pass
        case '*':
            pass
        case '/':
            pass
        case '^':
            pass
        case '!':
            pass
        case 'nrt':
            pass
        case 'log':
            pass
    print(cur_op)
    return