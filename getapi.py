from typing import List, Dict

from flask import Flask , jsonify




app = Flask(__name__)

courses  = [{"name": "yuvashrii",
            "course_id" :"1",
			"gender": "female",
			"address" : "selvavinayagar kovil street"},
            {'name': "yuva",
            "course_id" :"2",
			"gender": "female",
			"address" : "vadaku vellar street"},
           {"name": "shrii",
            "course_id" :"3",
			"gender": "male",
			"address" : "mundrumavadi"}]



@app.route('/')
def index():
    return "welcome to Home Page"

@app.route("/courses", methods = ['GET'])
def get():
	return jsonify({'courses' : courses})

@app.route("/courses/<int:course_id>", methods = ['GET'])
def get_course(course_id):
    return jsonify({'course' : courses[course_id]})

if __name__ == "__main__":
    app.run(debug=True)


