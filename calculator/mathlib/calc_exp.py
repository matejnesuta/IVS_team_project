import math_funcs
from exp_parse import parse_exp
from exp_parse import oprtrs_set


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

#comm
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


"""
TO NEGATIVE OPERAND
brief: Adds brackets to negative operand
param: str oprnd
return str neg_oprnd
"""
def to_neg_oprnd(oprnd):
    return f"({oprnd})"


"""
NEGATIVE FIRST OPERAND
brief: Putting first operand into brackets, if it's negative
param: str exp, set{oprtrs}
return: str exp
"""
def neg_first_oprnd(exp, oprtr_set):
    cut_sign = exp[1:]
    ops = {}
    for op in oprtr_set:
        if cut_sign.find(op) > -1:
            ops[op] = cut_sign.find(op)
    #case of sole negative number, eg. -2
    if len(ops) == 0:
        return f"({exp})"
    
    next_op = min(ops.values()) + 1
    if next_op == 1:
        return f"(-1)*{cut_sign}"
    neg_start = exp[:next_op]
    cut_exp = exp[next_op:]
    return f"({neg_start}){cut_exp}"


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
FORMAT OUTPUT
brief: Formating output - for instance, converting .0 float to int
param: str out
return str f_out
"""
def format_output(out):
    if type(out) is float:
        if int(out) == out:
            return int(out)
    return out


"""
CALCULATION OUTPUT
brief: Calculates the expression 
param: list[ops]
return: float res / False if err
"""
def calc_output(exp):
    if exp[0] == '-':
        exp = neg_first_oprnd(exp, oprtrs_set)
    ops = parse_exp(exp)
    if ops is False:
        return False
    res = exp
    while len(ops) != 0:
        if ops is False:
            return False
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

        if l_op is False or r_op is False:
            return False

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
        if res is False:
            return False
        #TODO: .0 float to int, clean negative number, etc.
        res_to_exp = f"({res})" if res < 0 else res
        exp = update_exp(exp, cur_op, res_to_exp)
        ops = parse_exp(exp)
    res = format_output(res)  
    return res

e ='-3/(-1)'
print(calc_output(e))