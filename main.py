from flask import Flask, render_template, request
from flask_wtf import FlaskForm
import wtforms

app = Flask('app')

@app.route('/')
def home_page():
  return render_template("homepage.html")



#for running in repl
app.run(host='0.0.0.0', port=8080)


#for running in pycharm
#app.run(debug=True)