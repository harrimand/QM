#Quine McCluskey Aglorithm Module

def validDontCares(dontCare, data):
    """If item in dontCare list is found in data list
    item will be removed from dontCare list."""
    for d in dontCare:
        if d in data:
            dontCare.remove(d)
    return dontCare

def decList2binList(data):
    """Take a list of integers.  Return a list of
    binary strings padded with 0s to match the size of
    the binary representation of the largest integer in
    the list."""
    binData = []
    bitsize = max(data).bit_length()
    for b in data:
        setbits = bin(b)[2:].count("1")
        bitstr = ("{:0>{}}".format(bin(b)[2:], bitsize))
        binData.append(bitstr)
        #print("\t{}\t{}".format(bitstr, setbits))
    return binData

def mkSortByNumBitsSetDict(binData):
    bDict = {}
    """Take a list of binary strings and return a dictionary sorted by
    number of bits set in the strings.  Keys indicate number of bits set
    in each of the binary strings and values are lists of binary strings"""
    bitsize = len(binData[0])
    for i in range(bitsize + 1):
        bTemp = []
        for v in binData:
           if i == v.count("1"):
                bTemp.append(v)
        if len(bTemp):
            bDict[i] = bTemp
    return bDict

def mkEssDict(inDict):
    """Take input Dictionary and return matching
    sized dictionary with all values replaced with True"""
    tmpDict = {}
    for i in inDict:
        tmpDict[i] = ([True] * len(inDict[i]))
    return tmpDict

def compBin(astr, bstr):
    """Compare strings with matching lengths containing
    0s, 1s and Xs.
    If Xs are aligned in both strings and only one
    other character is different, return a string
    containing an X where a 1 in one string
    aligns with a 0 in the other string.
    If an appropriate comparison is not found,
    return an empty string."""
    result = ""
    chgCount = 0
    for c in range(len(astr)):
        if astr[c] == bstr[c]:
            result += astr[c]
        elif astr[c] != 'X' and bstr[c] != 'X':
            result += 'X'
            chgCount += 1
        else:
            result = ""
            break
    if chgCount > 1:
        result = ""
    return result

def copyPrimes(bDict, Essential, prime):
    """Copy strings in bDict identified as essential by
    True/False values in Essential and append to list
    prime"""
    for k in bDict:
        for i, v in enumerate(bDict[k]):
            if Essential[k][i]:
                prime.append(v)
#    print("\n\nPrimes: ",prime)
    return prime

def resetEssFlags(TempDict):
    """Take a dictionary with key:value pairs.
    keys are integers identifying number of bits set in all
    binary strings in lists
    values are lists of binary strings
    returns a dictionary with the same keys and all values
    containing boolean True"""
    bDictEssential = {}
    for k in TempDict:
        newlist = []
        for sz in range(len(TempDict[k])):
            newlist.append(True)
        bDictEssential[k] = newlist
    return bDictEssential

def decImps(term):
    """Parameter: String containing characters 1, 0 and X.
    Return list of all values where X's are replaced with all
    possible combinations of 1s and 0s"""
    numX = term.count("X")
    decList = []
    for b in range(2**numX):
        bbits = ("{:0>{}}".format(bin(b)[2:], numX))
        imp = term
        for bit in bbits:
            imp = imp.replace("X", bit, 1)
        decList.append(int(imp, 2))
    return(decList)

def binToVars(essStr):
    """Take a string containing 0s, 1s and Xs and return a string starting
    with A or !A if string starts with a 1 or 0 and exclude letters represented
    by X. Example:  X1X01 returns B !D E"""
    term = ""
    ch = 0
    for c in essStr:
        if c == '0':
           term += '!' + chr(ord('A') + ch) + ' '
        elif c == '1':
            term += chr(ord('A') + ch) + ' '
        ch += 1
    return term

def invList(imps):
    """Return a list of all integers less than or equal to the largest
    integer that can be represented with the bit size of the largest
    integer passed to the function and not included in the list passed
    to the function"""
    tmpList = []
    bitsize = max(imps).bit_length()
    for i in range(2**bitsize):
        if i not in imps:
            tmpList.append(i)
    print(tmpList)
    return tmpList

def sortByCountX(prime):
    """Take a list of strings and return a list sorted by the
    number of Xs found in each string"""
    pTemp = []
    for i in range(len(prime[0]) + 1):
        for p in prime:
           if i == p.count("X"):
                pTemp.append(p)
    return pTemp

def v2bterms(instr, vars):
    """ parameters:
    string  "A!B!D" representing a product in a sum of products
    boolean expression.
    list ['A', 'B', 'C', 'D'] containing all variables in the sum
    of products expression.
    returns a string "10?0" with missing variables in string replace
    with a "?".  """
    inlist = []
    c = 0
    while c < len(instr):
        if instr[c] == '!':
           inlist.append(instr[c] + instr[c+1])
           c += 2
        else:
            inlist.append(instr[c])
            c += 1
    #print("\n\n\tinstr: {}\n\n\tinlist: {}".format(instr, inlist))
    #print("\n\n\t vars: {}".format(vars))

    resb = ''
    for c in vars:
        if c not in inlist and ('!' + c) not in inlist:
            resb += 'X'
        elif c in inlist:
            resb += '1'
        else:
            resb += '0'
    #print("Result: {}".format(resb))
    return resb

