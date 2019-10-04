

from qm import *

segs = {
    'a': "0 2 3 5..9",
    'b': "..4 7 8 9",
    'c': "0 1 3..9",
    'd': "0 2 3 5 6 8",
    'e': "0 2 6 8",
    'f': "0 4 5 6 8 9",
    'g': "2..6 8 9"}

#segs = { 'a': "0 2 3 5 9" }

DCstr = "10.." #Don't Care Conditions 10..15
DClist = impStr2impList(DCstr) #String to List

with open("SevSegCcCa.txt", 'w') as SS:

# Creating Truth Table and printing each segment list.
    segList = []
    for s in range(ord('a'), ord('g')+1):
        segImp = impStr2impList(segs[chr(s)])
        segList.append(segImp)
        print("\n\t", chr(s) + " : " + segs[chr(s)].ljust(16), end='')
        print(chr(s),": ", segImp)
        SSstring = ("\n\n" + chr(s) + " : " + segs[chr(s)].ljust(16) + ', '.join(map(str, segImp)))
        SS.write(SSstring)

# Printing Don't Care conditions
    print("\n\tDC : " + DCstr.ljust(15), end='')
    print("DC : ", impStr2impList(DCstr))

# Printing Simplified SOP
    print("\n\n", '_'*60, "\nCommon Cathode\n")
    for ch, seg in enumerate(segList):
        print("\n\t", chr(ord('a')+ch), ": ", tt2ssop(seg, DClist))

# Inverting Truth Table and creating Simplified SOP list
    NsegList = []
    for s in range(ord('a'), ord('g')+1):
        NsegImp = invList(impStr2impList(segs[chr(s)]))
        NsegList.append(NsegImp)

# Printing Simplified SOPs from inverted Truth Table
    print("\n\n", '_'*60, "\nCommon Anode\n")
    for ch, seg in enumerate(NsegList):
        print("\n\t", chr(ord('a')+ch), ": ", tt2ssop(seg, DClist))

SS.close()

