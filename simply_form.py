from utils import sqrt

def found_pgcd(num, denum):
    if num < 0:
        num = -num
    if denum < 0:
        denum = -denum
    if num == 0:
        return(None)
    while (denum % num):
        pgcd = denum % num
        denum = num
        num = pgcd
        if num == 0:
            return(None)
    return (num)

def irreductible(num, denum):
    pgcd = found_pgcd(num, denum)
    if pgcd == None :
        return(None)
    num_p = num / pgcd
    denum_p = denum / pgcd
    if num_p.is_integer() and denum_p.is_integer():
        num_p = int(num_p)
        denum_p = int(denum_p)
        if denum_p != 1 and len(str(num_p)) <= 2 and len(str(denum_p)) <= 2:
            if denum_p < 0 and num_p > 0 or denum_p < 0 and num_p < 0:
                num_p, denum_p = -num_p, - denum_p
            return("{}/{}".format(int(num_p), int(denum_p)))
    return(None)

def get_fraction(b, a, delta, sign):
    if sign == '-':
        num = -b - sqrt(delta)
    else :
        num = -b + sqrt(delta)
    denum = 2 * a
    return(irreductible(num, denum))

def get_complex(delta, b, a):
    str_min, str_plus = '', ''
    min, plus, denum = -sqrt(-delta), sqrt(-delta), 2*a
    complex_min, complex_plus, real = None, None, None
    if denum.is_integer():
        if min.is_integer():
            complex_min = irreductible(min, denum)
        if plus.is_integer():
            complex_plus = irreductible(plus, denum)
        if b.is_integer():
            real = irreductible(b, denum)
        if complex_min == '':
            complex_min = None
        if complex_plus == '':
            complex_plus = None
        if real == '':
            real = None
        if complex_min != None or real != None :
            if complex_min != None :
                str_min += '{}i + '.format(complex_min)
                if real != None:
                    str_min += real
                else :
                    str_min += str(b / (2 * a))
            elif real != None :
                str_min = '{}i + {}'.format(min / (2 * a), real)
        if complex_plus != None:
            str_plus += '{}i + '.format(complex_plus)
            if real != None:
                str_plus += real
            else :
                str_plus += str(b / (2 * a))
        elif real != None :
            str_plus = '{}i + {}'.format(plus / (2 * a), real)
    return(str_plus.strip(), str_min.strip())
