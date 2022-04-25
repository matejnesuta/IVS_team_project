from . import math_funcs, exp_parse as prdel
#from . import exp_parse


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

def is_neg_oprnd(oprnd):
    return True if oprnd[0] == '(' else False


"""
CLEAN NEGATIVE OPERAND
brief: Removes brackets from negative operand
param: str oprnd
return str cln_oprnd
"""
def cln_neg_oprnd(oprnd):
    return oprnd[1:len(oprnd) - 1]


def to_neg_oprnd(oprnd):
    return f"({oprnd})"


#TODO: uhlednejsi reseni 
"""
UPDATE EXPRESSION
brief: Replaces operataion with its result
param: str exp, dict{op}, int res
return: str up_exp
"""
def update_exp(exp, op, res):
    cur_oprtr = op[list(op)[0]]
    if cur_oprtr in '+-/*^':
        cur_op_str = f"{op['l_op']}{cur_oprtr}{op['r_op']}"

    if cur_oprtr == '!':
        cur_op_str = f"{op['l_op']}{cur_oprtr}"

    if cur_oprtr == 'nrt' or cur_oprtr == 'log':
        cur_op_str = f"{cur_oprtr}({op['l_op']},{op['r_op']})"

    up_exp = exp.replace(cur_op_str, str(res))
    return up_exp


"""
CALCULATION OUTPUT
brief: 
param: list[ops]
return: float output
"""
def calc_output(exp):
    ops = exp_parse(exp)
    n_ops = len(ops)
    res = exp
    for i in range(n_ops):
        #sorting the list of operations by priority
        ops_pr_sorted = sorted(ops, reverse=True, key=lambda op: op['pr'])
        cur_op = ops_pr_sorted[0]
        cur_oprtr = cur_op[list(cur_op)[0]]
        l_op = cur_op[list(cur_op)[1]]
        r_op = cur_op[list(cur_op)[2]]

        if is_neg_oprnd(l_op):
            l_op = cln_neg_oprnd(l_op)

        #factorial r_op is None
        if r_op != None and is_neg_oprnd(r_op):
            r_op = cln_neg_oprnd(r_op)

        #maybe seperate func?
        #TODO:validation
        if '.' in l_op:
            l_op = str_to_float(l_op)
        else:
            l_op = str_to_int(l_op)

        #factorial r_op is None
        if r_op != None:
            if '.' in r_op:
                r_op = str_to_float(r_op)
            else:
                r_op = str_to_int(r_op)

        match cur_oprtr:
            case '+':
                res = math_funcs.add(l_op, r_op) 

            case '-':
                res = math_funcs.sub(l_op, r_op)
                
            case '*':
                res = math_funcs.mul(l_op, r_op)
                
            case '/':
                res = math_funcs.div(l_op, r_op)
                
            case '^':
                res = math_funcs.pow_n(l_op, r_op)
                
            case '!':
                res = math_funcs.factorial(l_op)
                
            case 'nrt':
                res = math_funcs.nth_root(l_op, r_op)
                
            case 'log':
                res = math_funcs.logx(l_op, r_op)
        #TODO: format result
        res_to_exp = f"({res})" if res < 0 else res
        exp = update_exp(exp, cur_op, res_to_exp)
        ops = exp_parse(exp)
        print(res)
        print(exp)
        
    return res