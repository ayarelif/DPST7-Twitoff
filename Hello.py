from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/new_page')
def new_page():
    return 'This is another page'

# on Windows:
# export FLASK_APP=hello.py ( in some case use "set" instead of export)
# flask run

# if you add this, you can run the flask app as:
# python Hello.py

if __name__=="__main__":
    app.run(debug=True)