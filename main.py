from flask import Flask, request

app = Flask(__name__)

@app.route("/<nome>")
def hello(nome):
    text = "<h1>Microsoft Student Partners</h1>"
    text += "<h3>Hello, {}!</h3> <br>".format(nome)
    text += "<img src='https://secure.meetupstatic.com/photos/event/b/b/2/a/global_481787914.jpeg'><br><br>"
    text += "<i>by Jean J. Barros</i>"
    return text