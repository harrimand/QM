from qm import * #v2bterms, decImps

#sop = "AC!D + !AB!D+A!B D!E +A! C !DE + !A ! BD E+ A!B !C E"
#sop = "!A!E + AE +C"
#data = [13, 1, 9, 4, 0, 15, 11, 5]
sop = "AB!CD+!A!B!CD+A!B!CD+!AB!C!D+!A!B!C!D+ABCD+A!BCD+!AB!CD"

#instr = "AC!D"
#instr = "!AB!C!DE!F!G"
#vars = ['A', 'B', 'C', 'D', 'E']
vars = ['A', 'B', 'C', 'D']

print("\tSOP     : {}\n\n".format(sop))
soplist = [t.strip().replace(' ', '')  for t in sop.split('+')]
print("\tSOP List: {}\n\n".format(soplist))

bterms = []
for s in soplist:
    #print("\n\n\t{}".format(s), end = "  ")
    bterms.append(v2bterms(s, vars))

print("\tTerms: {}\n\n".format(bterms))

implist = []
for b in bterms:
	implist.extend(decImps(b))
implist = list(set(implist))

print("\tImpList: {}\n\n".format(implist))

#-----------------------------------------------------------------------

binData = decList2binList(implist)

bDict = mkSortByNumBitsSetDict(binData)

bDictEssential = mkEssDict(bDict)

prime = []
done = False
while not done:
    done = True
    TempDict = {}
    for b1 in bDict:

#        print(b1, bDict[b1])
        newList = []
        if (b1+1) in bDict:
            for h, bt in enumerate(bDict[b1]):

                for i, b2 in enumerate(bDict[b1+1]):

                    #print("\tCompare {} with {}. ".format(bt, b2), end = "")
                    res = compBin(bt, b2)
                    if res != "":
                        done = False
                        bDictEssential[b1+1][i] = False
                        bDictEssential[b1][h] = False
                        newList.append(res)
                        #print("\tCompare {} with {}. ".format(bt, b2), end = "")
                        #print("Result = {}".format (res))
                    #print("Result = {}".format (res))

                #print()

        if newList != []:
           TempDict[b1] = list(set(newList))

#    print("\n-------------------------------------------------")
    copyPrimes(bDict,bDictEssential, prime)
    bDictEssential = resetEssFlags(TempDict)
    bDict = TempDict

essentialFlag = []
impList = []
impFlat = []

for p in prime:
    imp = decImps(p)
    impList.append(imp)
    essentialFlag.append(False)
    for v in imp:
        impFlat.append(v)
    print("\n\t{}\t{}\n".format(p, imp))


#print("\n\n{: >{}}{}  ".format("impList:  ", 16, impList))

impFlat.sort()

#print("\n\n{: >{}}{}  ".format("impFlat:  ", 16, impFlat))
print("\n\n{: >{}}{}  ".format("impFlat:  ", 16, set(impFlat)))


for i, p in enumerate(impList):
    ess = False
    for c in p:
        if impFlat.count(c) == 1: #and c not in dontCare:
            ess = True
            essentialFlag[i] = True
    if not ess:
        for c in p:
            impFlat.remove(c)
        essentialFlag[i] = False

#print("\n\n{: >{}}{}  ".format("essentialFlag: ", 16, essentialFlag))

"""Create a list of essential terms in prime indicated by essentialFlag[]  """
essTerms = []
for i, p in enumerate(prime):
    if essentialFlag[i]:
        essTerms.append(p)

#print("\n\n")
#print("Essential Terms: {}".format(essTerms))

essList = []
for t in essTerms:
    essList.append(binToVars(t))
#print("\n\nEssential Terms: ", essList)

"""Create Sum Of Product string from list of terms"""
SOPstring = ""
for i, t in enumerate(essList):
    SOPstring += t
    if i < (len(essList) - 1):
        SOPstring += "+ "

print("\n\n Simplified SOP: {}".format(SOPstring))

print("\n\n")



