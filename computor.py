#!/usr/bin/python3
import sys
import re
from utils import sqrt
from utils import abs
from utils import sign
from utils import append_tab

def found_x(before, after):
    maxi = 0
    tab = []
    reg = "(((-|\+)? {0,}\d+(\.\d+)?) ?\*? {0,}x\^(\d+))"
    bX = re.findall(reg, before)
    aX = re.findall(reg, after)
    for match_b in bX :
        a, b = 0, 0
        before = before.replace(match_b[0], '')
        b += float(re.sub(r"\s+", "", match_b[1], flags=re.UNICODE))
        for match_a in aX :
            if int(match_b[4]) == int(match_a[4]):
                a += float(re.sub(r"\s+", "", match_a[1], flags=re.UNICODE))
                after = after.replace(match_a[0], '')
                aX.remove(match_a)
        try :
            old = tab[int(match_b[4])]
            tab[int(match_b[4])] = (old + b) - a
        except :
            i = int(match_b[4])
            tab = append_tab(tab, i)
            tab[i] = b-a
        if int(match_b[4]) > maxi:
            maxi = int(match_b[4])
    if aX != []:
        for match in aX :
            a = 0
            a += float(re.sub(r"\s+", "", match[1], flags=re.UNICODE))
            after = after.replace(match[0], '')
            try :
                old = tab[int(match[4])]
                tab[int(match[4])] = old - a
            except :
                i = int(match[4])
                tab = append_tab(tab, i)
                tab[i] = (-a)
            if int(match[4]) > maxi:
                maxi = int(match[4])
    return(tab, maxi, before.strip(), after.strip())


def reduce_form(before, after):
    tab, maxi, before, after = found_x(before, after)
    str = ''
    first = True
    X = 0
    for i in tab :
        if i != 0:
            signX = sign(i)
            if first == True and signX == '+':
                signX = ''
            first = False
            str += '{} {} * X^{} '.format(signX, abs(i), X)
        X += 1
    if str != '' :
        str += '= 0'
    else :
        str += "0 = 0"
    if before == '' and after == '' or before == '0' and after == '' or before == '' and after == '0' or before == '0' and after == '0':
        print("Reduced form :", str.strip())
        if len(tab) < 3 :
            tab = append_tab(tab, 3)
        return(tab[0], tab[1], tab[2], maxi)
    else :
        print("Wrong format")
        return(None, None, None, None)

def aff_deg_minus(a, b, c, maxi):
    if maxi == 0:
        if c == 0:
            print("All reals are solutions")
        else :
            print("The solution is :")
            print(c)
    elif (maxi == 1):
        a, b = b, c
        if a == 0 and b != 0:
            print("No solution")
        elif a == 0 and b == 0:
            print("All reals are solutions")
        else :
            res = b / a
            if res == 0:
                res = 0
            print("The solution is :")
            print(res)

def aff_delta_negative(a, b, c, delta):
    print("Discriminant is strictly negative, the two solutions are :")
    if b < 0 :
        abs_b = abs(b)
        print("({} + i√({})) / (2 * {})".format(abs_b, abs(delta), a), end = ' => ')
        print("{}i + {}".format(sqrt(-delta) / (2 * a), b / (2 * a)))
        print("({} - i√({})) / (2 * {})".format(abs_b, abs(delta), a), end = ' => ')
        print("{}i + {}".format(-sqrt(-delta) / (2 * a), b / (2 * a)))
    else :
        print("(- {} + i√({})) / (2 * {})".format(b, abs(delta), a), end = ' => ')
        print("{}i + {}".format(sqrt(-delta) / (2 * a), b / (2 * a)))
        print("(- {} - i√({})) / (2 * {})".format(b, abs(delta), a), end = ' => ')
        print("{}i + {}".format(-sqrt(-delta) / (2 * a), b / (2 * a)))

def aff_delta_positive(a, b, c, delta):
    print("Discriminant is strictly positive, the two solutions are :")
    if b < 0 :
        abs_b = abs(b)
        print("({} - √({})) / (2 * {})".format(abs_b, delta, a), end = ' => ')
        print((-b - sqrt(delta)) / (2 * a))
        print("({} + √({})) / (2 * {})".format(abs_b, delta, a), end = ' => ')
        print((-b + sqrt(delta)) / (2 * a))
    else :
        print("(- {} - √({})) / (2 * {})".format(b, delta, a), end = ' => ')
        print((-b - sqrt(delta)) / (2 * a))
        print("(- {} + √({})) / (2 * {})".format(b, delta, a), end = ' => ')
        print((-b + sqrt(delta)) / (2 * a))

def aff_deg_second(a, b, c, maxi):
    delta = b*b - 4*a*c
    if delta > 0:
        aff_delta_positive(a, b, c, delta)
    elif delta == 0 :
        print("Discriminant is 0. The solution is :")
        print((-b) / (2 * a))
    elif delta < 0 :
        aff_delta_negative(a, b, c, delta)

def main():
    if (len(sys.argv)) != 2:
        print('''Bad argument.\nUsage : ./computor.py "[polynomial equation]"''')
    else :
        before, after = None, None
        expr = sys.argv[1]
        m = re.search("(.*) ?= ?(.*)", expr)
        if m :
            if m.group(1):
                before = m.group(1).lower().strip()
            if m.group(2):
                after = m.group(2).lower().strip()
            c, b, a, maxi = reduce_form(before, after)
            if c is not None:
                print('Polynomial degree:', maxi)
                if (maxi == 0 or maxi == 1) :
                    aff_deg_minus(a, b, c, maxi)
                elif (maxi == 2):
                    aff_deg_second(a, b, c, maxi)
                else :
                    print("The polynomial degree is stricly greater than 2, I can't solve.")
        else :
            print("Wrong format")

if __name__ == '__main__':
    main()
