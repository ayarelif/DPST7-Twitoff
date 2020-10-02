from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    x = 2 + 2
    return f"Hello World! {x}"

@app.route("/about")
def about():
    return "About me"

# on Windows:
# export FLASK_APP=hello.py ( in some case use "set" instead of export)
# flask run

# if you add this, you can run the flask app as:
# python Hello.py

if __name__=="__main__":
    app.run(debug=True)
    

