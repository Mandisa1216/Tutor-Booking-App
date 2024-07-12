from flask import Flask,url_for,redirect,Response,request,render_template,session, jsonify
from ..models.tutordetails import tutor


def display_tutors():
    # Fetch and display the tutor data from the database
    tutors = tutor.tutor_details()
    return render_template('turordetail.html', display=tutors)


    # Fetch and display the tutor data from the database
def display():
    tutors = tutor.display()
    return render_template('display.html', tutors=tutors)

