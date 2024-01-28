import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

dbcofig=credentials.Certificate("source.json")
app =firebase_admin.initialize_app(dbcofig)

db=firestore.client(app)

User=db.collection('Profile')


class database():
    def profile_create(data):
        profile=User.add(data)
        print('document uploaded suceessfully')

    def profile_search():
        profile=User.document.get().to_dict()
        print(profile)
        return profile





