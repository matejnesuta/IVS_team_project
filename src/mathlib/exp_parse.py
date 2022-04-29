#Set of all operators
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
param: str exp, int br_i
return: int end_br_i / -1 if not found
"""
def find_comp_br(exp, br_i):
    return exp.find(')', br_i)


"""
FIND NEXT OPERATOR
brief: Looking for the closest operator
param: str exp, int i, bool rev
return int next_op_i, -1 if there is none
"""
def find_next_oprtr(oprtrs, op_i, rev):
    op_i_list = list(oprtrs)
    #next operator index in the op_i_list
    next_op_l_i = op_i_list.index(op_i)
    #checking for index out of range
    if (next_op_l_i == 0 and rev) or (next_op_l_i == len(op_i_list) - 1 and not rev):
        return -1

    #edge case of nrt or log being next to some other operator
    if not rev and (oprtrs[op_i_list[next_op_l_i + 1]] == 'log' or oprtrs[op_i_list[next_op_l_i + 1]] == 'nrt'):
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
return: dict{index: oprtr}
"""
def find_oprtrs(exp):
    found_oprtrs = {}
    #position of the found operator
    f_p = 0
    #index of the found operator
    op_i = 0
    for op in oprtrs_set:
        #f_p is used in find method as a starting position
        while exp.find(op, f_p) != -1:
            op_i = exp.find(op, f_p)
            #excluding minus signs of negative numbers
            if (op == '-' and is_neg_num(exp, op_i)):
                f_p = op_i + 1
                continue
            found_oprtrs[op_i] = op
            f_p = op_i + 1
        f_p = 0
    #sorting dict of operators by keys(indexes)
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
            #the offset stands for len(nrt)
            if exp[op_i + 3] != '(':
                return False
            else:
                end_br = find_comp_br(exp, op_i + 3)
                #params parsing
                params = exp[op_i + 4:end_br] 
                ops = params.split(',')
                oprnds['l_op'] = ops[0]
                oprnds['r_op'] = ops[1]

        case 'log':
            #arguments of logarithm must be in brackets 
            #the offset stands for len(log)
            if exp[op_i + 3] != '(':
                return False
            else:
                end_br = find_comp_br(exp, op_i + 3)
                #params parsing
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
        print('Incorrect use of brackets')
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
        
        if not check_empty_oprnds(op_dict):
            return False

        ops_list.append(op_dict)
        op_dict = {}
    return ops_list