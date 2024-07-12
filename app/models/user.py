from ..import mongo
from flask import request, redirect, url_for, render_template

class user:
      def create_user(details):
         return mongo.db.user_collection.insert_one(details)
    
      def get_all_user_collection(login):
         return mongo.db.user_collection.find_one(login)
   
      def create_tutor_signup(user_tutor):
         return mongo.db.new_tutors.insert_one(user_tutor)
     
       
      def get_all_tutor_login(user_tutor):
         return mongo.db.new_tutors.insert_one(user_tutor)
    
      