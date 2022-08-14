from flask import Flask, render_template
import requests
from pprint import pprint
app = Flask(__name__)
# titles = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391").json()
# print(titles)
data = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391").json()
pprint(data)

@app.route('/')
def home():
    return render_template("index.html",data = data)

@app.route("/<id>")
def open_blog(id):


    return render_template("post.html",data=data,id = int(id) )



if __name__ == "__main__":
    app.run(debug=True)
