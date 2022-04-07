from firebase_admin import credentials, firestore, initialize_app
import threading


cred = credentials.Certificate('ntpu-all-star-firebase-adminsdk-yq6fs-cda9dd2d3d.json')
initialize_app(cred)
db = firestore.client()

doc_ref = db.collection(u'user')

doc = doc_ref.get()
# for d in doc:
#     print(d.to_dict()['email'], d.to_dict()['displayName'])
print(len(doc))
