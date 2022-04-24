#Set with all operators
oprtrs_set = {'+', '-', '*', '/', '^', '!', 'nrt', 'log'}

#Operators priority
oprtrs_pr = {
    'nrt': 3,
    'log': 3,
    '!': 3,
    '^': 2,
    '*': 1,
    '/': 1,
    '+': 0,
    '-': 0
}


#FIXME: handling negative numbers


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
FIND NEXT OPERATOR
brief: Looking for the closest operator
param: str exp, int i, bool rev
return int next_op
"""
def find_next_oprtr(exp, i, rev):
    found_op = {}
    #operator offset - number of characters between i and the next operator
    op_off = len(exp)
    next_op_i = -1
    next_op = ''
    for op in oprtrs_set:
        if rev:
            found_op[op] = exp.find(op, 0, i)
        else:
            found_op[op] = exp.find(op, i + 1)

    for v in found_op:
        if rev:
            if found_op[v] != -1 and (i - found_op[v]) < op_off:
                op_off = i - found_op[v]
                next_op_i = found_op[v]
                next_op = v
        else:
            if found_op[v] != -1 and (found_op[v] - i) < op_off:
                op_off = found_op[v] - i
                next_op_i = found_op[v]
                next_op = v
    return {next_op: next_op_i}


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
    #sorting dict of operators by keys(index)
    oprtrs_sorted = {k:v for k,v in sorted(found_oprtrs.items())}
    return oprtrs_sorted


"""
FIND OPERANDS OF THE EXPRESSION
brief: Looking for opearnds of the operation
param: str exp, int op_i, str op
return: dict{l_op: l_oprnd, r_op: r_oprnd} 
"""
def find_oprnds(exp, op_i, op):
    oprnds = {}
    match op:
        case '!':
            n_op_d = find_next_oprtr(exp, op_i, True)
            n_op = list(n_op_d)[0]
            if n_op == '':
                l_oprnd = exp[:op_i]
                oprnds['l_op'] = l_oprnd
                oprnds['r_op'] = None
            else:
                l_oprnd = exp[n_op_d[n_op] + 1:op_i]
                oprnds['l_op'] = l_oprnd
                oprnds['r_op'] = None
                
        case 'nthrt':
            pass

        case 'log':
            pass

        case _:
            l_oprtr_d = find_next_oprtr(exp, op_i, True) 
            l_oprtr = list(l_oprtr_d)[0]
            r_oprtr_d = find_next_oprtr(exp, op_i, False) 
            r_oprtr = list(r_oprtr_d)[0]
            if l_oprtr == '':
                l_oprnd = exp[:op_i]
                oprnds['l_op'] = l_oprnd
            else:
                l_oprnd = exp[l_oprtr_d[l_oprtr] + 1:op_i]
                oprnds['l_op'] = l_oprnd


            if r_oprtr == '':
                r_oprnd = exp[op_i + 1:]
                oprnds['r_op'] = r_oprnd
            else:
                r_oprnd = exp[op_i + 1:r_oprtr_d[r_oprtr]]
                oprnds['r_op'] = r_oprnd
                pass

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
list[{i: oprtr, l_op: l_oprnd, r_op: r_oprnd} pr: n}]
"""
def exp_parse(exp):
    oprtrs = find_oprtrs(exp)
    #dict of operation - operator, operands and priority of calculation
    op_dict = {}
    #list of dict{operation}
    ops_list = []
    for oprtr in oprtrs:
        op_dict[oprtr] = oprtrs[oprtr] 
        op_dict.update(find_oprnds(exp, oprtr, oprtrs[oprtr]))
        op_dict['pr'] = oprtrs_pr[oprtrs[oprtr]]
        ops_list.append(op_dict)
        op_dict = {}
    return ops_list

e = "2!+3*5^2"
print(exp_parse(e))