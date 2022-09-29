from flask import render_template, request
from .rsascripts import *
from flask_login import login_required
from models.extensions import Composite


@login_required
def rsa():

    if request.method == "GET":
        return render_template("rsa/rsa.html", c="")

    if request.method == "POST":

        # Get encrption parameters
        E_n = request.form.get('n')
        E_e = request.form.get('e')
        E_m = request.form.get('m')
        c = rsaEncrypt(E_n, E_e, E_m)

        # Get decryption parameters
        D_N = request.form.get('N')
        D_D = request.form.get('D')
        D_C = request.form.get('C')
        M = rsaDecrypt(D_N, D_D, D_C)

        # Get totient parameters
        T_p = request.form.get('p')
        T_q = request.form.get('q')
        T_e = request.form.get('E')
        TOT = totFromPQ(T_p, T_q, T_e)

        # Get pem
        ppem = request.form.get('pem')
        PEM = pemmish(ppem)

        exploit_e, exploit_n, exploit_c = request.form.get('eee'), request.form.get(
            'nnn'), request.form.get('ccc')

        ME = "Not required"
        ow = wiener(exploit_e, exploit_n, exploit_c)

        success = "Awaiting input"

        # If n is provided
        if exploit_n:
            try:
                # Check database for n
                dbN = Composite.query.filter_by(value=int(exploit_n)).first()
            except:
                dbN = False
            # If n is in the database, and neither of the prime factors are 1
            if(dbN and [i.value for i in dbN.Primes][1] != 1):
                # Return prime factors
                DBF = "Factored using database: " + \
                    str([i.value for i in dbN.Primes])
                success = "Success!"
                ow = ""
                ME = ""

            # Database attack failed, try wiener

            # If wiener attack fails
            elif(ow == "" or ow == "Malformed input"):
                DBF = ""
                # Attempt small e attack
                ME = minuteE(exploit_e, exploit_c, exploit_n)

                # If small e attack fails
                if(ME == "" or ME == "Malformed input" or ME == "Not required"):
                    # Attempt fermat factorization with a max time of 2 seconds
                    fermat = ntfermat((exploit_n), 2)
                    # If fermat attack succeeds, and neither of the prime factors are 1
                    if(fermat != "" and fermat != "Malformed input" and fermat[1] != 1):
                        success = "Success!"
                        # Return prime factors
                        ow = "Factored using fermat factorization: " + \
                            str(fermat)
                        ME = ""
                    else:
                        # All attacks failed
                        success == "Failed"
                        ow = ""

                else:
                    # Minute e attack succeeded
                    success = "Success!"
                    ow = ""
            else:
                # Wiener attack succeeded
                DBF = ""
                ME = ""
                success = "Success!"
        else:
            # No n was provided
            DBF = ""
            ME = ""
            success = "Failed, no input"
        return render_template("rsa/rsa.html", c=c, m=M, TOT=TOT, PEM=PEM, ow=ow, ME=ME, DBF=DBF, success=success)
