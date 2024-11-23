from flask import Flask,render_template,url_for,request
from views import sobrenome, gerar_cert
import sqlite3

app = Flask(__name__)   

@app.route("/")
def Home():
    return render_template('index.html')
@app.route("/quiz")
def quiz():
    return render_template('test-scrum.html')
@app.route('/quemsomos')
def quemsomos():
    return render_template ('/quemsomos.html')

@app.route('/insert', methods = ['POST','GET'])
def insert():
    if request.method == 'POST':
        try:
            nm = request.form['nome']
            cpf = request.form['CPF']
            pts1 = request.form['pts-1']
            pts2 = request.form['pts-2']
            pts3 = request.form['pts-3']
            pts4 = request.form['pts-4']
            pts5 = request.form['pts-5']
            with sqlite3.connect('database.db') as conn:
                cur = conn.cursor()
                cur.execute(f"SELECT * FROM users WHERE CPF = '{cpf}' AND Nome = '{nm}'")
                if cur.fetchone():
                    cur.execute(f"UPDATE users SET quiz = '"+pts1+"', quizz = '"+pts2+"', quizzz = '"+pts3+"', quizzzz = '"+pts4+"', quizzzzz='"+pts5+"' WHERE CPF = '"+cpf+"'")
                    conn.commit()
                else:
                    cur.execute(f"INSERT INTO users (CPF,Nome,quiz,quizz,quizzz,quizzzz,quizzzzz) values (?,?,?,?,?,?,?)", (cpf,nm,pts1,pts2,pts3,pts4,pts5))
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
            with sqlite3.connect('database.db') as conn:
                cur = conn.cursor()
                cur.execute("DELETE FROM users WHERE CPF = '"+cpf+"' and Nome = '"+nm+"'")
                conn.commit()
        except:
            conn.rollback()
            msg ="Dados invalidos"
        finally:
            conn.close()
            return mostra()
        
@app.route('/mostrar')
def mostra():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    cur.close()
    return render_template('teste.html', rows = rows)

@app.route('/certificado', methods=['POST'])
def certificado():
    cpf = request.form['cpf']
    nome = sobrenome(request.form['nome'])
    cert = gerar_cert(nome)
    return render_template('certificado.html', cert = cert)