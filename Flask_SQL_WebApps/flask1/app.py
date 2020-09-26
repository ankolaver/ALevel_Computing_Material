from flask import Flask, render_template, request

app = Flask(__name__)#turn flask app in to a web app

@app.route("/")
def index(): #name it anything
    #return "hello, world" #<simply prints out hello world>
    #name = request.args.get("name","world. It a deep deep place.Stay zen") #second value is in case user does not provide one
    #if not name:
        #name = <second method to do stuff>
    #return render_template("index.html", personal=name) #this is a variable
    return render_template("index.html")

'''
@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    dorm = request.form.get("dorm")
    if not name or not dorm:
        return "Failure! Oof try again?"
    return render_template("success.html")
'''

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
