from flask import Flask


app = Flask(__name__)


#dumy
@app.route('/')
def index():
    return "welcome to api"

@app.route("/blog/<int:postID>") #int
def show_blog(postID):
	return 'Blog number is : %s' % postID

@app.route("/rev/<float:revno>")  #float
def revision(revno):
	return 'Revision number is : %s' %revno

@app.route("/hello/<name>") #string
def hello_name(name):
	return 'Hello %s!' %name


if __name__ == "__main__":
    app.run(debug=True)

