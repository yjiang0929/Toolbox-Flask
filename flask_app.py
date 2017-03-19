"""
Put your Flask app code here.
"""

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html')

@app.route('/login/', methods=['GETS','POST'])
def login():
    error = None
    if request.method == "POST":
        name = request.form.get('name','')
        age = request.form.get('age','')
        ninja = request.form.get('ninja','')
        if name == '' or age == '' or ninja == '':
            error = 'Please check your input and fill in all the boxes'
    return render_template('login.html',name=name, age=age, ninja = 'Patrick Huston',
                           error=error)

if __name__ == '__main__':
    app.debug = True
    app.run()
