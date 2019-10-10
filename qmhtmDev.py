
from qm import *
from qmhtm import *

sop = '!B!DE + !ACE + !BC!DE + A!CDE + AB!CE + BDE'

V = getVars(sop)
impList = sop2imps(sop, V)
T = htmTT(sop)

# for t in T: print(t)
print(T)

'''
for t in T:
   print("\t" + str(int(''.join(t),2)).ljust(6) + " ".join(t))
'''

