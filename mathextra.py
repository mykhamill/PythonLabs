def s(m, n):
    """
    The function s is used to find the highest number it takes
    to multiply n by to get more than m. The value is then decremented by
    1 and returned giving the last integer that can be multiplied with n so
    as not to be more than m.
    e.g. s(12, 5) -> 2    #2*5 == 10 < 12, 3*5 == 15 > 12
    """
    c = 0
    t = 0
    while t <= m:
        t += n
        c += 1
    return c - 1

def strip_leading_zeros(s):
    """
    This function removes leading zeros from a string that is passed to it.
    It then returns the amended string.
    e.g. strip_leading_zeros("00001234") -> "1234"
    """
    
    while s[0] == "0":              
        s = s[1:]                   
    if s[0] == ".":                 
        s = "0" + s                 
    return s

def strip_trailing_zeros(s):
    """
    This function removes trailing zeros from a string that is passed to it.
    It then returns the amended string.
    e.g. strip_leading_zeros("12340000") -> "12340000"
    """
    while s[-1] == "0":
        s = s[:-1]
    if s[-1] == ".":
        return s + "0"
    else:
        return s

def longdiv(m, n, dp = 0, text=True):
    """
    Calculates m / n using long division and returns a string by default.
    This can calculate an arbitary number of decimal places.
    e.g. longdiv(1, 17, 10) -> '0.0588235294117647058823529411764705882352'
    """
    t = ""
    a = list(str(m))
    c = 0
    b = "0"
    dflag = False
    dpcount = 0
    while len(a) > 0:
        d = a.pop(0)
        if d == ".":
            t += d
            dflag = True
            continue
        b = str(int(b) - c*n) + d
        c = s(int(b), n)
        t += str(c)
    if not(dflag) and (dp > 0):
        t += "."
        dflag = True
    while (dpcount < dp): # or (b != "0"):
        b = str(int(b) - c*n) + "0"
        c = s(int(b), n)
        t += str(c)
        dpcount += 1
    if text and not dflag:
        return strip_leading_zeros(t)
    elif text and dflag:
        return strip_trailing_zeros(strip_leading_zeros(t))
    elif not text and dflag:
        return float(t)
    else:
        return int(t)

def recurring(s):
    """
    Shows if there is a recurring pattern of digits after the decimal point.
    Takes a number as a string and returns a list of strings.
    """
    l = [list(s)] #create a list and put the string supplied as a list of characters into the list
    l.append("")  #add a second element in the list
    l.append("")  #add a third element in the list
    if len(s) > 2: 
        l[1] += l[0].pop(0)
        while len(l[0]) > 0:
            l[2] += l[0].pop(0)
            if l[2] not in l[1]:
                l[1] += l[2]
                l[2] = ""
            else:
                if (l[1].find(l[2]) + len(l[2])) == len(l[1]):
                    if "".join(l[0][:len(l[2])]) in l[1]:
                        while len(l[0]) > 0:
                            l.append("".join(l[0][:len(l[2])]))
                            l[0] = l[0][len(l[2]):]
        return l
    else:
        return l
