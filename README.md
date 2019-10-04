# Quine McCluskey simplification
qm.py
Generate a simplified Sum Of products (SOP) from a list of decimal numbers where the truth table output is true.
Don't Care conditions may be included.
```
eg:
>>> tt = impStr2impList("0, 2, 3, 5..9")
>>> tt
[0, 2, 3, 5, 6, 7, 8, 9]
>>> dc = impStr2impList("10..")
>>> dc
[10, 11, 12, 13, 14, 15]
>>> qmSimp(tt, dc)
'!B!D + A + BD + C'
```

