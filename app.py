from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS, cross_origin
import json
import os

app = Flask(__name__, static_folder="./resources/")
CORS(app)



@app.route('/', methods=['GET', 'POST'])
@cross_origin(origin="*")
def home():
    if request.method == 'POST':
        return redirect(url_for('task'))
    return render_template('home.html')

@app.route("/task", methods=["GET", "POST"])
@cross_origin(origin="*")
def task():
	if (request.method == "POST"):
		form = request.form
		x = form.to_dict(flat=False)
		path = os.getcwd()+ "/"+form['name'].lower()+'.json'
		if os.path.isfile(path)==False:
			with open(form['name'].lower()+'.json','w') as f:
				f.write(json.dumps(x,indent=4))
			return render_template('story.html')
		else:
			with open(form['name'].lower()+'_updated.json','w') as f:
				f.write(json.dumps(x,indent=4))
			return render_template('index.html')
	return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
