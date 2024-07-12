from flask import Blueprint
from ..controllers import tutordetails



app = Blueprint ('display_tutors', __name__)


app.route ("/display_tutors",methods = ["POST","GET"])(tutordetails.display_tutors)
app.route ("/display",methods = ["POST","GET"])(tutordetails.display)