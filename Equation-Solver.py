import os
import time
p_factors = []
q_factors = []

global factors
factors = []

global possible_roots_list
possible_roots_list = []

global roots_list
roots_list = []

global coefficients
coefficients = []

global signs
signs = []

coeff = []

actual_roots = []

def IsInt(num):
    rounded_num = int(num)
    if rounded_num - num == 0:       
        return True
    else:
        return False


start = 1

def factor_num(num):
    global start
    start = 1
    # print(num)
    absolute_num = abs(num)
    # print(absolute_num)
    if absolute_num == 0:
        print("Factor: Number entered 0")
    elif absolute_num == 1:
        factors.append(absolute_num)
    else:
        for i in range (1, absolute_num+1):
            if IsInt(absolute_num/i):
                factors.append(i)
    #print(factors)


def list_append(transfer_list, og_list):
    for each in og_list:
        transfer_list.append(each)
    #print(transfer_list)


def get_factors_q(q):
    global factors
    
    factor_num(q)
    list_append(q_factors, factors)
    factors = []


    # print(q_factors)
    # print(p_factors)

def get_factors_p(p):
    global factors
    
    factor_num(p)
    list_append(p_factors, factors)
    factors = []


    # print(q_factors)
    # print(p_factors)

def possible_roots(q, p):
    global possible_roots_list
    possible_factor = 0
    get_factors_q(q)
    get_factors_p(p)
    for p in p_factors:
        for q in q_factors:
            possible_factor = p/q    
            if possible_factor not in possible_roots_list:
                possible_roots_list.append(possible_factor)
                possible_roots_list.append(possible_factor * -1)
    print(possible_roots_list)
    




    
#possible_roots(2, 12)

#6x^4+5^3-2x^2+4x-1



def proccess_inputs(equation):
    global coefficients
    indices = []
    start_index = 0
    index_equation = equation
    plus_num = 3
    redo = False
    zero_coeff_sign = "+"
    equation = equation + "x^0"
    to_not_break = True
    

    index_equation = index_equation.replace(equation[0:equation.index("x^")+2], "")

    if "+" in index_equation:
        if "-" in index_equation:
            if index_equation.index("+") < index_equation.index("-"):
                sign_look_for = "+"
            elif index_equation.index("-") < index_equation.index("+"):
                sign_look_for = "-"
        else:
            sign_look_for = "+"
    else:
        sign_look_for = "-"
        
    
    degree = index_equation[0:index_equation.index(sign_look_for)]
    #print(degree)

    sign_look_for = "plus"
    if "x+" in equation:

        equation = equation.replace("x+", "x^1+")

    if "x-" in equation:
        equation = equation.replace("x-", "x^1-")

    if equation[0] == "x":
        equation = equation.replace("x", "1x", 1) 
    
    if "-x" in equation:
        equation = equation.replace("-x", "-1x")
    if "+x" in equation:
        equation = equation.replace("+x", "+1x")

    zero_coeff_equation = equation

    while True:
        index = equation.find("x^", start_index)
        if index == -1:
            break
        indices.append("x^")
        start_index = index + 1
    print(indices) 

    old_exp = int(degree) + 1
    print(equation, "equation")

    for each in indices:
        zero_coeff_equation = equation
        print(coefficients, "coefficients")
        old_exp -= 1
        print(zero_coeff_equation, "zero coeff equ before")
        if redo == False:
            if "x^" in zero_coeff_equation:
                zero_coeff_equation = zero_coeff_equation.replace(zero_coeff_equation[0:zero_coeff_equation.index("^")+1], "") # here is teh sport
                #print("x^ un zce")
                #print(equation[0:zero_coeff_equation.index("^")+1], "replacement")
                
            print(zero_coeff_equation, "zero coeff equ after")

            if "+" not in zero_coeff_equation and "-" not in zero_coeff_equation[1:]:
                print("we are at the end.       ")
                print(zero_coeff_equation)
                print(old_exp)
                while old_exp >= 1:
                    coefficients.append(0)
                    old_exp -= 1            
                print(zero_coeff_equation, "ZERO COEFF EQUATION")
                #coefficients.append(equation) #should this be equation or zero_coeff_equation
                print(equation)
                print("ihihihouhrfoeirfwefwew")
                print(coefficients)
                if old_exp == 0:
                    coefficients.append(equation[0:equation.index("x")])
                    to_not_break = False
            else:
                if "+" in zero_coeff_equation and "-" in zero_coeff_equation:
                    if zero_coeff_equation.index("+") < zero_coeff_equation.index("-"):
                        zero_coeff_sign = "+"
                    else:
                        zero_coeff_sign = "-"
                elif "+" in zero_coeff_equation and "-" not in zero_coeff_equation:
                    zero_coeff_sign = "+"
                else:
                    zero_coeff_sign = "-"
                print(zero_coeff_sign, "zce sign")

                print()
                print(zero_coeff_equation[0:zero_coeff_equation.index(zero_coeff_sign)])
                print(old_exp)
                print()
                print(zero_coeff_equation, "right before the error")
                
                if zero_coeff_equation[0:zero_coeff_equation.index(zero_coeff_sign)] == str(old_exp):
                    zero_coeff_equation = zero_coeff_equation.replace(equation[0:zero_coeff_equation.index(zero_coeff_sign)], "", 1)
                    print(zero_coeff_equation)
                    
                    if "+" in equation:
                        if equation.index("+") == 0:
                            equation = equation[1:len(equation)+1]
                            plus_num = 3
                        else:
                            plus_num = 2
                    else:
                        plus_num = 2
                    print()
                    print()
                    print(equation[0:equation.index("x^")], "equatoin apppended")
                    coefficients.append(equation[0:equation.index("x^")])
                    equation = equation.replace(equation[0:equation.index("x^") + len(str(degree)) + plus_num], "")
                else:
                    coefficients.append(0)
                    print("we went here")
                    redo = False
                    
            

        print(equation, "equation")
    
    print(equation, "this is the coef.append(eq)")
    if to_not_break == True:
        coefficients.append(equation[0:equation.index("x")])

    new_item = 0
    new_item = coefficients[len(coefficients) - 1]
    #print(new_item)
    new_item = new_item.replace("+", "")
    #print(new_item)
    #print(coefficients)
    del coefficients[-1]
    #print(coefficients)

    coefficients.append(new_item)

    #print(coefficients)
    #print("coefficients")
    #print(coefficients, "coeff 1")
    coefficients = [int(s) for s in coefficients]
    #os.system("clear")

    print(coefficients, "is this process inputs")

#--------------
    

#proccess_inputs("5x^3-2x-4")
#proccess_inputs("3x^4+2")
#proccess_inputs("x^4-x^3-22x^2+16x+96")
#print(coefficients, "coeffs")

def real_roots(pr):
    global actual_roots
    total = 0
    print(coefficients, "hello???")
    degree = len(coefficients) - 1
    old_deg = degree
    print(pr, "possible roots list")
    for a in pr:
        

        print()
        print()
        print()
        print()
        print()
        print(a, "a")

        for each in coefficients:

            print(each, "coeffs")
            b = each*(a**(degree))
            print(degree, "degree")
            print((a**degree), "a^deg")
            print(b, " b")
            total = total + b
            print(total, " total")
            degree -= 1
        if total == 0:
            actual_roots.append(a)
            print("appended")
        
        degree = old_deg
        total = 0
        print()
        print()
        print()
        print()
        print()
        print(total, " total")
    os.system("clear")

    print(actual_roots)

    
    #print(degree)

# possible_roots(1, 96)
# #print(possible_roots_list)
# real_roots(possible_roots_list)
    

print(coefficients)

def solver(equation):
    global coefficients
    proccess_inputs(equation)
    possible_roots(coefficients[0], coefficients[len(coefficients) - 1])
    real_roots(possible_roots_list)



   
#solver("x^4-x^3-22x^2+16x+96")

solver("2x^4+7x^3-24x^2-45x")
# proccess_inputs("2x^4+7x^3-24x^2-45x")

