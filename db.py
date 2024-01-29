import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

dbcofig=credentials.Certificate("source.json")
app =firebase_admin.initialize_app(dbcofig)

db=firestore.client(app)

User=db.collection('Profile')
import json


class database():
    def profile_create(data):
        profile=User.add(data)
        print('document uploaded suceessfully')

   
    def profile_search():
        data=User.stream()
        user=[]
        for i in data:
            user_data=i.to_dict()
            user.append(user_data)
        
        return user




