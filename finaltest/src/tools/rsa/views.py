from flask import render_template, session, redirect, request
from .rsascripts import *

from flask_login import login_required
from models.extensions import db, User, Prime, Composite, t_Primes_Composites

@login_required
def rsa():

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
        dbN = Composite.query.filter_by(value=int(nnn)).first()
        if(dbN):
            DBF =  "Factored using database: " + str([i.value for i in dbN.Primes])
            success = "Success!"
            ow = ""
            ME = ""
        elif(ow == "Attack not applicable" or ow == "Malformed input"):
            DBF = ""
            ME = minuteE(eee, ccc, nnn)
            if(ME == "Attack not applicable" or ME == "Malformed input" or ME == "Not required"):
                success == "Failed"
            else:
                success = "Success!"
                ow = ""
        else:
            DBF = ""
            ME = ""
            success = "Success!"
        return render_template("rsa/rsa.html", c=c, m=M, TOT = TOT, PEM=PEM, ow=ow, ME=ME, DBF=DBF, success=success)

        