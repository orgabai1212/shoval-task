from flask import Flask ,request,jsonify,render_template,flash
import mysql.connector


app = Flask(__name__)



def connect():
    return mysql.connector.connect(
    host="some-mysql",
    user="root",
    password="root",
    database="orgabay",
    port="3306"
    )
def sql_command(command):
    conection =connect()
    cursor = conection.cursor()
    cursor.execute(command)
    result=cursor.fetchall()
    cursor.close()
    conection.close()
    return result

def sql_insert(id,first_name,last_name):
    conection =connect()
    cursor = conection.cursor()
    qury="insert into person (id,first_name,last_name) values (%s,%s,%s)"
    values=(id,first_name,last_name)
    cursor.execute(qury,values)
    conection.commit()
    cursor.close()
    conection.close()


def sql_delete(id):
  conection=connect()
  cursor = conection.cursor()
  qury=f"delete from person where id = {id};"
  cursor.execute(qury)
  conection.commit()
  cursor.close()
  conection.close()
 

@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/add',methods=['POST','GET'])
def add():
    if request.method == 'POST':
      id = request.form.get('id')
      first_name=request.form.get('first_name')
      last_name=request.form.get('last_name')
      sql_insert(id,first_name,last_name)
      return  "person added"
    return render_template("add.html")

#get all criminal list im db
@app.route('/all',methods=['GET'])
def all():
  result =sql_command("select * from person;")
  return jsonify(result)
  
# sql_insert(322271525,idan,shvar)

@app.route('/delete',methods=['GET','POST'])
def delete():
  if request.method == 'POST':
    person_to_rm=request.form.get('id')
    sql_delete(person_to_rm)
    return "person removd"
  return render_template("delete.html")

@app.route('/find', methods=['GET', 'POST'])
def find():
    if request.method == 'POST':
        check_id = request.form.get('id')
        if check_id:
            command = f"SELECT id, first_name, last_name FROM person WHERE id={check_id};"
            person = sql_command(command)
            return jsonify(person)
        
    return render_template('find.html')
  


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
