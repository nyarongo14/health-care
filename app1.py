from flask import Flask
# from flask import*
app= Flask(__name__)

@app.route('/')
def home():
    return"hello world"

if__name__=='_main_':


app.run(debug=True)