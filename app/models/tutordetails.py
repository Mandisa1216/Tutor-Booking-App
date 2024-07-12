from ..import mongo
class tutor:
    def tutor_details():
        return mongo.db.new_tutors.find()
    
    def display():
        return mongo.db.new_tutors.find()