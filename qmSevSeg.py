
from qm import *

segs = {
    'a': "0 2 3 5..9",
    'b': "..4 7 8 9",
    'c': "0 1 3..9",
    'd': "0 2 3 5 6 8",
    'e': "0 2 6 8",
    'f': "0 4 5 6 8 9",
    'g': "2..6 8 9"}

DCstr = "10.." #Don't Care Conditions 10..15
DClist = impStr2impList(DCstr) #String to List

with open("SevSegCcCa.txt", 'w') as SS:

    # Creating Truth Table and printing each segment list.
    segList = []
    for s in range(ord('a'), ord('g')+1):
        print("\n\t", chr(s) + " : " + segs[chr(s)].ljust(16), end='')
        segImp = impStr2impList(segs[chr(s)])
        segList.append(segImp)
        print(chr(s),": ", segImp)
        SS.write('\n\t' + chr(s) + ": " + ''.join(str(segImp)))

    # Printing Don't Care conditions
    print("\n\tDC : " + DCstr.ljust(15), end='')
    print("DC : ", impStr2impList(DCstr))
    SS.write("\n\n\tDC: " + ''.join(str(impStr2impList(DCstr))))

    # Printing Simplified SOP
    print("\n", '_'*60, "\n Common Cathode")
    SS.write("\n\n" + '_'*60 + "\n Common Cathode\n")

    for ch, seg in enumerate(segList):
        print("\n\t", chr(ord('a')+ch), ": ", end='')
        print(tt2ssop(seg, DClist))
        SS.write("\n\n\t" + chr(ord('a')+ch) + ": ") 
        SS.write(tt2ssop(seg, DClist))

    # Inverting Truth Table and creating Simplified SOP list
    NsegList = []
    for s in range(ord('a'), ord('g')+1):
        NsegImp = invList(impStr2impList(segs[chr(s)]))
        NsegList.append(NsegImp)

    # Printing Simplified SOPs from inverted Truth Table
    print("\n", '_'*60, "\n Common Anode")
    SS.write("\n\n" + '_'*60 + "\n Common Anode\n")
    for ch, seg in enumerate(NsegList):
        print("\n\t", chr(ord('a')+ch), ": ", end='')
        print(tt2ssop(seg, DClist))
        SS.write("\n\n\t" + chr(ord('a')+ch) + ": ") 
        SS.write(tt2ssop(seg, DClist))

SS.close()

