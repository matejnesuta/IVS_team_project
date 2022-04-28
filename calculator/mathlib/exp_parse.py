from cmath import exp


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


#TODO: works for now, but primitive
"""
IS A NEGATIVE NUMBER
brief: Checking if '-' stands for negative number or an operator
param: str exp, int sign_i
return: True / False
"""
def is_neg_num(exp, sign_i):
    return True if exp[sign_i - 1] == '(' else False


"""
CHECKING BRACKET PAIRS 
brief: Checks bracket pair integrity
param: str exp
return: True / False
"""
def bracket_pair_check(exp):
    n_left_br = 0
    n_right_br = 0
    for c in exp:
        if c == '(':
            if n_left_br != n_right_br:
                return False
            else:
                n_left_br += 1
        if c == ')':
            if n_left_br <= n_right_br:
                return False
            else:
                n_right_br += 1
    return True if n_left_br == n_right_br else False


"""
FIND COMPLEMENTARY BRACKET
brief: Based on the index of the bracket finds its complementary bracket
param: str exp, int first_i, bool rev
return: int sec_i
"""
def find_comp_br(exp, br_i, rev):
    n_left_br = 0
    n_right_br = 0

    #iterating through expression backwards
    if rev:
        n_right_br = 1
        for i in range(br_i - 1, -1, -1):
            if exp[i] == '(':
                n_left_br += 1
            if exp[i] == ')':
                n_right_br += 1
            if n_left_br == n_right_br:
                return i 

    else:
        n_left_br = 1
        for i in range(br_i + 1, len(exp)):
            if exp[i] == '(':
                n_left_br += 1
            if exp[i] == ')':
                n_right_br += 1
            if n_left_br == n_right_br:
                return i
    return -1

"""
FIND NEXT OPERATOR
brief: Looking for the closest operator
param: str exp, int i, bool rev
return int next_op_i, -1 if there isn't a next operator
"""
def find_next_oprtr(oprtrs, op_i, rev):
    op_i_list = list(oprtrs)
    #next operator index in the op_i_list
    next_op_l_i = op_i_list.index(op_i)
    #checking for index out of range
    if (next_op_l_i == 0 and rev) or (next_op_l_i == len(op_i_list) - 1 and not rev):
        return -1
    else:
        if rev:
            next_op_l_i -= 1
        else:
            next_op_l_i += 1
    return op_i_list[next_op_l_i]


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
            if (op == '-' and is_neg_num(exp, op_i)):
                f_p = op_i + 1
                continue
            found_oprtrs[op_i] = op
            f_p = op_i + 1
        f_p = 0
    #sorting dict of operators by keys(index)
    oprtrs_sorted = {k:v for k,v in sorted(found_oprtrs.items())}
    return oprtrs_sorted


"""
FIND OPERANDS OF THE EXPRESSION
brief: Looking for opearnds of the operation
param: str exp, int op_i, str op, dict{} oprtrs
return: dict{l_op: l_oprnd, r_op: r_oprnd} 
"""
def find_oprnds(exp, op_i, oprtrs):
    op = oprtrs[op_i]
    oprnds = {}
    match op:
        case '!':
            n_op = find_next_oprtr(oprtrs, op_i, True)
            if n_op == -1:
                l_oprnd = exp[:op_i]
                oprnds['l_op'] = l_oprnd
                oprnds['r_op'] = None
            else:
                l_oprnd = exp[n_op + 1:op_i]
                oprnds['l_op'] = l_oprnd
                oprnds['r_op'] = None
                
        case 'nrt':
            #arguments of nth root must be in brackets 
            #the offset stands for len(nthrt)
            if exp[op_i + 3] != '(':
                return False
            else:
                end_br = find_comp_br(exp, op_i + 3, False)
                params = exp[op_i + 4:end_br] 
                ops = params.split(',')
                oprnds['l_op'] = ops[0]
                oprnds['r_op'] = ops[1]

        case 'log':
            #arguments of logarithm must be in brackets 
            #the offset is stands for len(log)
            if exp[op_i + 3] != '(':
                return False
            else:
                end_br = find_comp_br(exp, op_i + 3, False)
                params = exp[op_i + 4:end_br] 
                ops = params.split(',')
                oprnds['l_op'] = ops[0]
                oprnds['r_op'] = ops[1]

        case _:
            l_oprtr = find_next_oprtr(oprtrs, op_i, True) 
            r_oprtr = find_next_oprtr(oprtrs, op_i, False) 
            if l_oprtr == -1:
                l_oprnd = exp[:op_i]
                oprnds['l_op'] = l_oprnd
            else:
                l_oprnd = exp[l_oprtr + 1:op_i]
                oprnds['l_op'] = l_oprnd

            if r_oprtr == -1:
                r_oprnd = exp[op_i + 1:]
                oprnds['r_op'] = r_oprnd
            else:
                r_oprnd = exp[op_i + 1:r_oprtr]
                oprnds['r_op'] = r_oprnd

    return oprnds


"""
CHECK EMPTY OPERANDS
brief: Checks, if operands are not empty strings
param: dict{op}
return: True if not empty / False
"""
def check_empty_oprnds(op):
    return True if op['l_op'] != '' and op['r_op'] != '' else False


"""
EXPRESSION PARSER
brief: Parsing the whole expression and dividing it to the seperate operations
param: str exp, dict {oprtrs}
return: list[{i: oprtr, l_op: l_oprnd, r_op: r_oprnd} pr: n}] / False if err

"""
def parse_exp(exp):
    if not bracket_pair_check(exp):
        print("Incorrect brackets use")
        return False
    oprtrs = find_oprtrs(exp)
    #dict of operation - operator, operands and priority of calculation
    op_dict = {}
    #list of dict{operation}
    ops_list = []
    for oprtr in oprtrs:
        op_dict[oprtr] = oprtrs[oprtr] 
        op_dict.update(find_oprnds(exp, oprtr, oprtrs))
        op_dict['pr'] = oprtrs_pr[oprtrs[oprtr]]
        #muze byt soucasti vetsi validace
        if not check_empty_oprnds(op_dict):
            return False
        ops_list.append(op_dict)
        op_dict = {}
    return ops_list