from flask import Blueprint
from ..controllers import user_controllers
from ..routes import user_routers

app = Blueprint ('user', __name__)

app.route("/")(user_controllers.landing) 
app.route ("/signup",methods = ["POST","GET"])(user_controllers.index)
app.route ("/login",methods = ["POST","GET"]) (user_controllers.login)

app.route('/tutorsignup', methods=['GET', 'POST']) (user_controllers.tutorsignup)
app.route ("/Tutorlogin",methods = ["POST","GET"]) (user_controllers.Tutorlogin)