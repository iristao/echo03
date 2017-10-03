from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])    


def root():
    return render_template("fom.html")

@app.route('/returned', methods = ['GET', 'POST']) 

def returned():
	return render_template("returned.html", user = request.form["username"], method = request.method, message = request.form["message"])  

if __name__ == '__main__':
    app.debug = True
    app.run()
