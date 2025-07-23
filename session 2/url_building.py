from flask import Flask, redirect, url_for


app=Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to the Home Page!</h1>"

@app.route("/pass/<name>/<int:num>")
def passed(name, num):
    return f"<h1>Congrats {name.title()}, you're passed with {num} marks.</h1>."

@app.route("/fail/<name>/<int:num>")
def failed(name,num):
    return f"<h1>Sorry {name.title()}, you're failed with {num} marks.</h1>"

@app.route("/score/<name>/<int:num>")
def score(name, num):
    if num<30:
        # code for fail
        return redirect(url_for("failed",sname=name,num=num))
    else:
        # code for pass
        return redirect(url_for("passed",sname=name,num=num))


if __name__== "__main__":
    app.run(debug=True)

