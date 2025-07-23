from flask import Flask, redirect, url_for


app=Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to the Home Page!</h1>"

@app.route("/pass")
def passed():
    return "<h1>Congrats, you're passed</h1>."

@app.route("/fail")
def failed():
    return "<h1>Sorry, you're failed.</h1>"

@app.route("/score/<name>/<int:num>")
def score(name, num):
    if num<30:
        # code for fail
        return redirect(url_for("failed"))
    else:
        # code for pass
        return redirect(url_for("passed"))


if __name__== "__main__":
    app.run(debug=True)

