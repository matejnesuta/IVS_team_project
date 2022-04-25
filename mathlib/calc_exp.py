import math_funcs
from exp_parse import exp_parse
from exp_parse import find_next_oprtr


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
UPDATE EXPRESSION
brief: Replaces operataion with its result
param: str exp, dict{op}, int res
return: str up_exp
"""
def update_exp(exp, op, res):
    cur_oprtr = op[list(op)[0]]
    cur_op_str = f"{op['l_op']}{cur_oprtr}{op['r_op']}"
    up_exp = exp.replace(cur_op_str, str(res))
    return up_exp


"""
CALCULATION OUTPUT
brief: 
param: list[ops]
return: float output
"""
def calc_output(exp):
    calc_res = 0
    ops = exp_parse(exp)
    if len(ops) == 0:
        #no more operations, returns last saved result
        #probably will be transformed to loop
        return
    #sorting the list of operations by priority
    ops_pr_sorted = sorted(ops, reverse=True, key=lambda op: op['pr'])
    cur_op = ops_pr_sorted[0]
    cur_oprtr = cur_op[list(cur_op)[0]]
    l_op = cur_op[list(cur_op)[1]]
    r_op = cur_op[list(cur_op)[2]]

    #maybe seperate func?
    #TODO:validation
    if '.' in l_op:
        l_op = str_to_float(l_op)
    else:
        l_op = str_to_int(l_op)

    if '.' in r_op:
        r_op = str_to_float(r_op)
    else:
        r_op = str_to_int(r_op)

    match cur_oprtr:
        case '+':
            cur_res = math_funcs.add(l_op, r_op) 

        case '-':
            cur_res = math_funcs.sub(l_op, r_op)
            
        case '*':
            cur_res = math_funcs.mul(l_op, r_op)
            
        case '/':
            cur_res = math_funcs.div(l_op, r_op)
            
        case '^':
            cur_res = math_funcs.pow_n(l_op, r_op)
            
        case '!':
            cur_res = math_funcs.factorial(l_op)
            
        case 'nrt':
            cur_res = math_funcs.nth_root(l_op, r_op)
            
        case 'log':
            cur_res = math_funcs.logx(l_op, r_op)
    #TODO: format result
    calc_res += cur_res
    ops = exp_parse(update_exp(exp, cur_op, cur_res))
    
    return calc_res