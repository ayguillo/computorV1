def abs(nb):
    if nb < 0 :
        return (nb * (-1))
    else :
        return nb

def sqrt(nb):
    x = 1
    y = 0.5 * (x + nb)
    while abs(y-x) > 0.00000001:
        x = y
        y = 0.5 * (x + nb / x)
    return(y)

def sign(nb):
    if nb < 0:
        return('-')
    return('+')

def sign_without_plus(nb):
    if nb < 0:
        return('-')
    return('')

def append_tab(tab, i):
    while (len(tab) <= i):
        tab.append(0)
    return(tab)
