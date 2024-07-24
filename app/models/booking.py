from bson import ObjectId
from ..import mongo

class booking:
    
    def add_student(subject):
        return mongo.db.Subjects.insert_one(subject)
    
    def student_id():
        return  mongo.db.Subjects.find()
    
    def view_school():
        return list(mongo.db.Subjects.find())
    
    def confirm_booking(booking_id):
        return mongo.db.Subjects.update_one({'_id': ObjectId(booking_id)}, {'$set': {'bookingstatus': 'Confirmed'}})

    def delete_record(delete_id):
        return mongo.db.Subjects.delete_one({'_id': ObjectId(delete_id)})  
    
    

    
    


