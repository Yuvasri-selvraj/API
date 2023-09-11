#URL binding
from flask import Flask,redirect,url_for
app = Flask(__name__)

@app.route("/admin")
def hello_admin():
    return "Hello Admin Sir or Mam !!"

@app.route("/guest/<guest>")
def hello_guest(guest):
    return "Hello %s you logged in as guest user" % guest

@app.route("/user/<name>")
def hello_user(name):
    if name == 'admin' :
        return redirect(url_for("Hello Admin"))

    else:
        return redirect(url_for('Hello_guest', guest = name))


if __name__ == '__main__':
    app.run(debug=True)