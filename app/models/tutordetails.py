from ..import mongo

class tutor:
    def tutor_details():
        return mongo.db.new_tutors.find()
 
    
    