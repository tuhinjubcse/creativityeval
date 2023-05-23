from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__, static_folder="./resources/")
CORS(app)

@app.route("/", methods=["GET", "POST"])
@cross_origin(origin="*")
def home():
	if (request.method == "POST"):
		form = request.form
		x = form.to_dict(flat=False)
		with open(form['name'].lower()+'.json','w') as f:
			f.write(json.dumps(x,indent=4))
		return render_template('story.html')
	return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
