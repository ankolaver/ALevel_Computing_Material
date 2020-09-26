from flask import *
import sqlite3
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
#app.config['MAX_CONTENT_LENGTH'] = 16*1024*1024
app.config['SECRET_KEY'] = '9483f' #random
app.config['UPLOAD_FOLDER'] = 'static/'

@app.route("/upload",methods=["GET","POST"])
def upload():
    if request.method == "GET":
        return render_template("upload.html")
    else:
        '''
        f = request.files['bigpic']
        f.save(secure_filename(f.filename))
        return "file upload sucessful"
        '''
        f = request.files['bigpic']
        filenames = []
        #for f in files:
        if f:
            f_name = secure_filename(f.filename)
            filenames.append(f_name)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], f_name))
        print(filenames)
        return render_template("upload.html", filenames=filenames)
        

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/input", methods=["POST"])
def input():
    if request.method == "POST":
        u_location = request.form.get("location")
        print(u_location)
        conn = sqlite3.connect("bakery.db")
        cur = conn.cursor()
        data = cur.execute("SELECT Name, Type, Price FROM Product WHERE Location=? ORDER BY Price DESC",(u_location,)).fetchall()
        return render_template("index.html",u_location=u_location,data=data)

if __name__ == "__main__":
    app.run()
    
