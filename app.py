from flask import Flask,render_template,url_for

app = Flask(__name__)   

@app.route("/")
def Home():
    return render_template('index.html')
@app.route("/quiz")
def quiz():
    return render_template('test-scrum.html')