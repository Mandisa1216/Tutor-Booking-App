from flask import Flask
from flask import request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask import render_template, redirect, url_for

app = Flask (__name__,static_url_path='/static')
app.config["MONGO_URI"] = "mongodb://localhost:27017/signup"
Mongo = PyMongo(app)
db = Mongo.db

@app.route ("/signup",methods = ["POST","GET"])

def index():
  print("email")
  if request.method== "POST":
    print("email")
#    declare variables
    name= request.form["name"]
    email = request.form["email"]
    password = request.form["password"]
    print(name)
# adding user to the database
    user = {"name":name, "email":email, "password":password }
    
    if db.user_collection.insert_one(user):
       return render_template("login.html")
  return render_template("index.html")


@app.route ("/login",methods = ["POST","GET"])

def login():
  if request.method== "POST":
    print("email")
#    declare variables
    email = request.form["email"]
    password = request.form["password"]

    user = {"email":email, "password":password }
    
    if  db.user_collection.find_one(user):
        tutors = db.tutors.find()
        return redirect(url_for('display', tutors=tutors))
        

  return render_template("login.html")

# LANDING PAGE

@app.route("/")
def landing():
    return render_template("landing.html")

@app.route("/turordetail" , methods=["GET"] )
def turordetail():
     display = db.new_tutors.find()
     return render_template("turordetail.html" , display=display)

# ABOUT PAGE

@app.route("/About")
def about():
    return render_template("about.html")
        

# ADD PAGE

@app.route('/subject', methods=["GET"])
def subject():
    subjects = db.Subjects.find()
    return render_template('Subjects.html', subject=subjects)


from flask import redirect, url_for, render_template

@app.route('/add', methods=["POST", "GET"])
def add():
    if request.method == 'POST':
        id = request.form['id']
        print("add id: ", id)
        name = request.form['name']
        number = request.form['number']
        subject_name = request.form['subject']
        date = request.form['date']
        time = request.form['time']
        bookingstatus = "Waiting Response"
        subject = {
            'subject': subject_name,
            'name': name,
            'number': number,
            'date': date,
            'time': time,
            'bookingstatus': bookingstatus 
        }

        db.Subjects.insert_one(subject)

        # Redirect the user to the 'subjects' route after successful insertion
        return redirect(url_for('subjects', id=id))
    
    return render_template('add.html')

@app.route('/subjects/<id>')
def subjects(id):
    subjects = db.Subjects.find()
    return render_template('Subjectss.html', subjects=subjects, id=id)

@app.route('/subj/<id>')
def subj():
    subject = db.Subjects.find()
    return render_template('Subjectss.html', subject=subject, id=id)



@app.route("/adding")
def adding():
    tutors = list(db.tutors.find())
    return render_template("adding.html", tutors=tutors)

from flask import redirect, url_for



@app.route('/display_tutors')
def display_tutors():
    # Fetch and display the tutor data from the database
    tutors = db.new_tutors.find()
    return render_template('turordetail.html', display=tutors)

                 
   
from flask import redirect, url_for


@app.route('/tutorsignup', methods=['GET', 'POST'])
def tutorsignup():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
        phone = request.form['phone']
        subject = request.form['subject']
        date = request.form['date']
        time = request.form['time']
        location = request.form['location']
        password = request.form["password"]

        # Assuming you have a MongoDB connection string
        # Collection named 'tutors'
        tutor = {
            'name': name,
            'surname': surname,
            'email': email,
            'phone': phone,
            'subject': subject,
            'date': date,
            'time': time,
            'location': location,
            'password': password

        }
        db.new_tutors.insert_one(tutor)

        # Redirect the user to the display page after successful insertion
        return redirect(url_for('Tutorlogin'))
    else:
        return render_template("tutorsignup.html")
    
#Tutor login
@app.route ("/Tutorlogin",methods = ["POST","GET"])

def Tutorlogin():
  if request.method== "POST":
    print("email")
#    declare variables
    email = request.form["email"]
    password = request.form["password"]

    user = {"email":email, "password":password }
    
    if  db.new_tutors.find_one(user):
        tutors = db.new_tutors.find()
        return redirect(url_for('turordetail', tutors=tutors))
        

  return render_template("logintutor.html")

     

@app.route('/display')
def display():
    tutors = db.new_tutors.find()
    return render_template('display.html', tutors=tutors)


@app.route('/delete', methods=['POST'])
def delete_record():
    if request.method == "POST":
        id = request.form["deleteid"]
        db.Subjects.delete_one({'_id': ObjectId(id)})
        print(id)
        return redirect(url_for('school'))

       
    return render_template('Subjectss.html', subj=subjects)


@app.route('/updatepage', methods=['POST'])
def update_page():
    if request.method == "POST":   
        id = request.form["updateid"]

        return render_template('update.html', id=id)


@app.route('/update', methods=['POST'])
def update():
    if request.method == "POST":
        id = request.form["updateid"]
        name = request.form["name"]
        subject = request.form["subject"]
        time = request.form["time"]
        date = request.form["date"]


        db.Subjects.update_one({'_id': ObjectId(id)}, {"$set": {'name':name, 'subject':subject, 'date' :date, 'time':time }})
        print(id)
        subjects = list(db.Subjects.find())
    
    return render_template('Subjects.html', subj=subjects)

@app.route('/school', methods=['GET'])
def school():
    
      school=list(db.Subjects.find())

      return render_template('my booking.html', school=school)


@app.route('/status', methods=['GET'])
def status():
    
      status=list(db.Subjects.find())

      return render_template('status.html', status=status)






@app.route('/addbooking', methods=['POST'])
def booking():
    if request.method == "POST":
        id = request.form["id"]
    return render_template('Adding.html', id=id)

@app.route('/tutor', methods=['POST'])
def tutor():
  if request.method== "POST":
    print("email")
#    declare variables

    
    tutors = db.tutors.find()
    return render_template('Subjects.html', tutors=tutors)


  return render_template("login.html")


@app.route('/confirm', methods=['POST'])
def confirm():
    booking_id = request.form['confirm']
    print("confirm i", booking_id)
    # Update the status of the booking to "Confirmed"
    db.Subjects.update_one({'_id': ObjectId(booking_id)}, {'$set': {'bookingstatus': 'Confirmed'}})
    test = list(db.Subjects.find())
    print("tt", test)
    
    return redirect(url_for('school'))



if __name__ == "__main__":
    app.run(debug=True)

 
 