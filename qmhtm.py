#! /bin/opt/env python

def htmTT(sop):
    from qm import getVars, sop2imps
    V = getVars(sop)
    imps = sop2imps(sop, V)
    tt = [['N'] + [chr(ch + 65) for  ch in range(max(imps).bit_length())] + ['Q']]
    nmax = 2**max(imps).bit_length()
    bv = [[b for b in bin(d)[2:].zfill(nmax.bit_length()-1)] for d in range(nmax)]
    for i, b in enumerate(bv):
        tf = '1' if i in imps else '0'
        row = [str(i)]
        row.extend(b)
        row.append(tf)
        tt.append(row)
#    return tt
    ttStr = '<table id="t01">\n<tr>\n'
    for th in tt[0]:
        ttStr = ttStr + '<th>' + th + '</th>'
    ttStr = ttStr + '\n</tr>\n'
    for tr in tt[1:]:
        ttStr = ttStr + '<tr>\n'
        for td in tr:
            ttStr = ttStr + '<td>' + td + '</td>'
        ttStr = ttStr + '\n</tr>\n'
    ttStr = ttStr + '</table>'
    return ttStr

def htm(sop):
    from qm import sop2htm
    from os import getcwd
    import webbrowser

    headStr = '\
    <!DOCTYPE html>\n\
    <html>\n\
    <head>\n\
    <title>Bool Exp</title>\n\
    <h1 style="text-align:center;">Boolean Expression</h1>\n\
    \n\
    <p style="text-align:center; font-size:160%; ">\n\
    <br>\n\
    <br>\n'

    tailStr = '\n\
    </body>\n\
    </html>\n'

    tableStyle = '\n\
    <style>\n\
    table{\n\
    width:25%;\n\
    margin-left: 200px;\n\
    }\n\
    table, th, td {\n\
    border: 1px solid black;\n\
    border-collapse: collapse;\n\
    }\n\
    th, td {\n\
    padding: 15px;\n\
    text-align: center;\n\
    }\n\
    table#t01 tr:nth-child(even) {\n\
    background-color: #eee;\n\
    }\n\
    table#t01 tr:nth-child(odd) {\n\
    background-color: #fff;\n\
    }\n\
    table#t01 th {\n\
    background-color: black;\n\
    color: white;\n\
    }\n\
    table#t01 td {\n\
    text-align: center;\n\
    }\n\
    </style>\n'

    htmsop = sop2htm(sop)
    htmTable = htmTT(sop)

#    print(htmTable)

    with open("boolT.html", 'w') as fid:
        fid.write(headStr)
        fid.write(tableStyle)
        fid.write('</head>\n<body>\n<p style="text-align:center; font-size:160%; ">\n')
        fid.write(htmsop)
        fid.write('</p>\n<br><br>\n')
        fid.write(htmTable)

        fid.write(tailStr)

    print("boolT.html file created\n")

    filePath = "file://" + getcwd() + "/boolT.html"
    webbrowser.open(filePath, new=2)

