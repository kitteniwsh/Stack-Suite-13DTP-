from flask import render_template, send_file, request

def notes():
    return render_template("notes/notes.html")