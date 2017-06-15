from qm import *

#data = [0, 1, 4, 5, 9, 11, 13, 15]
#data = [13, 1, 9, 4, 0, 15, 11, 5]
#data = [13, 9, 15, 31, 27, 23, 29, 25, 19]
#data = [7, 11, 13, 14, 19, 21, 22, 25, 26, 28]
#data = [15, 6, 12, 0, 9, 30, 7, 29, 24, 31, 17, 18, 3]
#data = [0, 1, 4, 5, 6, 7, 9, 11, 13, 15, 14]
data = [0, 1, 4, 5, 3, 16, 17, 20, 21, 19, 11, 10, 26, 27, 15, 14, 31, 30, 8, 24]
#data = [1, 3, 25, 26, 6, 14, 20, 28, 17, 19, 9, 10, 22, 30, 4, 12, 2, 8, 11, 0]
#data = [12, 16, 10, 22, 15, 20, 9, 19, 13, 17, 14, 21, 11, 18, 8, 23, 3, 25, 1, 29, 7, 27, 5, 31]
#data = [0, 2, 4, 5, 6, 7, 12, 13, 14, 15, 8, 10, 17, 19, 20, 21, 22, 23, 28, 29, 30, 31, 25, 27]

#Don't Care List
dontCare = []
#dontCare = [0, 2, 24, 26, 4, 6]
#data.extend(dontCare)
#print(data)



dontCare = validDontCares(dontCare, data)

#data = invList(data)

print("\t", data, "\n")

#bitsize = max(data).bit_length()

binData = decList2binList(data)

bDict = mkSortByNumBitsSetDict(binData)

bDictEssential = mkEssDict(bDict)

print("\n******")
print(str(bDict))
print("******\n")


"""Take list of binary strings and replace characters where two compared
strings differ only by 1 character and different characters are 1s and 0s.
Differing characters are replaced with Xs. If no string is found that
differs only by a single 1 or 0, then that string (term) is copied to a
list of prime.  Strings are sorted by the number of 1s to minimize the
number possible matches and reduce number of comparisons required.
Search and Replace process is repeated for all strings that are not
copied to prime until entire list of strings is searched and no matches
are found."""
prime = []
done = False
while not done:
    done = True
    TempDict = {}
    for b1 in bDict:

        print(b1, bDict[b1])
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
                        print("\tCompare {} with {}. ".format(bt, b2), end = "")
                        print("Result = {}".format (res))
                    #print("Result = {}".format (res))

                print()

        if newList != []:
           TempDict[b1] = list(set(newList))

    print("\n-------------------------------------------------")
    copyPrimes(bDict,bDictEssential, prime)
    bDictEssential = resetEssFlags(TempDict)
    bDict = TempDict


print("\n\n{: >{}}{}  ".format("Prime:   ", 16, prime))

prime = list(set(prime))

print("\n\n{: >{}}{}  ".format("Prime Set:  ", 16, prime))

prime.sort()

print("\n\n{: >{}}{}  ".format("Prime Sorted:  ", 16, prime))

prime = sortByCountX(prime)

print("\n\n{: >{}}{}  ".format("Sorted by #Xs:  ", 16, prime))

print("\n\n{: >{}}{}\n".format("data:   ", 16, data))


"""Take a list of strings equal in length containing 0s, 1s and Xs.
Create a list of lists containing all integers that can
be represented by substituting Xs with all combinations of
0s and 1s. A string with n Xs returns a list of 2^n integers.
impFlat is a flat list of all integers including duplicates."""
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


print("\n\n{: >{}}{}  ".format("impList:  ", 16, impList))

impFlat.sort()

print("\n\n{: >{}}{}  ".format("impFlat:  ", 16, impFlat))


"""Take a list containing lists of integers and a flat list
containing all integers including duplicates.
If all elements of a list have duplicates in the flat list
remove one copy of each element from the flat list and mark
the list as non-essential.  Values in the dontCare list are
not required to be in the flat list."""
for i, p in enumerate(impList):
    ess = False
    for c in p:
        if impFlat.count(c) == 1 and c not in dontCare:
            ess = True
            essentialFlag[i] = True
    if not ess:
        for c in p:
            impFlat.remove(c)
        essentialFlag[i] = False

print("\n\n{: >{}}{}  ".format("essentialFlag: ", 16, essentialFlag))

"""Create a list of essential terms in prime indicated by essentialFlag[]  """
essTerms = []
for i, p in enumerate(prime):
    if essentialFlag[i]:
        essTerms.append(p)

print("\n\n")
print("Essential Terms: {}".format(essTerms))

"""Create a list of essential terms with alpha character representation
Example ["0X1X1", "10XX0"] returns ["!A C E", "A !B !E"]"""
essList = []
for t in essTerms:
    essList.append(binToVars(t))
print("\n\nEssential Terms: ", essList)

"""Create Sum Of Product string from list of terms"""
SOPstring = ""
for i, t in enumerate(essList):
    SOPstring += t
    if i < (len(essList) - 1):
        SOPstring += "+ "

print("\n\nSimplified SOP: {}".format(SOPstring))

print("\n\n")






