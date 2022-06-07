from flask import render_template, send_file, request, session

def index():
    auth = "0"
    try:
        if session["authed"]:
            auth = "1"
    except:
        pass
    return render_template("base/index.html", auth=auth)

def favicon():
    return send_file("../static/favicon.ico", mimetype='image/gif')
