from flask import render_template, session, redirect, request
from .rsascripts import *
def rsa():
    if not session["authed"]:
        return redirect("/authenticate")
    if request.method == "GET":
        return render_template("rsa/rsa.html", c="")
    if request.method == "POST":
        
        n =request.form.get('n')
        e = request.form.get('e')
        m = request.form.get('m')
        c = rsaEncrypt(n,e,m)

        N =request.form.get('N')
        D = request.form.get('D')
        C = request.form.get('C')
        M = rsaDecrypt(N,D,C)

        p =request.form.get('p')
        q = request.form.get('q')
        e = request.form.get('E')
        
        TOT = totFromPQ(p, q, e)


        ppem = request.form.get('pem')
        PEM = pemmish(ppem)
        ME = "Not required"
        eee, nnn, ccc = request.form.get('eee'), request.form.get('nnn'), request.form.get('ccc')
        ow = wiener(eee, nnn, ccc)
        success = "Awaiting input"
        if(ow == "Attack not applicable" or ow == "Malformed input"):
            ME = minuteE(eee, ccc, nnn)
            if(ME == "Attack not applicable" or ME == "Malformed input"):
                success == "Failed"
            else:
                success = "Success!"
        else:
            success= "Success!"        
        return render_template("rsa/rsa.html", c=c, m=M, TOT = TOT, PEM=PEM, ow=ow, ME=ME, success=success)
        
    
    
