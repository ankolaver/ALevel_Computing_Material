from flask import Flask, render_template, request

import sqlite3

app = Flask(__name__)
@app.route('/',methods=["GET","POST"])
def main():
    if request.method == "GET":
        #looks for file in templates folder, name cannot be changed
        return render_template("index.html")

    else: #request.method == "POST"
        name = request.form.get("name")
        
        conn = sqlite3.connect("inventory.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM parts")
        rows = cur.fetchall()
        print(rows)
        return render_template("onsubmit.html", name=name, rows=rows)

if __name__=="__main__":
    app.run()