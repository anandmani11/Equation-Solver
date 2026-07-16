import os
import time
import re


def IsInt(num) -> bool:
    rounded_num = int(num)
    if rounded_num - num == 0:       
        return True
    else:
        return False

def factor_num(num) -> list:
    absolute_num = abs(num)
    factors = []
    if absolute_num == 0:
        print("Factor: Number entered 0")
    elif absolute_num == 1:
        factors.append(absolute_num)
    else:
        for i in range (1, absolute_num+1):
            if IsInt(absolute_num/i):
                factors.append(i)
    return factors


def get_factors_q(q):
    factors = factor_num(q)
    return factors

def get_factors_p(p):
    factors = factor_num(p)
    return factors


def possible_roots(q, p):
    possible_roots_list = []
    possible_factor = 0
    q_factors = get_factors_q(q)
    p_factors = get_factors_p(p)
    for q_val in q_factors:
        for p_val in p_factors:
            possible_factor = p_val / q_val    
            if possible_factor not in possible_roots_list:
                possible_roots_list.extend([possible_factor, possible_factor * -1])
    return possible_roots_list 


def real_roots(possible_roots, coefficients):
    real_roots = []
    total = 0
    current_degree = len(coefficients) - 1
    original_degree = current_degree
    for possible_root in possible_roots:
        for each in coefficients:
            b = each*possible_root**current_degree
            total += b
            current_degree -= 1
        if abs(total) < 1e-9:
            if possible_root not in real_roots:
                real_roots.append(int(possible_root) if IsInt(possible_root) else possible_root)         
        current_degree = original_degree
        total = 0
    return real_roots

   

def solver(equation):
    coefficients = proccess_inputs(equation.replace(" ", ""))
    print(real_roots(possible_roots(coefficients[0], coefficients[-1]), coefficients))

    
def proccess_inputs(equation):
    chunked_polynomial = create_missing_terms(fix_last_chunks(split_equation(equation)))
    coefficients = get_coeffs(chunked_polynomial)
    return coefficients


def split_equation(equation):
    chunks = []
    chunks = re.split(r'(?=[-+])', equation)
    for i in range(len(chunks)):
        chunks[i] = chunks[i].replace("+", "")
    return [i for i in chunks if i != ""]

def fix_last_chunks(chunks):
    length = len(chunks) - 1
    if "^"  not in chunks[length - 1]:
        chunks[length - 1] = chunks[length - 1] + "^1"
    if "^" not in chunks[length]:
        chunks[length] = chunks[length] + "x^0"
    return chunks

def create_missing_terms(chunks):
    degree = get_degree(chunks[0])
    zero_polynomial = make_zero_polynomial(degree)
    full_polynomial = list(zero_polynomial)
    for each in chunks:
        full_polynomial[degree - get_degree(each)] = each
    return full_polynomial

def make_zero_polynomial(degree):
    zero_polynomial = []
    for i in range(degree, -1, -1):
        zero_polynomial.append("0x^" + str(i))
    return zero_polynomial

def get_degree(chunk):
    degree = chunk[chunk.index("^") + 1:]
    return int(degree)

def get_coeffs(chunks):
    coefficients = []
    for each in chunks:
        match = re.match(r'([+-]?\d*)x', each)
        if match:
            coeff_str = match.group(1)
            if coeff_str in ('', '+'):
                coefficients.append(1)
            elif coeff_str == '-':
                coefficients.append(-1)
            else:
                coefficients.append(int(coeff_str))
    return coefficients

# (x+3)(x-2)(x+4)(2x-5)(7x+2)
solver("14x^5 + 39x^4 - 193x^3 - 324x^2 + 764x + 240")