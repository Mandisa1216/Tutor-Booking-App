from flask import Blueprint
from ..controllers import booking_controller


app = Blueprint ('add', __name__)

app.route('/add', methods=["GET", "POST"]) (booking_controller.add)
app.route('/addbooking', methods=['GET','POST']) (booking_controller.add_booking)
app.route('//subjects/<id>', methods=['GET','POST']) (booking_controller.subjects)
app.route('/school', methods=['GET']) (booking_controller.school)
app.route('/confirm', methods=['POST'])(booking_controller.confirm)
app.route('/delete', methods=['POST'])(booking_controller.delete_record)

