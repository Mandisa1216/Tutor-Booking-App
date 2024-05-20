from flask import Flask
from flask import request
from flask_pymongo import PyMongo
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
     return render_template("Subjects.html")


  return render_template("login.html")

# LANDING PAGE

@app.route("/")
def landing():
    return render_template("landing.html")

# ABOUT PAGE

@app.route("/About")
def about():
    return render_template("about.html")


# ADD PAGE

@app.route('/subject', methods=["GET"])
def subject():
    subjects = db.Subjects.find()
    return render_template('Subjects.html', subjects=subjects)


@app.route('/add', methods=["POST", "GET"])
def add():
    if request.method == 'POST':
        name = request.form['name']
        number = request.form['number']
        subject_name = request.form['subject']
        date = request.form['date']
        time = request.form['time']
        
        subject = {
            'subject': subject_name,
            'name': name,
            'number': number,
            'date': date,
            'time': time
        }

        db.Subjects.insert_one(subject)

        return redirect('/subject')
    
    return render_template('add.html')

@app.route("/adding")
def adding():

    return render_template("adding.html",)

@app.route('/register', methods=['GET', 'POST'])
def register_tutor():
    if request.method == 'POST':
        tutor_data = {
            'name': request.form['name'],
            'surname': request.form['surname'],
            'email': request.form['email'],
            'phone': request.form['phone'],
            'subject': request.form['subject'],
            'date': request.form['date'],
            'time': request.form['time'],
            'location': request.form['location']
        }

        # tutor = {
        #     'subject': tutor_data['subject'],
        #     'name': tutor_data['name'],
        #     'number': tutor_data['phone'],
        #     'date': tutor_data['date'],
        #     'time': tutor_data['time']
        # }

        if db.tutors.find_one(tutor_data):
            return render_template('tutorsignup.html')
        else:
            db.tutors.insert_one(tutor_data)
            return render_template ('dispay.html')
    else:
        return render_template('tutorsignup.html')


@app.route('/display')
def display():
    tutor = []
    for i in db.tutors.find():
        tutor.append(i)
    print(tutor)
    return render_template("dispay.html" , i = tutor)
    # tutor_profiles = 
        # {
        #     "name": "John Doe",
        #     "surname": "Doe",
        #     "email": "johndoe@example.com",
        #     "phone": "123-456-7890",
        #     "subjects": ["Mathematics", "Physics", "Chemistry"],
        #     "date": "May 15, 2024",
        #     "time": "10:00 AM - 2:00 PM",
        #     "location": "123 Main Street, Anytown USA"
        # },
        # Add more tutor profiles here if needed
   
    return render_template('display.html', tutor_profiles=tutor_profiles)
    
from bson.objectid import ObjectId

# @app.route('/delete', methods=['POST'])
# def delete_Subjects():
#     if request.method == "POST":
#         id = request.form["id"]
#         db.Subjects.delete_one({'_id': ObjectId(id)})
        
#         subjects = list(db.Subjects.find())
    
#     return render_template('Subjects.html', subjects=subjects)
if __name__ == "__main__":
    app.run(debug=True)

 
 