from flask import Flask,url_for,redirect,Response,request,render_template,session, jsonify
from bson import ObjectId
from ..models.booking import booking

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

        subject = { 'subject':subject_name,'name':name, 'number': number,'date': date,'time': time,'bookingstatus': bookingstatus,
        }
        if booking.add_student(subject):
           return redirect(url_for('add.subjects', id=id))
        return render_template('add.html')

def add_booking():
    if request.method == "POST":
        id = request.form["id"]
    return render_template('Adding.html', id=id)


def subjects(id):
    subjects = booking.student_id()
    return render_template('Subjectss.html', subjects=subjects, id=id)

def school():
    
      school= booking.view_school()

      return render_template('my booking.html', school=school)


def confirm():
    booking_id = request.form['confirm']
    print("confirm i", booking_id)
    
    # Update the status of the booking to "Confirmed"
    booking.confirm_booking(booking_id)
    
    # test = list(booking.student_id())
    # print("tt", test)
    
    return redirect(url_for('add.school'))

def delete_record():
    if request.method == "POST":
        id = request.form["deleteid"]
        delete_id = ObjectId(id)
        booking.delete_record(delete_id)
        print(id)
        return redirect(url_for('add.school'))
    




    



    






            