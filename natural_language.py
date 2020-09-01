import re
from utils import append_tab

def treatment_str(epur, maxi, tab, sign='+'):
    reg = "(((-|\+)? {0,}\d+(\.\d+)?) ?\*? {0,}x)"
    search_x = re.findall(reg, epur)
    for is_x in search_x:
        try :
            ad = float(re.sub(r"\s+", "", is_x[1], flags=re.UNICODE))
            if sign == '-':
                ad = -ad
            old = tab[1]
            tab[1] = (old + ad)
        except :
            ad = float(re.sub(r"\s+", "", is_x[1], flags=re.UNICODE))
            if sign == '-':
                ad = -ad
            tab = append_tab(tab, 1)
            tab[1] = ad
        if maxi < 1:
            maxi = 1
        epur = (epur.replace(is_x[0], '')).strip()
    if epur != '0' and epur != '':
        reg = "((-|\+)? {0,}\d+(\.\d+)?)"
        search_int = re.findall(reg, epur)
        for is_int in search_int:
            try :
                ad = float(re.sub(r"\s+", "", is_int[0], flags=re.UNICODE))
                if sign == '-':
                    ad = -ad
                old = tab[0]
                tab[0] = (old + ad)
            except :
                ad = float(re.sub(r"\s+", "", is_int[0], flags=re.UNICODE))
                if sign == '-':
                    ad = -ad
                tab = append_tab(tab, 0)
                tab[0] = ad
            epur = (epur.replace(is_int[0], '')).strip()
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
