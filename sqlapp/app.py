from flask import Flask, render_template, request, flash
import os
import sqlite3

#UPLOAD_FOLDER = 'C:\\Users\\Kenneth\\Downloads'

app = Flask(__name__)
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/',methods=["GET","POST"])
def main():
    if request.method == "GET":
        return render_template("main.html")
    else:
        
        if 'file' in request.files:
            #file = request.files['file']
            #file_name = secure_filename(file.filename)
            #file.save(os.path.join(target, file_name))
            #flash("Item uploaded!")
            
            return '''<!DOCTYPE HTML>
<body>successful!</body>'''

        con = sqlite3.connect("new.db")
        con.execute("""CREATE TABLE IF NOT EXISTS ITEMS""" +\
                    """(ID INTEGER PRIMARY KEY AUTOINCREMENT, Title TEXT);""")
        data = request.form.get("data")
        con.execute("INSERT INTO ITEMS(Title) VALUES(?)",(data,))
        con.commit()
        stuff = con.execute("SELECT * FROM ITEMS ORDER BY Title ASC")
        stuff = stuff.fetchall()
        
        if request.form.get("del")=="del":
            con.execute("DELETE FROM ITEMS WHERE Title IS NULL;")
            con.commit()
        con.close()   
        return render_template("main2.html",stuff = stuff)

if __name__ == "__main__":
    app.run()
