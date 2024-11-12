from flask import Flask,render_template,url_for,request
import sqlite3

app = Flask(__name__)   

@app.route("/")
def Home():
    return render_template('index.html')
@app.route("/quiz")
def quiz():
    return render_template('test-scrum.html')

@app.route('/Q-I', methods = ['POST','GET'] )
def insert():
    if request.method == 'POST':
        try:
            nm = request.form['nome']
            cpf = request.form['CPF']
            quiz = request.form['Q']
            pts = request.form['pts']
            with sqlite3.connect('database.db') as conn:
                cur = conn.cursor()
                cur.execute(f"SELECT * FROM users WHERE CPF = '{cpf}' AND Nome = '{nm}'")
                if cur.fetchone():
                    cur.execute(f"UPDATE users SET "+quiz+"="+pts+" WHERE CPF = '"+cpf+"'")
                    conn.commit()
                else:
                    cur.execute(f"INSERT INTO users (CPF,Nome,{quiz}) values (?,?,?)", (cpf,nm,pts))
                    conn.commit()
        except:
            conn.rollback()
            msg ="Dados invalidos"
        finally:
            conn.close()
            return render_template('test-scrum.html')
@app.route('/delete', methods = ['POST','GET'])
def delete():
    if request.method == 'POST':
        try:
            nm = request.form['nome']
            cpf = request.form['CPF']
            quiz = request.form['Q']
            pts = request.form['pts']
            with sqlite3.connect('database.db') as conn:
                cur = conn.cursor()
                cur.execute("DELETE FROM users WHERE CPF = '"+cpf+"' and Nome = '"+nm+"'")
                conn.commit()
        except:
            conn.rollback()
            msg ="Dados invalidos"
        finally:
            conn.close()
            return render_template('test-scrum.html')
@app.route('/mostrar')
def mostra():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT CPF, * FROM users")
    rows = cur.fetchall()
    cur.close()
    return render_template('teste.html', rows = rows)