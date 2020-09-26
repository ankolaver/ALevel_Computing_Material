from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = '7f3'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/form', methods=["POST"])
def form():
    #if request.method == "GET":
        #return "Not allowed to access"
    #else: #request.method == "POST"
    matric_no = request.form.get("matric_no")
    print(matric_no)
    session['matric_no'] = matric_no
    
    if matric_no is None:
        return redirect(url_for('/'))
    else:
        #Connect to DB
        conn = sqlite3.connect('school.db')
        cursor = conn.cursor()

        #Extract data
        matric_no = int(matric_no)
        studentinfo = cursor.execute('''
            SELECT * FROM STUDENT WHERE MatricNo=?
        ''',(matric_no,)).fetchall()
        print(studentinfo)
        name = studentinfo[0][1]
        gender = studentinfo[0][2]
        civicsclass = studentinfo[0][3]
        
        civicsinfo = cursor.execute('''
            SELECT Tutor,HomeRoom FROM Civics WHERE Class=?
        ''',(civicsclass,)).fetchall()
        print(civicsinfo)
        tutor = civicsinfo[0][0]
        homerm = civicsinfo[0][1]

        sccainfo = cursor.execute('''
            SELECT CCAName FROM StudentCCA WHERE MatricNo=?
        ''',(matric_no,)).fetchall()
        print(sccainfo)
        cca = sccainfo[0][0]

        ccainfo = cursor.execute('''
            SELECT TeacherIC FROM CCAInfo WHERE Name=?
        ''',(cca,)).fetchall()
        cca_teacher = ccainfo[0][0]
        print(ccainfo)
        
        conn.commit()
        conn.close()
        return render_template("info.html",matric_no=matric_no,name=name,gender=gender,civicsclass=civicsclass,tutor=tutor,homerm=homerm,cca_teacher=cca_teacher)

@app.route('/cca', methods=["POST"])
def cca():
    change_cca = request.form.get("change")
    if change_cca == "N":
        return render_template("the_end.html")
    elif change_cca == "Y":
        db = sqlite3.connect('school.db')
        c = db.cursor()
        c.execute('''SELECT name FROM CCAInfo''')
        data = c.fetchall()
        return render_template("cca.html", data=data)

@app.route('/update', methods=["POST"])
def update():
    matric_no = session['matric_no']
    user_cca = request.form.get("cca_choice")
    print(f"USercca {user_cca}, matric_no: {matric_no}")
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()
    cursor.execute("""UPDATE STUDENTCCA SET CCANAME=? WHERE MatricNo=?""",(user_cca,matric_no))
    conn.commit()
    conn.close()
    return render_template("success.html",matric_no=matric_no,user_cca=user_cca)    
    
if __name__ == "__main__":
    app.run(debug=True)
