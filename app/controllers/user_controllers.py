from flask import Flask,url_for,redirect,Response,request,render_template,session, jsonify
from ..models.user import user

def landing():
    return render_template("landing.html")

def index():
  print("email")
  if request.method== "POST":
    print("email")
    name= request.form["name"]
    email = request.form["email"]
    password = request.form["password"]
    print(name)

    details = {"name":name, "email":email, "password":password }
    
    if(user.create_user(details)):
       return render_template("login.html")
  return render_template("index.html")

def login():
  if request.method== "POST":
    email = request.form["email"]
    password = request.form["password"]

    user_controllers = {"email":email, "password":password }
    user.get_all_user_collection(user_controllers)
    return redirect(url_for('display_tutors.display'))

        

  return render_template("login.html")





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

      user_tutor = {"name":name, "surname":surname, "email":email, "phone":phone,"subject":subject, "date":date, "time":time, "location":location, "password":password, }
    

      if user.create_tutor_signup(user_tutor):
        return render_template("logintutor.html")
    return render_template("tutorsignup.html")

def Tutorlogin():
  if request.method== "POST":
    email = request.form["email"]
    password = request.form["password"]

    user_tutor = {"email":email, "password":password }
    user.get_all_tutor_login(user_tutor)

    return redirect(url_for('display_tutors.display_tutors'))
  
  return render_template("logintutor.html")


        

        
