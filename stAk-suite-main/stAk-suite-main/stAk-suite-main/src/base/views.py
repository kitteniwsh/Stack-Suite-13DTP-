from flask import render_template, send_file, request, session

def index():
    if(session["authed"]):
        return render_template("base/indexAUTH.html")

    else:
        return render_template("base/index.html")

def favicon():
    return send_file("../static/favicon.ico", mimetype='image/gif')
