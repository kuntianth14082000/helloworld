from flask import Flask,request,render_template,jsonify

app=Flask(__name__)
@app.route('/')
@app.route('/home')
def home():
    return "hello world"


if __name__=='__main__':
    app.run(debug=True)