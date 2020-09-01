import re
from utils import append_tab

def epur_only_x(epur, maxi, tab, sign='+'):
    if epur != '0' or epur != '':
        reg = "(((-|\+)? {0,}\d+(\.\d+)?) ?\*? {0,}x(.|))"
        search_x = re.findall(reg, epur)
        for is_x in search_x:
            if is_x[4] != ' ' and is_x[4] != '+' and is_x[4] != '-' and is_x[4] != '' and is_x[4] != '=':
                continue
            ad = float(re.sub(r"\s+", "", is_x[1], flags=re.UNICODE))
            if sign == '-':
                ad = -ad
            try :
                old = tab[1]
                tab[1] = (old + ad)
            except :
                tab = append_tab(tab, 1)
                tab[1] = ad
            if maxi < 1:
                maxi = 1
            epur = (epur.replace(is_x[0], '')).strip()
    return(epur.strip(), maxi, tab)

def epur_only_pow(epur, maxi, tab, sign='+'):
    if epur != '0' or epur != '':
        reg = "((-|\+)? {0,}x(\^(\d+))?(.|))"
        search_x = re.findall(reg, epur)
        for is_x in search_x :
            if is_x[4] != ' ' and is_x[4] != '+' and is_x[4] != '-' and is_x[4] != '' and is_x[4] != '=':
                continue
            if is_x[1] == '-':
                sign_x = '-'
            else :
                sign_x = '+'
            if is_x[3] == '':
                pow = 1
            else :
                try :
                    pow = int(is_x[3])
                except ValueError :
                    continue
            if sign_x == '-':
                ad = -1.0
            else :
                ad = 1.0
            if sign == '-':
                ad = -ad
            try :
                old = tab[pow]
                tab[pow] = (old + ad)
            except :
                tab = append_tab(tab, pow)
                tab[pow] = ad
            if maxi < pow:
                maxi = pow
            epur = (epur.replace(is_x[0], '')).strip()
    return(epur.strip(), maxi, tab)

def epur_only_int(epur, tab, sign='+'):
    if epur != '0' and epur != '':
        reg = "((-|\+)? {0,}\d+(\.\d+)?)"
        search_int = re.findall(reg, epur)
        for is_int in search_int:
            ad = float(re.sub(r"\s+", "", is_int[0], flags=re.UNICODE))
            if sign == '-':
                ad = -ad
            try :
                old = tab[0]
                tab[0] = (old + ad)
            except :
                tab = append_tab(tab, 0)
                tab[0] = ad
            epur = (epur.replace(is_int[0], '')).strip()
    return(epur.strip(), tab)

def treatment_str(epur, maxi, tab, sign='+'):
    epur, maxi, tab = epur_only_x(epur, maxi, tab, sign)
    epur, maxi, tab = epur_only_pow(epur, maxi, tab, sign)
    epur, tab = epur_only_int(epur, tab, sign)
    return(epur, maxi, tab)

def natural_language(tab, before, after, maxi):
    if before != '0':
        before, maxi, tab = treatment_str(before, maxi, tab)
    else :
        before = ''
    if after != '0' :
        after, maxi, tab = treatment_str(after, maxi, tab, '-')
    else :
        after = ''
    return(tab, before, after, maxi)
